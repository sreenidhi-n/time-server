#  time-server
Development of a time server in python which gives time zone selection and time synchronization by contacting an actual time server.

## Features: 
- Connects to the NIST time server to retrieve accurate time
- Allows the user to specify a timezone to display the time in

## Working
- **pytz** library is used to handle timezones whereas the **socket** library is used to connect to the NIST time server
- The user is prompted to enter a valid timezone (e.g., 'Asia/Kolkata')
- A socket is created and connects to the NIST timeserver. It receives the time data and extracts the date and time, converts them to a datetime object and retirns the UTC time.
- The UTC time is then converted to the user-specified timezone using pytz and the current time is printed in the specified timezone.

## Where can I find valid timezones?
A list of valid timezones may be found [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)

