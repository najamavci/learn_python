from datetime import date, timedelta

today = date.today()
future_date = today + timedelta(days=7)

print("Today's date:", today)
print("Date in 7 days:", future_date)
