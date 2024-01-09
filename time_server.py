# list of timezones may be found at: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
import datetime
import pytz
import socket

def get_time():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('time.nist.gov', 13)  #Port 13 is called the daytime port for reading and displaying current date and time
    client_sock.connect(server_address)
    time_data = client_socket.recv(1024).decode('utf-8') # Receive atmost 1024 bytes
    client_sock.close()
    date_str, time_str = time_data.split()[1], time_data.split()[2] #date and time extracted and converted to strings
    time_str = f"{date_str} {time_str}" # Format to single string
    return datetime.datetime.strptime(time_str, '%y-%m-%d %H:%M:%S').replace(tzinfo=pytz.UTC)

def run_timeserver():
    print("Welcome to the Time Server!")
    while True:
        timezone = input("Please enter a valid timezone (e.g. 'Asia/Kolkata'): ")
        try:
            tz = pytz.timezone(timezone)
            break
        except pytz.exceptions.UnknownTimeZoneError:
            print("Invalid timezone entered. Please try again.")
            
    curr_time = get_time()
    #print(curr_time)
    curr_time = curr_time.astimezone(tz)
    print("The current time is:", curr_time.strftime('%Y-%m-%d %H:%M:%S %Z')
run_time_server()
