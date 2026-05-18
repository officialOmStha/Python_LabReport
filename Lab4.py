# Lab 4:

import os


class FileProcessor:

    # Method to write data to a file
    def write_to_file(self, filename, data):

        try:
            file = open(filename, "w")
            file.write(data)

        except PermissionError:
            print("Permission denied while writing to the file.")

        except IOError:
            print("An input/output error occurred while writing.")

        else:
            print("Data written successfully.")

        finally:
            try:
                file.close()
                print("Write operation completed.")
            except:
                pass

    # Method to read data from a file
    def read_from_file(self, filename):

        try:
            file = open(filename, "r")
            content = file.read()

        except FileNotFoundError:
            print("File not found.")

        except PermissionError:
            print("Permission denied while reading the file.")

        except IOError:
            print("An input/output error occurred while reading.")

        else:
            print("File read successfully.")
            return content

        finally:
            try:
                file.close()
                print("Read operation completed.")
            except:
                pass

    # Method to append data to a file
    def append_to_file(self, filename, data):

        try:
            file = open(filename, "a")
            file.write(data)

        except PermissionError:
            print("Permission denied while appending to the file.")

        except IOError:
            print("An input/output error occurred while appending.")

        else:
            print("Data appended successfully.")

        finally:
            try:
                file.close()
                print("Append operation completed.")
            except:
                pass


# Main program

# Create object
fp = FileProcessor()

filename = "sample.txt"

# Write data
fp.write_to_file(filename, "Hello, this is the first line.\n")

# Check if file exists before reading
if os.path.exists(filename):

    # Read file content
    content = fp.read_from_file(filename)

    print("\nFile Content:")
    print(content)

else:
    print("File does not exist.")

# Append new text
fp.append_to_file(filename, "This is the appended line.\n")

# Read updated content
print("\nUpdated File Content:")
updated_content = fp.read_from_file(filename)
print(updated_content)