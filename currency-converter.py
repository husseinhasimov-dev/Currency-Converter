import requests , json , time

response=requests.get("api.key")
data=response.json()


def conversion(x,y):
    usd=1/float(data["conversion_rates"][x])
    conv_money=data["conversion_rates"][y]
    return usd*conv_money


your_money=(input("Enter currency that you have (For ex.: 300 USD) : ").upper()).split()
your_conversion=input("Enter currency that you want to convert (For ex.: GBP) : ").upper()

exchange_rate=conversion(your_money[1],your_conversion)

print(f"{your_money[0]} {your_money[1]} equals {(exchange_rate*int(your_money[0])*100//1)/100} {your_conversion}.")

print("Hello from Ubuntu")