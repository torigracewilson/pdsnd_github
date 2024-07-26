import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Task 1 get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("\nPlease select the city you would like to filter by: new york city, chicago, or washington.\n")
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry, that is an invalid input. Please try again and only choose from new york city, chicago, or washington.")
        continue
      else:
        break

    # Task 2 get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nPlease select the month you would like to filter by: january, february, march, april, may, june or type 'all' if you do not have a preference.\n")
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, that is an invalid input. Please try again and only choose from january, february, march, april, may, june or type 'all' if you do not have a preference.")
        continue
      else:
        break

    # Task 3 get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nPlease select the day you would like to filter by: sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all' if you do not have a preference.\n")
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, that is an invalid input. Please try again and only choose from sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all' if you do not have a preference.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load file
    df = pd.read_csv(CITY_DATA[city])

    #convert column format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month f into new column called month
    #df['month'] = df['Start Time'].dt.month

    #filter by month if needed

    #if month != 'all':
        # use the index of the months list to get the int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        #month = months.index(month) + 1

        # filter by month to create the new dataframe
        #df = df[df['month'] == month]

    # extract day into new column 
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by day of week if applicable
    #if day != 'all':
        # filter by day of week to create the new dataframe
        #df = df[df['day_of_week'] == day.title()]
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def fiv_row_disp(df):
    """
    display rows of data depending on user answer "load 5 rows"

    Args:
         df - filitered city dataframe that returned from load_data function

    """
    row_display = input("\nDo you want to see the first five raws of data? Yes or No:\n").lower()
    if  row_display == 'yes':
        r = 0
        while True:
            print(df.iloc[r: r+5])
            r += 5
            more_row = input("\nDo you want to see more? Yes or No:\n").lower()
            if more_row != 'yes':
                break
            


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Task 4 display the most common month
    print("The most common month is: ", df['month'].mode()[0])

    # Task 5 display the most common day of week
    print("The most common day is: ", df['day_of_week'].mode()[0])

    # Task 6 display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Task 7 display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].mode()[0])

    # Task 8 display most commonly used end station
    print("The most common end station is: ", df['End Station'].mode()[0])

    # Task 9 display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Task 10 display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours is: ", total_duration)

    # Task 11 display mean travel time
    mean_duration = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time in hours is: ", mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Task 12 Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe count of each user type: \n",user_types)

    # Task 13 Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # Task 14 Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        fiv_row_disp(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  main()
