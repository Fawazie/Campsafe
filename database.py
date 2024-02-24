from main import gun_exist


# Simplified Building Map (Example)


def get_location():
    # Retrieve location details from user inputs during initial setup
    building = building_entry.get()
    floor = floor_entry.get()
    room = room_entry.get()


building_map = {
    "floor1": {
        "room1": ["hallway", "room2"],
        "hallway": ["room1", "stairwellA"],
        "room2": ...,
    },
    "floor2": {...},
}

exits = ["stairwellA", "exitB"]  # List your exits

# Simulating a Shooter Location
shooter_location = {"floor": 2, "x": 50, "y": 25}  # Example coordinates

# List representing your connected panic screens (you'll likely have a way to manage these)
panic_screens = [screen_1, screen_2, ...]

# Trigger Function (Your hackathon 'button press' would call this)

if gun_exist:

    def trigger_alert():
        for screen in panic_screens:
            screen.update_shooter_location(shooter_location)


break


def calculate_safest_route(shooter_location, building_map, exits):
    current_floor = shooter_location["floor"]
    safe_exits = [exit for exit in exits if exit not in building_map[current_floor]]

    if safe_exits:
        route_suggestion = f"Head towards {safe_exits[0]}"
    else:
        route_suggestion = "Seek immediate cover"

    return route_suggestion
