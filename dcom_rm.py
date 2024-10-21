import sys

def is_digit(c):
    return '0' <= c <= '9'

def is_valid_date(date):
    """Validate the date format DD/MM/YYYY or D/M/YYYY."""
    parts = date.split('/')
    if len(parts) != 3:
        return False
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    day, month, year = int(day), int(month), int(year)
    if month < 1 or month > 12 or year < 1000 or year > 9999:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    return 1 <= day <= days_in_month[month - 1]

def find_date(text):
    """Find a date in the format D/M/YYYY or DD/MM/YYYY in the given text."""
    i = 0
    while i < len(text):
        if is_digit(text[i]):
            start = i
            while i < len(text) and (is_digit(text[i]) or text[i] == '/'):
                i += 1
            potential_date = text[start:i].strip()
            if is_valid_date(potential_date):
                return potential_date
        i += 1
    return None

def is_date_in_comment(comment):
    """Check if a comment contains a valid date."""
    comment = comment.strip()  # Handle spaces before the date
    return find_date(comment) is not None

def remove_dated_comments(input_file, output_file):
    """Remove comments with valid dates from the input C++ file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        in_multi_line_comment = False
        multi_line_comment = ""

        for line in infile:
            if not in_multi_line_comment:
                # Check for start of multi-line comment
                if "/*" in line:
                    parts = line.split("/*", 1)
                    outfile.write(parts[0].rstrip())  # Write code before comment
                    multi_line_comment = "/*" + parts[1]  # Capture start of comment
                    in_multi_line_comment = True
                elif "//" in line:
                    # Handle single-line comment
                    parts = line.split("//", 1)
                    comment_content = parts[1].strip()
                    if not is_date_in_comment(comment_content):
                        outfile.write(parts[0] + "//" + comment_content + "\n")
                    else:
                        outfile.write(parts[0].rstrip() + "\n")  # Skip the comment
                else:
                    # No comment in line
                    outfile.write(line)
            else:
                # Accumulate multi-line comment until it's closed
                multi_line_comment += line
                if "*/" in line:
                    in_multi_line_comment = False
                    # Now check the entire multi-line comment for a date
                    if not is_date_in_comment(multi_line_comment):
                        outfile.write(multi_line_comment)
                    else:
                        outfile.write("\n")  # Skip the multi-line comment
                    multi_line_comment = ""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dcom_rm.py inputC.cpp inputC_rm.cpp")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_dated_comments(input_file, output_file)
