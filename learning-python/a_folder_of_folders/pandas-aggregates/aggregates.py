import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

utm_grouped = ad_clicks.groupby("utm_source").count().reset_index()
print(utm_grouped)

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

clicks_per_source = ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index()

clicks_pivot = clicks_per_source.pivot(columns="is_click",
index="utm_source",
values="user_id").reset_index()

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False]) *100
print(clicks_pivot)

a_b_grouped = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(a_b_grouped)

a_b_grouped_twice = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index()
a_b_grouped_pivot = a_b_grouped_twice.pivot(columns="experimental_group",
index="is_click",
values="user_id")
print(a_b_grouped_pivot)


a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

a_clicks_day = a_clicks.groupby(["is_click","day"]).user_id.count().reset_index()
b_clicks_day = b_clicks.groupby(["is_click","day"]).user_id.count().reset_index()

a_day_pivot = a_clicks_day.pivot(columns="is_click",
index="day",
values="user_id")
b_day_pivot = b_clicks_day.pivot(columns="is_click",
index="day",
values="user_id")

a_day_pivot["pct"] = a_day_pivot[True] / (a_day_pivot[True]+a_day_pivot[False]) *100
b_day_pivot["pct"] = b_day_pivot[True] / (b_day_pivot[True]+b_day_pivot[False]) *100

print(a_day_pivot)
print(b_day_pivot)