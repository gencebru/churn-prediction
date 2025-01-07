import pandas as pd
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
pd.set_option("display.float_format", lambda x: "%.5f" %x)

df_ = pd.read_excel("data/input/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df = df_.copy()

df.head()
df.isnull().sum()

df = df[~df["Invoice"].str.contains("C", na=False)]
df.describe().T

df = df[(df["Quantity"] > 0)]
df.dropna(inplace=True)

df["TotalPrice"] = df["Quantity"] * df["Price"]


calc_cltv = df.groupby("Customer ID").agg({"Invoice" : lambda x: x.nunique(),
                                           "Quantity" : lambda x: x.sum(),
                                           "TotalPrice" : lambda x: x.sum() })

calc_cltv.columns = ["total_transaction", "total_unit", "total_price" ]
calc_cltv["average_order_value"]  =  calc_cltv["total_price"] / calc_cltv["total_transaction"]
calc_cltv["purchase_frequency"] = calc_cltv["total_transaction"] / calc_cltv.shape[0]

repeat_rate = calc_cltv[calc_cltv["total_transaction"] > 1].shape[0] / calc_cltv.shape[0]
churn_rate = 1 - repeat_rate


calc_cltv["profit_margin"] = calc_cltv["total_price"] * 0.10
calc_cltv["customer_value"] = calc_cltv["average_order_value"] * calc_cltv["purchase_frequency"]
calc_cltv["cltv"] = (calc_cltv["customer_value"] / churn_rate) * calc_cltv["profit_margin"]
calc_cltv.sort_values(by = "cltv", ascending = False).head()
calc_cltv["segment"] = pd.qcut(calc_cltv["cltv"], 4, labels=["D", "C", "B", "A"])
calc_cltv.sort_values(by="cltv", ascending=False).tail()
calc_cltv.groupby("segment").agg({"count", "mean", "sum"})

calc_cltv.to_csv("data/output/cltv.csv")

def create_calculate_cltv(dataframe, profit=0.10):
    #veri ön işleme - data preprocessing
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantitiy"] > 0]
    dataframe.dropna(inplace=True)


    #hesaplamalar - calculations 
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    calc_cltv = dataframe.groupby("Customer ID").agg({"Invoice": lambda x: x.nunique(),
                                                      "Quantity": lambda x: x.sum(),
                                                      "TotalPrice": lambda x: x.sum() })

    calc_cltv.columns = ["total_transaction", "total_unit", "total_price"]
    calc_cltv["average_order_value"] = calc_cltv["total_price"] / calc_cltv["total_transaction"]
    calc_cltv["purchase_frequency"] = calc_cltv["total_transaction"] / calc_cltv.shape[0]
    
    repeat_rate = calc_cltv[calc_cltv["total_transaction"] > 1].shape[0] / calc_cltv.shape[0]
    churn_rate = 1 - repeat_rate
    
    calc_cltv["profit_margin"] = calc_cltv["total_price"] * profit
    calc_cltv["customer_value"] = calc_cltv["average_order_value"] * calc_cltv["purchase_frequency"]
    calc_cltv["cltv"] = (calc_cltv["customer_value"] / churn_rate) * calc_cltv["profit_margin"]
    calc_cltv.sort_values(by="cltv", ascending=False).head()

    calc_cltv["segment"] = pd.qcut(calc_cltv["cltv"], 4, labels=["D", "C", "B", "A"])

    return calc_cltv

df = df_.copy()

cltv = create_calculate_cltv(df)













