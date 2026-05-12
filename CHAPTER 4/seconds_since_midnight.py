def seconds_since_midnight(hour, minute, seconds):
    hour_in_seconds = hour * 60 * 60
    minute_in_seconds = minute * 60
    converter = hour_in_seconds + minute_in_seconds + seconds
    return converter
    
