""" 
energy blocks and energy scalars
"""
from datetime import datetime

def answer(month_data):
    """ 
    energy blocks and energy scalars
    """
    peak_avg, off_peak_avg = 0, 0
    for index in range(0, len(month_data), 24):
        day_data = month_data[index:index+24]
        print(len(day_data))
        peak_hours = day_data[6:22]
        off_peak_hours = day_data[0:6] + day_data[22:]
        peak_avg += sum(data['price'] for data in peak_hours)/16
        off_peak_avg += sum(data['price'] for data in off_peak_hours)/8

    date_string = month_data[0]["date"]

    formatted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime(
        "%Y-%m"
    )
    print(len(month_data)/24)
    peak_avg /= (len(month_data)/24)
    off_peak_avg /= (len(month_data)/24)
    return {
        "date": formatted_date,
        "peak_energy_block": f"{peak_avg:.2f}",
        "off_peak_energy_block": f"{off_peak_avg:.2f}"
    }

