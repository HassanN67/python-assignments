def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify content (example: uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("File successfully processed! Modified version saved as 'output.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    read_and_modify_file()

