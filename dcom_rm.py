import sys

# Author: Khushal Mehta

def is_digit(c):
    """Check if a character is a digit (0-9)."""
    return '0' <= c <= '9'

def is_valid_date(date):
    """Validate the date format DD/MM/YYYY."""
    if len(date) != 10:  # Ensure the length is 10 characters
        return False
    if date[2] != '/' or date[5] != '/':  # Check for correct slashes
        return False
    day = int(date[0:2])  # Extract day
    month = int(date[3:5])  # Extract month
    year = int(date[6:10])  # Extract year
    # Validate day, month, and year ranges
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1000 or year > 9999:
        return False
    return True

def is_date_in_comment(comment):
    """Check if a comment contains a valid date."""
    for i in range(len(comment) - 9):  # Loop through the comment
        potential_date = comment[i:i+10]  # Extract a substring of length 10
        if is_valid_date(potential_date):  # Check if it's a valid date
            return True  # Return True if a valid date is found
    return False  # Return False if no valid date is found

def remove_dated_comments(input_file, output_file):
    """Remove comments with valid dates from the input C++ file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        inside_multiline_comment = False  # Track if inside a multi-line comment
        current_multiline_comment = ""  # Store the current multi-line comment
        for line in infile:
            if not inside_multiline_comment:  # Not inside a multi-line comment
                # Check for single-line comment
                if '//' in line:
                    comment_start = line.index('//')  # Find start of single-line comment
                    code = line[:comment_start]  # Get code part
                    comment = line[comment_start:]  # Get comment part
                    if not is_date_in_comment(comment):  # Check if date is in comment
                        outfile.write(line)  # Write the whole line if no date
                    else:
                        outfile.write(code + '\n')  # Write only code part if date is present
                # Check for start of multi-line comment
                elif '/*' in line:
                    inside_multiline_comment = True  # Set flag to True
                    comment_start = line.index('/*')  # Find start of multi-line comment
                    code = line[:comment_start]  # Get code part
                    current_multiline_comment = line[comment_start:]  # Store multi-line comment
                    outfile.write(code)  # Write the code part
                else:
                    outfile.write(line)  # Write lines without comments as they are
            else:
                # Inside multi-line comment
                current_multiline_comment += line  # Accumulate lines for multi-line comment
                if '*/' in line:  # Check for end of multi-line comment
                    inside_multiline_comment = False  # Reset flag
                    if not is_date_in_comment(current_multiline_comment):  # Check for date
                        outfile.write(current_multiline_comment)  # Write multi-line comment if no date
                    current_multiline_comment = ""  # Reset multi-line comment accumulator

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python dcom_rm.py inputC.cpp inputC_rm.cpp")
        sys.exit(1)  # Exit if incorrect arguments
    input_file = sys.argv[1]  # Get input file name
    output_file = sys.argv[2]  # Get output file name
    remove_dated_comments(input_file, output_file)  # Call the function to remove dated comments
