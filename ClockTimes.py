def clock_times(hour, minute):
    if hour < 1 or hour > 12:
        return "Invalid Number"
    elif minute < 0 or hour > 59:
        return "Invalid Number"

    hour_times = {
        1 : "One",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        10 : "Ten",
        11 : "Eleven",
        12 : "Twelve",
        13 : "Thirteen",
        14 : "Fourteen",
        15 : "Fifteen",
        16 : "Sixteen",
        17 : "Seventeen",
        18 : "Eighteen",
        19 : "Nineteen",
        20 : "Twenty",
        60 : "O'Clock",

    }

    if minute == 0:
        print(hour_times[hour], hour_times[60])
    elif minute == 15:
        print("Quarter Past", hour_times[hour])
    elif minute == 45:
        if hour == 12:
            print('Quarter To', hour_times[1])
        else:
            print("Quarter To", hour_times[hour + 1])
    elif minute == 30:
        print("Half Past", hour_times[hour])
    elif minute > 30:
        if minute < 40 and minute >= 30:
            print(hour_times[20], hour_times[minute - 30 + (10 - (minute - 30) - (minute - 30))], 'minutes to', hour_times[hour + 1])
        else:
            print(hour_times[60 - minute], 'minutes to', hour_times[hour + 1])
    elif minute < 30:
        if minute < 30 and minute >= 20:
            print(hour_times[20], hour_times[minute - 20], 'minutes past', hour_times[hour])
        else:
            print(hour_times[minute], 'minutes past', hour_times[hour])

clock_times(7,00)