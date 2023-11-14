# try_643_version2

# Data Cleaning and Joining Tool

This Python script is designed to clean and join two CSV files containing contact information and additional details. The cleaned and joined data is then saved as a new CSV file.

### Requirements
Python 3.x
pandas library
### Usage
1. Install the required libraries:
pip install pandas

2. Run the script with the following command:
python script_name.py contact_info_file.csv other_info_file.csv output_file.csv

* `contact_info_file.csv`: CSV file containing contact information.
* `other_info_file.csv`: CSV file containing additional information.
* `output_file.csv`: Desired name for the cleaned and joined output file.

### Functionality
* The script reads two CSV files specified as command-line arguments: contact_info_file and other_info_file.
* It performs a left join on the 'respondent_id' column to combine the information from both files.
* The 'birthdate' column is converted to a datetime format using the '%m%d%Y' format.
* The cleaned and joined data is saved to the specified output_file.
