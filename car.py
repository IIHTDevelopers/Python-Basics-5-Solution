# /car_inventory.py

import json

# Sample dataset with 5 cars
car_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 565000},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
    {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
]


# Function 1: Search cars by budget
def search_by_budget(inventory, max_price):
    filtered_cars = [car for car in inventory if car['price'] <= max_price]
    if filtered_cars:
        print(f"\nCars available under ${max_price}:")
        for car in filtered_cars:
            print(f"{car['make']} {car['model']} - ${car['price']}")
    else:
        print("\nNo cars found within this budget.")
    return filtered_cars

# Function 2: Save inventory to a file
def save_inventory(inventory, filename="car_inventory.json"):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)
    print("\nCar inventory saved successfully.")
    return filename

# Execute the functions
if __name__ == "__main__":

    search_by_budget(car_inventory, 25000)
    save_inventory(car_inventory)
