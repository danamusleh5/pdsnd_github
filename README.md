### Date created
January 26, 2025
### Project Title
Bikeshare Data Analysis

### Description
This Python program analyzes bikeshare data for different cities in the United States. It allows the user to explore data from Chicago, New York City, and Washington. The program enables users to filter data by month and day of the week and provides various statistics about the bikeshare system, including:

- **Most frequent travel times**
- **Most popular stations and trips**
- **Trip duration statistics**
- **User demographics** (e.g., user type, gender, birth year)


## Files used
The program requires CSV files for the three cities:

1. `chicago.csv`
2. `new_york_city.csv`
3. `washington.csv`

These files should contain the necessary data for the analysis. Ensure the files are placed in the same directory as the script, or adjust the file paths accordingly in your code.

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

### Example of Running the Program ###

![image.png](attachment:caa062aa-8d88-4304-b0fc-bab50bbe2c2e.png)
![image.png](attachment:50ff63ab-f025-4c3d-baa2-60683542e98e.png)
![image.png](attachment:4cea6d74-2ca0-4ab8-9c2c-7b5da3e7f04e.png)

## Requirements
The program requires the following Python libraries:
- `pandas` – for data manipulation and analysis
- `numpy` – for numerical operations
- `time` – for handling time-related operations
- `calendar` – for handling month and weekday names

You can install the required libraries using:

```bash
pip install pandas numpy





