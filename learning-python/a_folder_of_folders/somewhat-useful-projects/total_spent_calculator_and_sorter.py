import pandas as pd

df1 = pd.read_csv("Retail.OrderHistory.1.csv")
df2 = pd.read_csv("Retail.OrderHistory.2.csv")

order_data = pd.concat([df1, df2], ignore_index=True)

total_spent_pd = sum(order_data["Total Owed"])

order_data = order_data.sort_values(by=["Total Owed"])
print(order_data.head())

order_data.to_csv("order_data.csv")

total_spent = 0
for price, item, date, status in zip(order_data["Total Owed"], order_data["Product Name"], order_data["Order Date"],order_data["Order Status"]):
    if status != "Cancelled":
        print("%.2f - %s - %s" % (price, item, date))
        total_spent += price
    else: print(status, item, price)

print('''-----------------
£%.2f''' % (total_spent))