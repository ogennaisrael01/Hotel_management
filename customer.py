import uuid

from storage import save_guest, load_guest

guests = load_guest()
class Guest:
    def __init__(self):
        self.guest_id = str(uuid.uuid4())
        self.name = ""
        self.email = ""
        self.phone = ""
        self.address = ""
        self.assigned_room = None

    def to_dict(self):
        "serialize quest attributes to a dictionary"

        return {
            "GuestID": self.guest_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": int(self.phone),
            "Address": self.address,
            "Assigned_room": self.assigned_room
        }
    @staticmethod
    def validate_email(email):
        if ".com" not in email or  "@" not in email:
            raise ValueError("Invalid email address")
        
    @staticmethod   
    def validate_phone(phone): 
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number")


    def check_dublicate_guest(self, email):
        for guest in guests:
            if guest["Email"] == email: 
                raise ValueError("User already exist in our database")

    def add_guest(self, name, email, phone, address):
        
        Guest.validate_email(email)
        Guest.validate_phone(phone)
        guest = Guest()
        guest.check_dublicate_guest(email)

        guest.name = name
        guest.email = email
        guest.phone = phone
        guest.address = address

        guests.append(guest.to_dict())
        save_guest(guests)

    def view_guest(self):
        if not guests:
            return "No Guest"
        return guests
            

    def edit_guest(self,old_email, new_name, new_email, new_phone, new_address):
        Guest.validate_email(new_email)
        Guest.validate_phone(new_phone)

        for guest in guests:
            if guest["Email"] == old_email:
                guest["Name"] = new_name
                guest["Email"] = new_email
                guest["Phone"] = new_phone
                guest["Address"] = new_address

                save_guest(guests)
                return f"Guest with {old_email} updated successfully"
                
        return f"No user with {old_email}"
    
    def delete_guest(self, email):
        "Delete guests by email"

        for i, guest in enumerate(guests):
            if guest["Email"] == email:
                del guests[i]

                save_guest(guests)
                return f"{email} deleted from our database"
            
        return "Cant delete"