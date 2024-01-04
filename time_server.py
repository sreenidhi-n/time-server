import datetime
import pytz
import socket

def get_time_from_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('time.nist.gov', 13)  #Port 13 is called the daytime port for reading and displaying current date and time
    client_socket.connect(server_address)
    time_data = client_socket.recv(1024).decode('utf-8') # Receive atmost 1024 bytes
    client_socket.close()
    date_str, time_str = time_data.split()[1], time_data.split()[2] #date and time extracted and converted to strings
    time_str = f"{date_str} {time_str}" # Format to single string
    return datetime.datetime.strptime(time_str, '%y-%m-%d %H:%M:%S').replace(tzinfo=pytz.UTC)

#Function to run the time server and allow timezone selection and time synchronization.
def run_time_server():
    print("Welcome to the Time Server!")
    while True:
        # Get the timezone selection from the user
        timezone = input("Please enter a valid timezone (e.g. 'US/Pacific'): ")
        try:
            tz = pytz.timezone(timezone)
            break
        except pytz.exceptions.UnknownTimeZoneError:
            print("Invalid timezone entered. Please try again.")
    current_time = get_time_from_server()
    #print(current_time)
    current_time = current_time.astimezone(tz)
    print("The current time is:", current_time.strftime('%Y-%m-%d %H:%M:%S %Z'))

run_time_server()
