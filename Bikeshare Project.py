#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    flag = True 

    while flag == True:
        city = input('what city are you intersted in? please type one of these three (chicago, new york city, washington)\n').lower().strip()
        if city in CITY_DATA:
            flag = False
        else:
            print()
            print('Please make sure you entered the right input!')

    # TO DO: get user input for month (all, january, february, ... , june)
    print('\n'*2)
    flag = True 
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while flag == True:
        month = input('what month are you intersted in? please type in a month between january and june or all (all, january, february, ... ,                       june)\n').lower().strip()
        if month in months or month == 'all':
            flag = False
        else:
            print()
            print('Please make sure you entered the right input!')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n'*2)
    flag = True 
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    while flag == True:
        day = input('what day are you intersted in? please type in a day or all (all, monday, tuesday, ... sunday)\n').lower().strip()
        if day in days or day == 'all':
            flag = False
        else:
            print()
            print('Please make sure you entered the right input!')


    print('-'*40)
    return city, month, day

def five_rows(df):
    
   return(df.head())



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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = 1 + months.index(month)
        df = df[df['month'] == month]
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('popular month is ',popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('popular day is ',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('popular hour is ',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('popular start station is',popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('popular end station is',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_rout = (df['Start Station'] + ',' + df['End Station']).mode()[0]
    print('popular rout is ',popular_rout)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_traveled = df['Trip Duration'].sum()
    print('The total time traveled is', total_time_traveled)


    # TO DO: display mean travel time
    mean_time_traveled = df['Trip Duration'].mean()
    print('The mean of the total time traveled', mean_time_traveled)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_each_user_type = df['User Type'].value_counts()
    print('the number of each user type:\n',count_each_user_type)
    


    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_each_gender = df['Gender'].value_counts()
        print('the number of each gender:\n',count_each_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('earliest year is',earliest_year)
        recent_year = df['Birth Year'].max()
        print('most recent year is', recent_year)
        common_year = df['Birth Year'].mode()
        print('most repeated year is', common_year)


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
        
        viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.\n").lower().strip()
        if viewData == "yes":
            row = 0
            while True:
                print(df.iloc [row: row+5])
                row += 5
                viewData = input('would you like to see more? (yes or no)\n').lower().strip()
                if viewData != 'yes':
                    break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


    
#while True:
 #   viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.\n").lower().strip()
  #  if viewData == "Yes":
   #     row = 0
    #    print(.....dataframe from row 0 to 5)
     #   row += 5
   # if viewData = 'No':
    #    break
#x = input('would you like to take a glance at the data? (yes or no)\n').lower().strip()
 #       if x == 'yes':
 #           print(five_rows(df))

