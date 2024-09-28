# Dated Comment Remover

## Description

The Date Comment Remover is a Python script designed to remove comments containing dates from C++ source files. It specifically targets comments with dates in the format DD/MM/YYYY. This tool is useful for cleaning up code by removing outdated or unnecessary dated comments while preserving the overall structure and non-dated comments.

## Features

- Removes single-line comments (//) containing dates
- Removes multi-line comments (/* */) containing dates
- Preserves code structure and non-dated comments
- Handles inline comments
- Supports nested comments
- Properly processes incomplete multi-line comments

## Requirements

- Python 3.x

No additional libraries are required. The script uses only built-in Python modules.

## Usage

1. Save the script as `dcom_rm.py` in your project directory.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script using the following command:

   ```
   python dcom_rm.py input_file.cpp output_file.cpp
   ```

   Replace `input_file.cpp` with the path to your input C++ file, and `output_file.cpp` with the desired path for the processed output file.

## Example

Input file (`input.cpp`):

```cpp
#include <iostream>
using namespace std;
int main() {
    // 01/01/2023 This comment will be removed
    cout << "Hello World!" << endl;
    /* This multi-line comment
       05/05/2020 contains a date
       and will be removed */
    int x = 10; // This comment stays
    return 0;
}
```

Command:

```
python dcom_rm.py input.cpp output.cpp
```

Output file (`output.cpp`):

```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello World!" << endl;
    int x = 10; // This comment stays
    return 0;
}
```

## Limitations

- The script only recognizes dates in the format DD/MM/YYYY.
- It does not check for the validity of dates (e.g., 31/02/2023 would be considered a valid date).
- The script does not handle comments that span multiple lines if they are not properly formatted as multi-line comments.

## License

This project is open-source and available under the MIT License.
