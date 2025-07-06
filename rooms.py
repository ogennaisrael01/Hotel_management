import uuid
from  storage import save_rooms, load_rooms

rooms = load_rooms()
class Room:
    def __init__(self):
        self.roomID = None
        self.type = ""
        self.is_available = True
        self.price = None
    
    def to_dict(self):
        "Serilialize rook attributes to a diictionary"

        return {
            "RoomID": int(self.roomID),
            "Type": self.type,
            "Status": self.is_available,
            "Price": float(self.price)
        }

    def add_room(self, roomID, type, price):
        """ Add rooms"""
        room = Room()
        room.roomID = roomID
        room.type = type
        room.price = price
        # check for dublicate room number
        for reservation in rooms:
            if reservation["RoomID"] == roomID:
                return "Room number already exists"

        rooms.append(room.to_dict())
        # save the rooms to the file
        save_rooms(rooms)
    
    def view_rooms(self):
        if not rooms:
            return "No rooms found"
        return rooms
           
    
    def view_available_rooms(self):
    
        available_rooms = [room for room in rooms if room["Status"]]

        if not available_rooms:
            return "No room available at the moment, check back later"
        
        return available_rooms

    def edit_room(self, roomID, new_type, new_price):
        "Edit room by the room number"
        for room in  rooms:
            if room["RoomID"] == roomID:
                room["Type"] = new_type
                room["Price"] = new_price
                save_rooms(rooms)

                return f"[!] Room {roomID}edited successfully"
        return "[!] Room not found"
    
    def delete_room(self, room_ID):
        "Delete a room by their id"

        for i, room in enumerate(rooms):
            if room["RoomID"] == room_ID:
                del rooms[i]
                save_rooms(rooms)
                return 

