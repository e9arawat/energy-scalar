""" 
energy blocks and energy scalars
"""

from datetime import datetime


def find_peak_avg(day_data):
    """
    return the peak block
    """
    peak_hours = day_data[6:22]
    return sum(data["price"] for data in peak_hours) / 16


def find_off_peak_avg(day_data):
    """
    return the off peak block
    """
    off_peak_hours = day_data[0:6] + day_data[22:]
    return sum(data["price"] for data in off_peak_hours) / 8


def find_monthly_hourly_data(month_data):
    """
    return the energy scalar monthly
    """
    peak_avg, off_peak_avg = 0, 0
    monthly_hourly_data = {}
    for index in range(0, len(month_data), 24):
        day_data = month_data[index : index + 24]
        peak_avg += find_peak_avg(day_data)
        off_peak_avg += find_off_peak_avg(day_data)

        for index, hour in enumerate(day_data):
            current_date = hour["date"]
            dt = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
            if dt.hour not in monthly_hourly_data:
                monthly_hourly_data[dt.hour] = 0

            monthly_hourly_data[dt.hour] += hour["price"]

    peak_avg /= len(month_data) // 24
    off_peak_avg /= len(month_data) // 24
    for index, data in enumerate(monthly_hourly_data):
        monthly_hourly_data[data] /= len(month_data) // 24

        if 5 < index < 22:
            monthly_hourly_data[data] /= peak_avg
        else:
            monthly_hourly_data[data] /= off_peak_avg

    return monthly_hourly_data


def answer(month_data):
    """
    energy blocks and energy scalars
    """
    monthly_hourly_data = find_monthly_hourly_data(month_data)

    day_data = month_data[:24]
    monthly_scalar = []
    for day in day_data:
        date_string = day["date"]
        dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        formatted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime(
            "%Y-%m-1 %H:%M:%S"
        )
        monthly_scalar.append(
            {
                "date": formatted_date,
                "energy_scalar": f"{float(monthly_hourly_data[dt.hour]):.2f}",
            }
        )

    print(monthly_scalar)
    return monthly_scalar
