
anapara = 1000 #principal
gunluk_faiz_oranı = 0.07 # daily interest rate
gün = 7 #day 
yıl =365 # year
# günlük faiz hesaplama günlük
#bileşik 7 günlük faiz= anapara x(1+dönemlik faiz oranı)**günsayısı - anapara
# çıkan 7 günlük faiz tutarını anapara ile toparlayalım 
# daily interest calculation daily
#compound 7-day interest = principal x(1+periodical interest rate)**number of days - principal
# Let's sum up the 7-day interest amount with the principal
print((anapara)*(gunluk_faiz_oranı/100) * gün) # bileşik banka faizlerini verir 
print(((anapara *(( 1 + gunluk_faiz_oranı)**7)- anapara)) + anapara) 

_7gunluk_getiri  = 1605.7814764784307  #7 days interest earning



