import socket
import time

def is_computer_online(hostname, port, timeout=5):
    try:
        # Create a socket object
        with socket.create_connection((hostname, port), timeout=timeout) as s:
            return True
    except (socket.timeout, socket.error):
        return False

def wait_until_booted(hostname, port, timeout=300, interval=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if is_computer_online(hostname, port):
            print(f"{hostname} is online.")
            return True
        time.sleep(interval)

    print(f"Timeout: {hostname} did not come online within {timeout} seconds.")
    return False

# Get user input for the target hostname
target_hostname = input("Enter the target computer name or IP address: ")

# Default RDP port
rdp_port = 3389

if wait_until_booted(target_hostname, rdp_port):
    print(f"{target_hostname} is online.")
    # Your additional code here, the computer is online
    # For example, you can proceed with further tasks or connect using other methods.
    # Add your custom logic or commands here.
else:
    print(f"{target_hostname} is not online.")
