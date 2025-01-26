## Bikeshare Data Analysis ##
### Overview ###
This Python program analyzes bikeshare data for different cities in the United States.
It allows the user to explore data from Chicago, New York City, and Washington.
The program enables users to filter data by month and day of the week and provides various statistics about the bikeshare system, including:

<ul>
<li>Most frequent travel times</li>
<li>Most popular stations and trips</li>
<li>Trip duration statistics</li>
<li>User demographics (e.g., user type, gender, birth year)</li>
</ul>

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

### Requirements ###
Before running the program, should make sure having the following:

Python 3.x
Pandas library (pip install pandas)
Numpy library (pip install numpy)

### Files ###
The program requires CSV files for the three cities:

<ol>
<li>chicago.csv</li>
<li>new_york_city.csv</li>
<li>washington.csv</li>
</ol>
These files should contain the necessary data for the analysis. 
And should make sure the files are placed in the same directory as the script or adjust the file paths accordingly.

### How to Run ###
<ol>
<li>Clone or download the repository.</li>
<li>Ensure you have the required dependencies (pandas, numpy).</li>
<li>Place the relevant city CSV files in the same directory as the script.</li>
<li>Run the program by executing the following command in your terminal:</li>
python bikeshare.py
<li>Follow the prompts to select a city, month, and day for analysis.</li>
<li>View the output statistics.</li>
</ol>

### Example of Running the Program ###

![image.png](attachment:caa062aa-8d88-4304-b0fc-bab50bbe2c2e.png)
![image.png](attachment:50ff63ab-f025-4c3d-baa2-60683542e98e.png)
![image.png](attachment:4cea6d74-2ca0-4ab8-9c2c-7b5da3e7f04e.png)

### License ###
This project is open source and available under the MIT License.
