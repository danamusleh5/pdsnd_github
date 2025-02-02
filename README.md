# Bikeshare Data Analysis

### Date Created
January 26, 2025

### Project Title
Bikeshare Data Analysis

### Description
This Python program analyzes bikeshare data for three major cities in the United States: Chicago, New York City, and Washington. It provides users with the ability to filter the data by month (from January to June) and day of the week, allowing for tailored analysis. The program calculates and displays various statistics that help explore the bikeshare system, such as:

- **Most frequent travel times** (month, day, hour)
- **Most popular stations** (start and end stations)
- **Most frequent trips** (combination of start and end stations)
- **Trip duration statistics** (total and average trip time)
- **User demographics** (user type, gender, birth year)

These insights can be used to identify trends and patterns in the bikeshare system, providing valuable information for decision-making or research.

### Files Used
The program requires CSV files containing data for each city. These files should be placed in the same directory as the script, or the file paths can be adjusted accordingly:

1. `chicago.csv`
2. `new_york_city.csv`
3. `washington.csv`

The CSV files must contain relevant data columns such as `Start Time`, `End Time`, `Trip Duration`, `Start Station`, `End Station`, `User Type`, `Gender`, and `Birth Year`.

### Example Usage:
python bikeshare.py

Select a city:
1. Chicago
2. New York City
3. Washington

Enter your choice (1, 2, or 3): 1

Select a month (January to June or 'all' for no filter):
1. January
2. February
3. March
...
Enter your choice (1, 2, 3, ..., or 'all'): January

Select a day of the week (Monday to Sunday or 'all' for no filter):
1. Monday
2. Tuesday
3. Wednesday
...
Enter your choice (1, 2, 3, ..., or 'all'): all

Displaying statistics for Chicago for the month of January:

- Most frequent travel times (month, day, hour)
- Most popular stations
- Most frequent trips
- Total and average trip duration
- User statistics (user type, gender, birth year)


### Credits
This project is inspired by and based on the Udacity Data Science program. Special thanks to **Udacity** for providing the course content and resources that helped shape the foundation of this project.

### Features ###
**City Selection:** Choose from three cities: Chicago, New York City, or Washington.
**Month Filter:** Filter data for a specific month (January to June) or no filter.
**Day Filter:** Filter data for a specific day of the week or no filter.
**Statistics Displayed:**
<ul>
<li>Most common travel times (month, day, and hour)</li>
<li>Most popular stations and most frequent trips</li>
<li>Total and average trip duration</li>
<li>User statistics (user type, gender, birth year)</li>
</ul>

- `pandas` – for data manipulation and analysis
- `numpy` – for numerical operations
- `time` – for handling time-related operations

### Requirements
To run this program, you will need the following Python libraries:

```bash
pip install pandas numpy 
