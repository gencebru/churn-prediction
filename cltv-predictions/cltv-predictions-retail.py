import pandas as pd
import datetime as dt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
import matplotlib.pyplot as plt
from lifetimes.plotting import plot_period_transactions
from sklearn.preprocessing import MinMaxScaler

df_ = pd.read_excel("data/input/online_retail_II.xlsx" ,sheet_name='Year 2010-2011')
df = df_.copy()
df.head()

df.dropna(inplace=True)
df = df[~df["Invoice"].str.contains("C", na=False)]
df = df[df["Quantity"] > 0]
df['TotalPrice'] = df['Price'] * df['Quantity']

today_date = dt.datetime(2011, 12, 11)

cltv = df.groupby('Customer ID').agg({'InvoiceDate': [
        lambda x: (x.max() - x.min()).days,  # recency
        lambda x: (today_date - x.min()).days  # T
],
    'Invoice': lambda x: x.nunique(),  # frequency
    'TotalPrice': lambda x: x.sum()  # monetary
})

cltv.columns = cltv.columns.droplevel(0)

cltv.columns = ['recency', 'T', 'frequency', 'monetary']

cltv = cltv[cltv['monetary'] > 0]
cltv['monetary'] = cltv['monetary'] / cltv['frequency']

cltv['recency'] = cltv['recency'] / 7
cltv['T'] = cltv['T'] / 7

cltv = cltv[(cltv['frequency'] > 1)]

# NG-NBD modelini oluşturma:
bgf = BetaGeoFitter(penalizer_coef=0.001)
bgf.fit(cltv['frequency'], cltv['recency'], cltv['T'])

# örnek-1
# Bir haftada en fazla satın alma işlemi yapması beklenen ilk 10 müşteri

bgf.conditional_expected_number_of_purchases_up_to_time(1, # hafta
                                                        cltv['frequency'],
                                                        cltv['recency'],
                                                        cltv['T']).sort_values(ascending=False).head(10)

# bir ayda en fazla satın alma işlemi yapması beklenen ilk 10 müşteri

bgf.conditional_expected_number_of_purchases_up_to_time(4,
                                                 # 4 hafta = 1 ay
                                                        cltv['frequency'],
                                                        cltv['recency'],
                                                        cltv['T']).sort_values(ascending=False).head(10)

# önemli not: bu model haftaları baz alarak çalışıyor. buna dikkat edilmeli!

# gelecek 6 ayda en çok satın alma işlemi yapması beklenen ilk 10 müşteri:

bgf.conditional_expected_number_of_purchases_up_to_time(4 * 6,
                                           # hafta * sayısı = ay
                                                        cltv['frequency'],
                                                        cltv['recency'],
                                                        cltv['T']).sort_values(ascending=False).head(10)

# gelecek 6 ayda yapılması beklenen toplam işlem-satış sayısı:

bgf.conditional_expected_number_of_purchases_up_to_time(4 * 6,
                                                        cltv['frequency'],
                                                        cltv['recency'],
                                                        cltv['T']).sum()


# gamma gamma alt modelinin oluşturulması

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv['frequency'], cltv['monetary'])

#örnek-2
# En değerli olması beklenen ilk 10 müşteri:

ggf.conditional_expected_average_profit(cltv['frequency'],
                               cltv['monetary']).sort_values(ascending=False).head(10)

# BG-NBD ve gamma gamma modeli kullanarak cltv'yi tahmin etme:

cltv['cltv_pred_3_months'] = ggf.customer_lifetime_value(bgf,
                                   cltv['frequency'],
                                   cltv['recency'],
                                   cltv['T'],
                                   cltv['monetary'],
                                   time=3,  # 3 ay
                                   freq="W",
                                   discount_rate=0.01)
cltv


cltv['segment'] = pd.qcut(cltv['cltv_pred_3_months'],4,labels=['D','C','B','A'])

cltv.sort_values(by="cltv_pred_3_months", ascending=False).tail()

cltv.groupby("segment").agg({"count","mean","sum"})

cltv.to_csv("cltv_predictions.csv")


# Fonksiyonlaştırma: 

def outlier_thresholds(dataframe,variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit,up_limit

def replace_with_thresholds(dataframe,variable):
    low_limit, up_limit = outlier_thresholds(dataframe,variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit),variable] = up_limit





def create_cltv_p(dataframe, month=3):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    today_date = dt.datetime(2011,12,11)

    cltv_df = dataframe.groupby("Customer ID").agg(
        {"InvoiceDate": [lambda InvoiceDate : (InvoiceDate.max() - InvoiceDate.min()).days,
         lambda InvoiceDate: (today_date - InvoiceDate.min()).days],
         "Invoice": lambda Invoice: Invoice.nunique(),
         "TotalPrice": lambda TotalPrice: TotalPrice.sum()
        }
    )

    cltv_df.columns = cltv_df.columns.droplevel(0)
    cltv_df.columns = ["recency", "T", "frequency"," monetary"]
    cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]
    cltv_df = cltv_df[(cltv_df["frequency"] > 1 )]
    cltv_df["recency"]  = cltv_df["recency"] / 7
    cltv_df["T"] = cltv_df["T"] / 7

    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df["frequency"],
            cltv_df["recency"],
            cltv_df["T"])

    cltv_df["expected_purchase_1_week"] = bgf.predict(1,
                                                      cltv_df["frequency"],
                                                      cltv_df["recency"],
                                                      cltv_df["T"])
    cltv_df["expected_purchase_1_month"]= bgf.predict(4,
                                                      cltv_df["frequency"],
                                                      cltv_df["recency"],
                                                      cltv_df["T"])
    cltv_df["expected_purchase_3_month"] = bgf.predict(12,
                                                      cltv_df["frequency"],
                                                      cltv_df["recency"],
                                                      cltv_df["T"])

    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df["frequency"], cltv_df["monetary"])
    cltv_df["expected_average_profit"]  = ggf.conditional_expected_average_profit(cltv_df["frequency"],
                                                                                  cltv_df["monetary"])
    cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df["frequency"],
                                       cltv_df["recency"],
                                       cltv_df["T"],
                                       cltv_df["monetary"],
                                       time=month, #3 aylık
                                       freq="W", # Tnin frekans bilgisi
                                       discount_rate=0.01)
    cltv = cltv.reset_index()
    cltv_final = cltv_df.merge(cltv, on="Customer ID", how="left")
    cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D","C","B","A"])

    return  cltv_final

df = df_.copy()
cltv_final2 = create_cltv_p(df)