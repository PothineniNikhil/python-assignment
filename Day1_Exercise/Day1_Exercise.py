def calculate_total_days(distance_km, speed_kmph, hours_per_day):
    total_hours = distance_km / speed_kmph
    return total_hours / hours_per_day

def convert_days_to_ymdh(total_days):
    years = int(total_days // 365)
    remaining_days = total_days % 365

    months = int(remaining_days // 30)
    days = int(remaining_days % 30)

    fractional_day = remaining_days % 1
    hours = int(fractional_day * 24)

    return years, months, days, hours

def display_time_required(distance_km, speed_kmph, hours_per_day):
    total_days = calculate_total_days(distance_km, speed_kmph, hours_per_day)
    years, months, days, hours = convert_days_to_ymdh(total_days)
    print(f"Time required: {years} years, {months} months, {days} days, {hours} hours")

total_distance_km = 10000
avg_speed_kmph = 8
daily_travel_hours = 5


display_time_required(total_distance_km, avg_speed_kmph, daily_travel_hours)
