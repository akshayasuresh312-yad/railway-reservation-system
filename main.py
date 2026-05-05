import random

# Step 4: Design the System
total_seats = 50
booked_tickets = []  # List to store dictionary data

def main():
    global total_seats
    
    while True:
        # Step 5: Create Menu
        print("\n--- Railway Reservation System ---")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        # Step 6: Implement Features
        if choice == '1':
            print(f"\nAvailable Seats: {total_seats}")

        elif choice == '2':
            if total_seats > 0:
                name = input("Enter passenger name: ")
                age = input("Enter passenger age: ")
                
                # Generate a random Booking ID
                booking_id = random.randint(1000, 9999)
                seat_no = 51 - total_seats
                
                ticket = {
                    "name": name,
                    "age": age,
                    "id": booking_id,
                    "seat": seat_no
                }
                
                booked_tickets.append(ticket)
                total_seats -= 1
                print(f"\nSuccess! Ticket booked. Your Booking ID is: {booking_id}")
            else:
                print("\nSorry, no seats available!")

        elif choice == '3':
            search_id = int(input("Enter your Booking ID: "))
            found = False
            for ticket in booked_tickets:
                if ticket["id"] == search_id:
                    print("\n--- Ticket Details ---")
                    print(f"Name: {ticket['name']}\nAge: {ticket['age']}\nSeat: {ticket['seat']}")
                    found = True
                    break
            if not found:
                print("\nInvalid Booking ID.")

        elif choice == '4':
            cancel_id = int(input("Enter Booking ID to cancel: "))
            for ticket in booked_tickets:
                if ticket["id"] == cancel_id:
                    booked_tickets.remove(ticket)
                    total_seats += 1
                    print("\nTicket cancelled successfully.")
                    break
            else:
                print("\nBooking ID not found.")

        elif choice == '5':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
