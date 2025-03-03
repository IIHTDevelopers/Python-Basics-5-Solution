# Smart Waste Management System

# Preset waste data (Location, Waste Type, Weight in kg)
waste_data = [
    ("Zone A", "Organic", 120),
    ("Zone B", "Plastic", 80),
    ("Zone C", "Electronic", 45),
    ("Zone D", "Metal", 60),
    ("Zone E", "Organic", 95)
]


# Function 1: Calculate total waste by type
def calculate_total_waste_by_type(data):
    waste_summary = {}
    for location, waste_type, weight in data:
        if waste_type in waste_summary:
            waste_summary[waste_type] += weight
        else:
            waste_summary[waste_type] = weight

    return waste_summary  # Return the summary instead of printing it


# Function 2: Identify unique waste zones
def unique_waste_zones(data):
    zones = {location for location, _, _ in data}
    return zones  # Return the unique zones instead of printing them


# Function 3: Find heaviest waste location
def find_heaviest_location(data):
    heaviest_zone = max(data, key=lambda x: x[2])
    return (heaviest_zone[0], heaviest_zone[2])  # Return the heaviest zone and its weight


# Main Execution
print("Smart Waste Management System")
print("Total Waste by Type:", calculate_total_waste_by_type(waste_data))
print("Unique Waste Zones:", unique_waste_zones(waste_data))
print("Heaviest Waste Location:", find_heaviest_location(waste_data))
