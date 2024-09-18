import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype = str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype = str)
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"]==self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"]==self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"]==self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
        pass
    
    def generate(self):
        content = f"""
                Thank you for your reservation
                Here are your booking data:
                Name: {self.customer_name}
                Hotel Name: {self.hotel_object.name}"""
        print(content)
class CreditCard:
    def __init__(self, card_num):
        self.card_num = card_num

    def validate(self, expiry, holder, cvc):
        data = {"number":self.card_num, "expiration":expiry, "holder":holder, "cvc":cvc}
        if data in df_cards:
            return True
        else:
            return False
        
class SecureCreditCard(CreditCard):
    def authenticate(self, password):
        true_pass = df_cards_security.loc[df_cards_security["number"]==self.number, "password"].squeeze()
        if true_pass == password:
            return True
        else:
            return False

if __name__ == "__main__":
    print(df)
    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id)
    if hotel.available():
        no = input("Enter your Credit Card Number: ")
        secure_credit_card = SecureCreditCard(no)
        expiry = input("Enter the Expiry Date: ")
        holder = input("Enter the Name of Card Holder: ")
        cvc = input("Enter the 3 digit CVC: ")
        if secure_credit_card.validate(expiry, holder, cvc):
            password = input("Please Enter your Credit Card Password: ")
            if secure_credit_card.authenticate(password):
                hotel.book()
                name = input("Enter your Name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                print(reservation_ticket.generate())
            else:
                print("Card authentication failed!")
        else:
            print("There was a problem with your payment!")
    else:
        print("Hotel is not free")