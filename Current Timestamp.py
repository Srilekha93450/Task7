import os
from datetime import datetime

def create_file_with_timestamp():
    # Get the current timestamp
    current_time = datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the file name with the timestamp
    file_name = f"{timestamp_str}.txt"
    
    # Write the content into the file
    with open(file_name, 'w') as file:
        # Write the timestamp as the content of the file
        file.write(timestamp_str)

# Call the function to create the file with the current timestamp
create_file_with_timestamp()
