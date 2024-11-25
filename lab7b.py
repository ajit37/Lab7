#!/usr/bin/env python3
# Student ID: [seneca_id]
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

        # Handle carry over for seconds
    if sum.second >= 60:
        extra_minutes = sum.second // 60
        sum.second = sum.second % 60
        sum.minute += extra_minutes

    # Handle carry over for minutes
    if sum.minute >= 60:
        extra_hours = sum.minute // 60
        sum.minute = sum.minute % 60
        sum.hour += extra_hours

    # Optional: Ensure the hour is within a valid range (0-23).
    if sum.hour >= 24:
        sum.hour = sum.hour % 24

    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):

 # Add the seconds to the current time's seconds
    time.second += seconds
    
    # Handle seconds that overflow or underflow
    while time.second >= 60:  # If seconds are 60 or more, carry over to minutes
        time.second -= 60
        time.minute += 1
    while time.second < 0:  # If seconds are negative, borrow from minutes
        time.second += 60
        time.minute -= 1
    
    # Handle minutes that overflow or underflow
    while time.minute >= 60:  # If minutes are 60 or more, carry over to hours
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:  # If minutes are negative, borrow from hours
        time.minute += 60
        time.hour -= 1
    
    # Optional: Wrap around hour if it goes beyond 24 or negative
    if time.hour >= 24:
        time.hour = time.hour % 24
    elif time.hour < 0:
        time.hour = 24 + time.hour % 24
    
    return None
