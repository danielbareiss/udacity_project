import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'all': 0, 'january': 1, 'febuary': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
DAY_DATA = {'all': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York or Washington? ").lower()
        if city in ('chicago', 'new york', 'washington'):
            break
        print('Sorry, we do not have this city in our data, please enter a valid city!')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to filter by month from the available months (January to June) or see all? ")
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        print('Sorry, we do not have the details for this month, please enter a valid month!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day would you like to see? For every day, type in: all, else the name of the day! ").lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        print('Sorry, we do not have this day in our data, please enter a valid day!')


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
    # Load data
    city_csv = CITY_DATA.get(city)
    df = pd.read_csv(city_csv)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Day']=df['Start Time'].dt.dayofweek
    df['Hour']=df['Start Time'].dt.hour

    if month != 'all':
        df = df[(df['Month'] == MONTH_DATA.get(month))]

    if day != 'all':
        df = df[(df['Day'] == DAY_DATA.get(day))]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['Month'].mode()[0]
    print('The most common month is: {}'.format(popular_month))

    # display the most common day of week
    popular_day = df['Day'].mode()[0]
    print('The most common day is: {}'.format(popular_day))

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('The most common hour is: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('The most used Start Station is: {}'.format(most_used_start_station))

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('The most used End Station is: {}'.format(most_used_end_station))

    # display most frequent combination of start station and end station trip
    df['adding_start_stop'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_combination = df['adding_start_stop'].mode()[0]
    print('The most used combination is: {}'.format(most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_time = df['Trip Duration'].sum()
    days = int(sum_time / 60 / 60 / 24 % 365)
    hours = int(sum_time / 60 / 60 % 24)
    minutes = int(sum_time / 60 % 60)
    seconds = int(sum_time % 60)
    print('The sum of the travel time is {} days, {} hours, {} minutes and {} seconds'.format(days, hours, minutes, seconds))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    days = int(mean_time / 60 / 60 / 24 % 365)
    hours = int(mean_time / 60 / 60 % 24)
    minutes = int(mean_time / 60 % 60)
    seconds = int(mean_time % 60)
    print('The mean time of the travel is {} days, {} hours, {} minutes and {} seconds'.format(days, hours, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('For this overview, we have the following amount of user types:\n{}'.format(user_type_count))

  # Display counts of gender
    if 'Gender' not in df:
        print('Sorry for this filter we do not have informations about this')
    else:
        print('For this overview, we have the following Gender overview:\n{}'.format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Sorry for this filter we do not have informations about this')
    else:
        print('You see here the overview to the year of birth in different categories')
        print('The earliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
"""Asks user if 5 rows of data should be displayed. As long as the user answers 'yes', 5 additional rows of data are shown. Loop is ended once users says 'no'. """

    view_data = input('\nWould you like to see 5 lines of data for the chosen filters? Enter yes or no.\n')
    start_loc = 0
    while view_data == 'yes':
        if 'Gender' and 'Birth Year' not in df:
            print(df[['Start Time', 'End Time', 'Start Station', 'End Station', 'User Type']].iloc[start_loc:(5+start_loc)])

        else:
            print(df[['Start Time', 'End Time', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']].iloc[start_loc:(5+start_loc)])
        start_loc += 5
        view_data = input('\nWould you like to see 5 more lines of data for the chosen filters? Enter yes or no.\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
