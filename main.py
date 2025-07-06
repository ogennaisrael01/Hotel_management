from rooms import Room
from storage import load_rooms
from bookings import Booking
from customer import Guest



def hotel_management_menu():
    print("" \
    "\n1. Room management" \
    "\n2. Booking management" \
    "\n3. Customer management" \
    "\n4, Exit")

def room_menu():
    print("" \
    "\n1. Add room" \
    "\n2. View all rooms" \
    "\n3. Edit room details" \
    "\n4. View avialable rooms" \
    "\n5. Delete rooms" \
    "\n6. Back to main menu")

def booking_menu ():
    print("" \
    "\n1. Book a room" \
    "\n2. Cancel booking" \
    "\n3. View all bookings" \
    "\n4. Back to main menu")

def customer_menu():
    print("" \
    "\n1. Add new customer" \
    "\n2. VIew all customers" \
    "\n3. Edit customer details" \
    "\n4. Delete customer" \
    "\n5. Back to main menu")

def room_management():
    room = Room()
    active = True
    while active:
        room_menu()

        option = int(input("Enter an option: "))

        match option:
            case 1:
                print("=== Add a room ===")
                try:
                    room_id = int(input("Enter the room number: ")).strip()
                    room_type = input("Enter the room type: ").strip().lower()
                    room_price = float(input("Enter the price: "))
                except Exception as e:
                    print(f"Error: {e}")
                room.add_room(room_id, room_type, room_price)
                add_more = input("Do you want to add another room (yes/no)? ").strip().lower()
                if add_more in ["yes" "y"]:
                    continue
                else:
                    print("Rooms saved")
            case 2:
                print("\n==== Available Rooms ====")
                rooms = room.view_rooms()
                for reservation in rooms:
                    status = "Available" if reservation.get("available", True) else "Occupied"

                    print(f"Room {reservation["RoomID"]} - {reservation["Type"]} - {status} - ${reservation["Price"]}")

            case 3:
                print("==== Edit room details ====")
                try:
                    room_id = int(input("Enter room ID to edit: "))
                    new_type = input("Enter the new type: ").strip().capitalize()
                    new_price = float(input("Enter the new price: "))

                except Exception as e:
                    print(f"Error {e}")

                print(room.edit_room(room_id, new_type, new_price))

            case 4:
                print("==== Available rooms ====")
                for room in room.view_available_rooms():
                
                    print(f"Room {room["RoomID"]} - {room["Type"]} - ${room["Price"]}")

            case 5:
                rooms = load_rooms()
                room_id = int(input("Enter the room id to delete: "))
                to_del = next((room for room in rooms if room["RoomID"] == room_id), None)
                prompt = input(f"Are you sure you want to delete this room? {to_del} (yes/no): ")
                if prompt == "no":
                    continue
                room.delete_room(room_id)
                print(f"Room {room_id} deleted")
            case 6:
                active = False

def booking_management():
    booking = Booking()
    active = True

    while True:
        booking_menu()

        option = int(input("Enter an option: "))
        match option:
            case 1:
                print("===== Book a room for a customer =====")
                try:
                    guest_id = input("Enter the guest id: ")
                    room_id = int(input("Enter the room id: "))
                    room_type = input("Enter the room type: ")
                    checkin = input("Enter the checkin date (YYYY-MM-DD): ")
                    checkout = input("Enter the check out date (YYYY-MM-DD): ")
                except Exception as e:
                    print(f"Error: {e}")

                print(booking.booking(guest_id, room_id, room_type, checkin, checkout)) 
            case 2:
                print("==== Cancel a booking ====") 

                print("\nEnter the booking ID")
                booking_id = int(input())
                print(booking.cancel_booking(booking_id))
            case 3:
                print("==== All booking =====")


                for booking in booking.view_bookings():
                    print(f"\n{booking}")
            case 4:
                active = False

def customer_management():
    guest = Guest()

    active = True
    while active:
        customer_menu()
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("==== Add a guest ====")

                try:
                    name  = input("Enter guest name: ")
                    email = input("Enter email: ")
                    phone = int(input("Enter phone number: "))
                    address = input("Enter user address: ")

                except Exception as e:
                    print(f"Error: {e}")

                guest.add_guest(name, email, phone, address)

                print("Guest saved")
            case 2:
                print("==== All Guest ====")
                for guest in guest.view_guest():
                    print(f"Guest ID: {guest['GuestID']}, Name: {guest['Name']}, Email: {guest['Email']}, Phone: {guest['Phone']}, Address: {guest['Address']}")
                                        
            case 3:
                print("Edit Guest Details")
                try:
                    old_email = input("Enter the old guest email: ")
                    new_name = input("Enter guest name: ")
                    new_email = input("Enter the new email: ")
                    new_phone = int(input("New phone number: "))
                    new_address = input("Guest address: ")
                except Exception as e:
                    print(f"Error  {e}")
                print(guest.edit_guest(old_email, new_name, new_email, new_phone, new_address))
            case 4:
                print("==== Delete guest =====")
                email = input("Enter email: ")
                print(guest.delete_guest(email)) 

            case 5:
                active = False        
                                                           

def main():
    while True:
        print("===== Hotel management system =====")

        exit_choice = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
        if exit_choice == "exit":
            print("Exiting the application...")
            break
        hotel_management_menu()

        choice = int(input("Select an option: "))

        match choice:
            case 1: 
                room_management()
            case 2:
                booking_management()
            case 3:
                customer_management()
            case 4:
                print( "Not included in our list of options" )
            
                

        
if __name__ == "__main__":
    main()
            