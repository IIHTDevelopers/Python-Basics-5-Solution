import unittest

import numpy as np
import pandas as pd

# Preset data for the Railway Reservation System
seat_numbers = np.array([101, 102, 103, 104, 105])  # Seat numbers
ticket_prices = np.array([250, 300, 400, 350, 500])  # Ticket prices for each seat
availability = np.array([True, False, True, False, True])  # Availability status (True means available)
passenger_names = ["John", "Alice", "Bob", "Emma", "David"]  # Reserved passenger names

# Create a DataFrame to manage reservations
df = pd.DataFrame({
    'Seat Number': seat_numbers,
    'Passenger Name': passenger_names,
    'Ticket Price': ticket_prices,
    'Availability': availability
})

# Function 1: Find the total waiting list (count passengers with unavailable seats)

# Function 2: Find the highest ticket price
def highest_ticket_price(df):
    highest_price = df['Ticket Price'].max()
    seat = df[df['Ticket Price'] == highest_price]['Seat Number'].values[0]
    return highest_price, seat

# Function 3: Find the number of available seats
def available_seats(df):
    available_seat_count = len(df[df['Availability'] == True])
    return available_seat_count

# Display initial reservation data
print("Railway Reservation System - Initial Status:")
print("-------------------------------------------")
print(df)
print("-------------------------------------------")

# Perform operations and return values

highest_price, seat = highest_ticket_price(df)  # Find highest ticket price
available_seat_count = available_seats(df)  # Find available seats


print(f"Highest ticket price is {highest_price} at Seat {seat}")
print(f"Number of available seats: {available_seat_count}")

