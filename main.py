class Ticket:
    counter = 2000
    tickets_created = 0
    tickets_resolved = 0
    tickets_to_solve = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        Ticket.counter += 1
        self.ticket_number = Ticket.counter
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets_created += 1
        if "Password Change" in self.description:
            self.resolve_password_change()
        else:
            Ticket.tickets_to_solve += 1  # Only increase Tickets To Solve for non-password change tickets

    def resolve_password_change(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = "New password generated ->" + new_password
        self.status = "Closed"
        Ticket.tickets_resolved += 1

    def respond(self, response):
        self.response = response
        if self.status != "Closed":
            self.status = "Closed"
            Ticket.tickets_resolved += 1

    def reopen(self):
        if self.status == "Closed":
            self.status = "Reopened"
            Ticket.tickets_resolved -= 1

    @staticmethod
    def print_ticket_statistics():
        print("Displaying Ticket Statistics")
        print(f"Tickets Created: {Ticket.tickets_created}")
        print(f"Tickets Resolved: {Ticket.tickets_resolved}")
        print(f"Tickets To Solve: {Ticket.tickets_created - Ticket.tickets_resolved}\n")

    def display_ticket(self):
        print("Printing Tickets:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}\n")

class Main:
    def __init__(self):
        self.tickets = []

    def run(self):
        # Append the three initial tickets from the brief
        ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
        ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a video camera to conduct webinars")
        ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password Change")
        self.tickets.extend([ticket1, ticket2, ticket3])

        while True:
            print("Options:")
            print("1. Create a new ticket")
            print("2. Respond to a ticket")
            print("3. Reopen a ticket")
            print("4. List Tickets")
            print("5. Display ticket statistics")
            print("6. Exit")

            choice = input("Select an option (1/2/3/4/5/6): ")

            if choice == "1":
                staff_id = input("Enter Staff ID: ")
                creator_name = input("Enter Ticket Creator Name: ")
                contact_email = input("Enter Contact Email: ")
                description = input("Enter Description of the Issue: ")
                new_ticket = Ticket(staff_id, creator_name, contact_email, description)
                self.tickets.append(new_ticket)
                print("Ticket created successfully!\n")

            elif choice == "2":
                ticket_number = int(input("Enter Ticket Number to Respond: "))
                response = input("Enter Response: ")
                for ticket in self.tickets:
                    if ticket.ticket_number == ticket_number:
                        ticket.respond(response)
                        print("Response added successfully!\n")
                        break
                else:
                    print("Ticket not found. Please enter a valid ticket number.\n")

            elif choice == "3":
                ticket_number = int(input("Enter Ticket Number to Reopen: "))
                for ticket in self.tickets:
                    if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                        ticket.reopen()
                        print("Ticket reopened successfully!\n")
                        break
                else:
                    print("Ticket not found or cannot be reopened. Please enter a valid ticket number.\n")

            elif choice == "4":
                for ticket in self.tickets:
                    ticket.display_ticket()
                print("All tickets listed successfully!\n")

            elif choice == "5":
                Ticket.print_ticket_statistics()

            elif choice == "6":
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please select a valid option.\n")


if __name__ == "__main__":
    main = Main()
    main.run()
