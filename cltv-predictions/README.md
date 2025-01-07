# Customer Life Time Predictions (CLTV) with BG/NBD and Gamma Gamma SubModel - Retail Data [ENG]
## Dataset link:
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II
## About dataset:
This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011.The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.
## Attribute Information:
- InvoiceNo:   Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
- StockCode:   Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
- Description: Product (item) name. Nominal.
- Quantity:    The quantities of each product (item) per transaction. Numeric.
- InvoiceDate: Invice date and time. Numeric. The day and time when a transaction was generated.
- UnitPrice:   Unit price. Numeric. Product price per unit in sterling (Â£).
- CustomerID:  Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
- Country:     Country name. Nominal. The name of the country where a customer resides.
## Input:
data/input/online_retail_II.xlsx
## Output:
data/output/cltv-predictions/cltv_predictions.csv



# BG/NBD ve Gamma Gamma Sub Modelini kullanarak Müşteri Yaşam Döngüsü Tahmini - Perakende Verisi ile [TUR]
## Veriseti linki:
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II
## Veriseti hakkında:
Bu Online Retail II veri seti, 01/12/2009 ile 09/12/2011 tarihleri ​​arasında İngiltere merkezli ve kayıtlı, mağaza dışı bir online perakende için gerçekleşen tüm işlemleri içerir. Şirket çoğunlukla benzersiz, her duruma uygun hediyelik eşyalar satmaktadır. Şirketin birçok müşterisi toptancıdır.
## Değişkenler:
- InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem.
- StockCode:    Ürün kodu. Her bir ürün için eşsiz numara.
- Description:  Ürün ismi
- Quantity:     Ürün adedi. Faturalardaki ürünlerden kaçar tane satıldığını ifade etmektedir.
- InvoiceDate:  Fatura tarihi ve zamanı.
- UnitPrice:    Ürün fiyatı (Sterlin cinsinden)
- CustomerID:   Eşsiz müşteri numarası
- Country:      Ülke ismi. Müşterinin yaşadığı ülke.
## Girdi:
data/input/online_retail_II.xlsx
## Çıktı:
data/output/cltv-predictions/cltv_predictions.csv