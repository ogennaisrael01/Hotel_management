
import json

ROOMS_FILE = "rooms.json"
# save rooms
def save_rooms(room):
    try:
        with open(ROOMS_FILE, "w") as file:
            json.dump(room, file, indent=4)
    except json.JSONDecodeError:
        print("Error saving rooms")
# Load roams
def load_rooms():
    try:
        with open(ROOMS_FILE, "r") as file:
            rooms = json.load(file)
            return rooms
    except json.JSONDecodeError:
        return []
    

# save guest

GUESTS_FILE = "guest.json"

def save_guest(guest):
    try:
        with open(GUESTS_FILE, "w") as file:
            json.dump(guest, file, indent=4)
    except json.JSONDecodeError:
        print("Error saving guests")

# Load guest
def load_guest():
    try:
        with open(GUESTS_FILE, "r") as file:
            guest = json.load(file)
            return guest
    except json.JSONDecodeError:
        return []
    


BOOKINGS_FILE = "bookings.json"

def save_bookings(bookings):
    try:
        with open(BOOKINGS_FILE, "w") as file:
            json.dump(bookings, file, indent=4)
    except json.JSONDecodeError:
        print("Error saving guests")

# Load guest
def load_bookings():
    try:
        with open(BOOKINGS_FILE, "r") as file:
            bookings = json.load(file)
            return bookings
    except json.JSONDecodeError:
        return []