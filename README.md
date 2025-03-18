# Email Typo Checker

A Python utility tool that catches and corrects common email typos, helping you clean up your contact lists.

## Overview

Email Typo Checker is designed to help clean up email lists by identifying and correcting common typos in email domains. Using Levenshtein distance algorithm, it compares input domains against a comprehensive database of common email providers to suggest corrections for potential typos.

## Features

- Validates email address format using regex
- Detects potential typos in email domains
- Suggests corrections for mistyped domains
- Calculates confidence level for suggested corrections
- Processes CSV files with email addresses
- Automatically identifies email column headers
- Supports both CSV files and simple text lists
- Generates detailed output reports
- Includes an extensive database of common email domains

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/tom-sather/email-typo-checker.git
cd email-typo-checker
```

## Dependencies

This script requires Python 3.6+ and uses only standard library modules:
- csv
- sys
- re
- typing

No external dependencies to install!

## Usage

### Basic Usage

```bash
python typochecker.py emails.csv
```

This will process the file `emails.csv` and display a summary of results in the console.

### Saving Results

```bash
python typochecker.py emails.csv output.csv
```

This will process `emails.csv` and save detailed results to `output.csv`.

### Input File Format

The script accepts two formats:

1. **CSV files** with headers (will automatically look for email column)
2. **Simple text files** with one email address per line

## How It Works

1. The script reads the input file and determines if it's a CSV or a simple list
2. For CSV files, it attempts to identify the email column
3. Each email is validated for correct format
4. The domain portion is compared against a database of common email domains
5. If a potential typo is detected, a correction is suggested based on Levenshtein distance
6. A confidence score is calculated for each suggestion
7. Results are summarized and optionally saved to an output file

## Output Format

When saving results to a CSV file, the following columns are included:

- **Email**: The original email address
- **Valid**: Whether the email is valid (Yes/No)
- **Suggested Correction**: Suggested correction if a typo is detected
- **Confidence**: Confidence level of the suggestion (as percentage)

## Example

For an input email `john.doe@gmial.com`, the tool might suggest:
```
john.doe@gmial.com → john.doe@gmail.com (95.0% confident)
```

## Domain Database

The tool includes a comprehensive database of common email domains, including:
- Gmail, Outlook, Hotmail, Yahoo, AOL, and many others
- Regional variants of major providers
- Country-specific domains

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

Potential areas for improvement:
- Adding more domains to the database
- Improving the domain matching algorithm
- Adding support for more input formats
- Implementing a GUI interface

## Author

Your Name
