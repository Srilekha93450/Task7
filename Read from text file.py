def read_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            # Print the content of the file
            print("File Content:")
            print(file_content)
    except FileNotFoundError:
        # Print an error message if the file is not found
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        # Print any other exception that occurs
        print("An error occurred:", e)

# Call the function to read and display the content of the text file
read_file("example.txt")
