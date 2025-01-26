import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Please choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from chicago, new york city, or washington.")

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month = input("Enter the month (january to june) or 'all' to apply no filter: ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please choose a valid month or 'all'.")

    # Get user input for day of the week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter the day of the week or 'all' to apply no filter: ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please choose a valid day or 'all'.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    # Load data for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    if df.empty:
        print("\nNo data available for the specified filters. Please try again.\n")
        return None

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month.capitalize()}")

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of the week: {common_day.capitalize()}")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {start_station}")

    # Display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {end_station}")

    # Display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most frequent combination of start and end stations: {combination[0]} -> {combination[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_time} seconds ({total_time / 3600:.2f} hours)")

    # Display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_time:.2f} seconds ({mean_time / 60:.2f} minutes)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df:
        user_types = df['User Type'].value_counts()
        print("Counts of user types:")
        print(user_types)
    else:
        print("User type data is not available for this city.")

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender data is not available for this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print("\nBirth Year Stats:")
        print(f"Earliest birth year: {earliest}")
        print(f"Most recent birth year: {most_recent}")
        print(f"Most common birth year: {most_common}")
    else:
        print("\nBirth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    """Displays raw data in chunks of 5 rows based on user input."""
    row_index = 0
    while True:
        user_input = input("\nWould you like to see 5 rows of raw data? Enter 'yes' or 'no': ").lower()

        if user_input == 'yes':
            print(df.iloc[row_index:row_index + 5])
            row_index += 5
            if row_index >= len(df):
                print("\nNo more data to display.")
                break
        elif user_input == 'no':
            print("\nEnding data display.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df is None:
            continue

        # Call the display_data function to show raw data if the user wants
        display_data(df)

        # Call other analysis functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
