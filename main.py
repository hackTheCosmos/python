seconds = 233726600

minute = 60
hour = 3600
day = 24*3600
month = 30*24*3600
year = 12*30*24*3600

date_years = seconds // year
date_months = (seconds % year) // month
date_days = (seconds % month) // day
date_hours = (seconds % day) // hour
date_minutes = (seconds % hour) // minute
date_seconds = seconds % 60

print(f"{seconds} secondes = {date_years} années,{date_months} mois,{date_days} jours,{date_hours} heures,{date_minutes} minutes,{date_seconds} secondes ")