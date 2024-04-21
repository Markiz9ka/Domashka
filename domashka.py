from datetime import datetime

def get_days_from_today(date):
    try: 
        zadana_data = datetime.strptime(date, "%Y.%d.%m").date()
        today = datetime.today().date()
        diff = today - zadana_data
        return diff.days
    except ValueError:
        print("Неправельний формат дати")

days_difference = get_days_from_today("2024.21.03")
print(days_difference)
