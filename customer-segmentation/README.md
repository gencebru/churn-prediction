# Customer Segmentation with RFM - RETAIL DATA [ENG]
## Dataset link: 
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II#
## Data Set Information:
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
## Goal:
An e-commerce company wants to segment its customers and determine marketing strategies according to these segments.
## Input:
data/input/online_retail_II.xlsx -> dataset path in repository
## Output:
data/output/retail-data/*        -> output folder for this study in repository



# RFM ile müşteri segmentasyonu - Perakende Verisi ile [TUR]
## Veriseti linki
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II#
## Veri seti hakkında:
Bu Online Retail II veri seti, 01/12/2009 ile 09/12/2011 tarihleri ​​arasında İngiltere merkezli ve kayıtlı, mağaza dışı bir online perakende için gerçekleşen tüm işlemleri içerir. Şirket çoğunlukla benzersiz, her duruma uygun hediyelik eşyalar satmaktadır. Şirketin birçok müşterisi toptancıdır.
## Değişkenler hakkında bilgilendirme:
- InvoiceNo:    Fatura numarası. Her işleme yani faturaya ait eşsiz numara. C ile başlıyorsa iptal edilen işlem.
- StockCode:    Ürün kodu. Her bir ürün için eşsiz numara.
- Description:  Ürün ismi
- Quantity:     Ürün adedi. Faturalardaki ürünlerden kaçar tane satıldığını ifade etmektedir.
- InvoiceDate:  Fatura tarihi ve zamanı.
- UnitPrice:    Ürün fiyatı (Sterlin cinsinden)
- CustomerID:   Eşsiz müşteri numarası
- Country:      Ülke ismi. Müşterinin yaşadığı ülke.
## Hedef:
Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
## Girdi:
data/input/online_retail_II.xlsx -> Bu repository içindeki verisetinin bulunduğu uzantı
## Çıktı:
data/output/retail-data/*        -> Bu repository içindeki çıktı klasörünün uzantısı







# Customer Segmentation with RFM Analysis - FLO Dataset [ENG]
## About dataset:
The dataset consists of information obtained from the past shopping behavior of customers who made their last purchases from Flo as OmniChannel (both online and offline shopping) in 2020 - 2021.
## Attribute informations:
- master_id:                         unique customer ID
- order_channel :                    Which channel of the shopping platform is used (Android, iOS, Desktop, Mobile)
- last_order_channel:                The channel/platform where the last purchase was made
- first_order_date:                  Date of the customer's first purchase
- last_order_date:                   Date of the customer's last purchase
- last_order_date_online:            The customer's last shopping date on the online platform
- last_order_date_offline:           The customer's last shopping date on the offline platform
- order_num_total_ever_online:       The total number of purchases made by the customer on the online platform
- order_num_total_ever_offline:      Total number of purchases made by the customer offline
- customer_value_total_ever_offline: Total amount paid by the customer for offline shopping
- customer_value_total_ever_online : Total amount paid by the customer for online shopping
- interested_in_categories_12 :      List of categories the customer has shopped in the last 12 months
## Input:
Unfortunately I can not add the complete dataset. 
## Output:
data/output/flo-data/*


# RFM Analizi ile Müşteri Segmentasyonu - FLO Dataset [TUR]
## Veri seti hakkında
Veri seti Flo’dan son alışverişlerini 2020 - 2021 yıllarında OmniChannel (hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından elde edilen bilgilerden oluşmaktadır.
## Değişkenler:
- master_id:                         Eşsiz müşteri numarası
- order_channel:                     Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile)
- last_order_channel:                En son alışverişin yapıldığı kanal
- first_order_date:                  Müşterinin yaptığı ilk alışveriş tarihi
- last_order_date:                   Müşterinin yaptığı son alışveriş tarihi
- last_order_date_online:            Müşterinin online platformda yaptığı son alışveriş tarihi
- last_order_date_offline:           Müşterinin offline platformda yaptığı son alışveriş tarihi
- order_num_total_ever_online:       Müşterinin online platformda yaptığı toplam alışveriş sayısı
- order_num_total_ever_offline:      Müşterinin offline'da yaptığı toplam alışveriş sayısı
- customer_value_total_ever_offline: Müşterinin offline alışverişlerinde ödediği toplam ücret
- customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
- interested_in_categories_12 :      Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi
## Girdi:
Bütün veri setini maalesef ki ekleyemem. (Çalışmayı -bu veri seti ile olmasa da- incelemek isteyenler açık kaynak verisetini inceleyebilir - perakende veri seti)
## Çıktı:
data/output/flo-data/*  -> çıktı klasörü.