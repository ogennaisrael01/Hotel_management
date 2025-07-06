import uuid
from storage import load_rooms, load_guest, load_bookings, save_bookings, save_guest, save_rooms
from enum import Enum
import datetime
guests = load_guest()
rooms = load_rooms()

bookings = load_bookings()
class BookingStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Booking:
    def __init__(self):
        self.booking_id = str(uuid.uuid4())
        self.guest = None
        self.rooms_id = None
        self.check_in = None
        self.check_out = None
        self.room_type = None
        self.status = BookingStatus.PENDING.value

    @staticmethod
    def parse_date(date):
        return datetime.datetime.strptime(date, "%Y-%m-%d")
    
    def is_available(self, room_id):
        for room in rooms:
            if room_id == room["RoomID"] and room["Status"]:
                return (True)

    def to_dict(self):
        return {
            "BookingID": self.booking_id,
            "GuestID": self.guest,
            "RoomID": self.rooms_id,
            "CheckIn": self.check_in,
            "CheckOut": self.check_out,
            "RoomType": self.room_type,
            "Status": self.status
        }
    def booking(self, guestID, roomId, room_type, checkedIn, checked_out):
        if not self.is_available(roomId):
            return "No room available"
        if not any(guest["GuestID"] == guestID for guest in guests):
            return "No guest with this ID"
        if not any(room["Type"] == room_type for room in rooms):
            print(f"{room_type} is not available")
            return
        if Booking.parse_date(checkedIn) >= Booking.parse_date(checked_out):
            return "Check in date must be before the check out date"
        
        booking = Booking()
        booking.guest = guestID
        booking.rooms_id = roomId
        booking.check_in = str(booking.parse_date(checkedIn))
        booking.check_out = str(booking.parse_date(checked_out))
        booking.room_type = room_type
        booking.status = BookingStatus.CONFIRMED.value

        bookings.append(booking.to_dict())
        save_bookings(bookings)

        # Assign room to guest
        for guest in guests:
            if guestID == guest["GuestID"]:
                guest["Assigned_room"] = roomId
                save_guest(guests)
                break

        # status will be false for booked rooms
        for room in rooms :
            if  roomId == room["RoomID"]:
                room["Status"] = False
                save_rooms(rooms)
                break

    def cancel_booking(self, booking_id):
        cancelled_at = datetime.datetime.now()
        if not any(booking["BookingID"] == booking_id for booking in bookings):
            return "Booking not found"
        # Update booking status to cancelled
        for booking in bookings:
            if booking["BookingID"] == booking_id:
                booking["Status"] = BookingStatus.CANCELLED.value
                booking["CancelledAt"] = cancelled_at.strftime("%Y-%m-%d %H:%M:%S")
                save_bookings(bookings)
                return "Booking cancelled"
            
    def view_bookings(self):
        if not bookings:
            return "No Bookings"
        return bookings

    def view_booking_by_guest(self, guest_id):
        guest_bookings = [booking for booking in bookings if booking["GuestID"] == guest_id]
        if not guest_bookings:
            return "No bookings found for this guest"
        for booking in guest_bookings:
            print(booking)

    def delete_booking(self, booking_id):
        for i, booking in enumerate(bookings):
            if booking["BookingID"] == booking_id:
                del bookings[i]
                save_bookings(bookings)
                return "Booking deleted successfully"
        return "Booking not found"




