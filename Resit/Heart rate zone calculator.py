def calculate_heart_rate_zone(age,heart_rate): #Make a function to calculate the zone of heart rate
    max_heart_rate=220-age #Define the max heart rate
    if heart_rate > max_heart_rate:
        return "Error: Heart rate too high"
    if heart_rate < 0.5*max_heart_rate:
        return "Error: Heart rate too low"
    if 0.5*max_heart_rate <= heart_rate < 0.6*max_heart_rate:
        return "1, very light exercise"
    if 0.6*max_heart_rate <= heart_rate < 0.7*max_heart_rate:
        return "2, light exercise"
    if 0.7*max_heart_rate <= heart_rate < 0.8*max_heart_rate:
        return "3, moderate exercise"
    if 0.8*max_heart_rate <= heart_rate < 0.9*max_heart_rate:
        return "4, hard exercise"
    if 0.9*max_heart_rate <= heart_rate <= 1*max_heart_rate:
        return "5, maximum"
print(calculate_heart_rate_zone(19,130)) #Show an example
