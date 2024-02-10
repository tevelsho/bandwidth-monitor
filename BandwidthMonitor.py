import time
import psutil 

# Previous values
last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    # Get the current total amount of bytes that are recevied and sent over the network
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent

    # Difference in bytes sent
    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total

    # Change bytes to megabytes
    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    print(f"MB received: {mb_new_received:.2f}")
    print(f"MB sent: {mb_new_sent:.2f}")
    print(f"MB total: {mb_new_total:.2f}")

    # Update the previous value 
    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total

    # Get every second
    time.sleep(1) 