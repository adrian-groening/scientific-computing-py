def add_time(start, duration, starting_day=None):
    # Split the start time into components
    time, meridiem = start.split()
    start_hour, start_minute = map(int, time.split(':'))
    if meridiem == "PM":
        start_hour += 12  # Convert to 24-hour time
    
    # Split the duration time into components
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minute = total_minutes % 60
    
    # Calculate total hours
    total_hours = start_hour + duration_hour + extra_hours
    final_hour = total_hours % 24
    days_past = total_hours // 24
    
    # Convert back to 12-hour time
    if final_hour == 0:
        final_hour_12 = 12
        final_meridiem = "AM"
    elif final_hour < 12:
        final_hour_12 = final_hour
        final_meridiem = "AM"
    elif final_hour == 12:
        final_hour_12 = 12
        final_meridiem = "PM"
    else:
        final_hour_12 = final_hour - 12
        final_meridiem = "PM"
    
    # Calculate the day of the week if provided
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if starting_day:
        starting_day_index = week_days.index(starting_day.capitalize())
        final_day_index = (starting_day_index + days_past) % 7
        final_day = week_days[final_day_index]
    else:
        final_day = None
    
    # Build the result string
    new_time = f"{final_hour_12}:{final_minute:02d} {final_meridiem}"
    if final_day:
        new_time += f", {final_day}"
    if days_past == 1:
        new_time += " (next day)"
    elif days_past > 1:
        new_time += f" ({days_past} days later)"
    
    return new_time

# Example calls
print(add_time('3:00 PM', '3:10'))  # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # 2:02 PM, Monday
print(add_time('11:43 PM', '24:20', 'tueSday'))  # 12:03 AM, Thursday (2 days later)
