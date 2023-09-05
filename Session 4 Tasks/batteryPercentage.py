from plyer import notification
import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print(percent)

notification.notify(
    title='Battery Percentage',
    message= str(percent) + "% Percent Remaining",
    timeout = 10
    )