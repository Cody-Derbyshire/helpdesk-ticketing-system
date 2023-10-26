
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
from main import Ticket  # Import the Ticket class from main.py


class HelpDeskGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk Ticketing System")

        # Create a themed style
        self.style = ttk.Style()

        # Choose the 'sv_ttk' theme
        sv_ttk.set_theme("light")

        self.tickets = []  # Store ticket objects

        # Set the initial window size
        self.root.geometry("400x600")  # Width x Height

        new_ticket_labelframe = ttk.Label(root, text="New Ticket", font=("default", 14))

        # Create a LabelFrame for new ticket details
        new_ticket_frame = ttk.LabelFrame(root, borderwidth=10, labelwidget=new_ticket_labelframe)
        new_ticket_frame.pack(padx=10, pady=10, fill="x", expand=True)

        # Create entry widgets for ticket details within the LabelFrame
        ttk.Label(new_ticket_frame, text="Staff ID:").grid(row=0, column=0, sticky="w")
        self.staff_id_entry = ttk.Entry(new_ticket_frame, width=30)
        self.staff_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(new_ticket_frame, text="Ticket Creator Name:").grid(row=1, column=0, sticky="w")
        self.creator_name_entry = ttk.Entry(new_ticket_frame, width=30)
        self.creator_name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(new_ticket_frame, text="Contact Email:").grid(row=2, column=0, sticky="w")
        self.contact_email_entry = ttk.Entry(new_ticket_frame, width=30)
        self.contact_email_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(new_ticket_frame, text="Description of the Issue:").grid(row=3, column=0, sticky="w")
        self.description_entry = ttk.Entry(new_ticket_frame, width=30)
        self.description_entry.grid(row=3, column=1, padx=5, pady=5)

        # Create a button to add a new ticket with centered text
        new_ticket_button = ttk.Button(new_ticket_frame, text="Create New Ticket", command=self.create_new_ticket,
                                       width=30)
        new_ticket_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Create a listbox to display tickets
        self.ticket_listbox = tk.Listbox(root, width=70)
        self.ticket_listbox.pack(fill=tk.BOTH, expand=True)  # Use the full width
        self.ticket_listbox.pack()

        # Load existing tickets from a file
        self.load_tickets()

        # Bind a click event to the listbox to view details
        self.ticket_listbox.bind("<<ListboxSelect>>", self.view_selected_ticket)

        # Create a button to display ticket statistics

        stats_button = ttk.Button(root, text="Display Ticket Statistics", command=self.display_statistics, width=30)
        stats_button.pack()

        # Register the window close event handler
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_tickets(self):
        try:
            with open('tickets.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        staff_id, creator_name, contact_email, description, response, status = data
                        ticket = Ticket(staff_id, creator_name, contact_email, description)
                        ticket.response = response
                        ticket.status = status
                        self.tickets.append(ticket)
                        self.update_ticket_listbox()
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            pass

    def save_tickets(self):
        with open('tickets.txt', 'w') as file:
            for ticket in self.tickets:
                file.write(
                    f"{ticket.staff_id},{ticket.creator_name},{ticket.contact_email},{ticket.description},{ticket.response},{ticket.status}\n")

    def create_new_ticket(self):
        # Get user input from the entry widgets
        staff_id = self.staff_id_entry.get()
        creator_name = self.creator_name_entry.get()
        contact_email = self.contact_email_entry.get()
        description = self.description_entry.get()

        # Create a new ticket object and append it to self.tickets
        new_ticket = Ticket(staff_id, creator_name, contact_email, description)
        self.tickets.append(new_ticket)
        self.update_ticket_listbox()

        # Save the ticket to the file
        self.save_tickets()

    def display_statistics(self):
        # Create a new window to display statistics
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Ticket Statistics")
        stats_window.geometry("200x100")  # Width x Height

        # Calculate ticket statistics
        total_tickets = len(self.tickets)
        resolved_tickets = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets

        # Create labels to display the statistics
        ttk.Label(stats_window, text=f"Total Tickets: {total_tickets}").pack()
        ttk.Label(stats_window, text=f"Resolved Tickets: {resolved_tickets}").pack()
        ttk.Label(stats_window, text=f"Open Tickets: {open_tickets}").pack()

    def update_ticket_listbox(self):
        self.ticket_listbox.delete(0, tk.END)
        for ticket in self.tickets:
            self.ticket_listbox.insert(tk.END, f"Ticket: {ticket.ticket_number}, User: {ticket.creator_name}, Status: {ticket.status}")

    def view_selected_ticket(self, event):
        selected_index = self.ticket_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]  # Get the first selected item
            selected_ticket = self.tickets[int(selected_index)]
            self.display_ticket_details(selected_ticket)

    def display_ticket_details(self, ticket):
        # Create a new window to display the selected ticket details
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Ticket Details: {ticket.ticket_number}")
        details_window.geometry("400x200")

        # Display ticket information in the new window
        ttk.Label(details_window, text=f"Ticket Number: {ticket.ticket_number}").pack()
        ttk.Label(details_window, text=f"Ticket Creator: {ticket.creator_name}").pack()
        ttk.Label(details_window, text=f"Staff ID: {ticket.staff_id}").pack()
        ttk.Label(details_window, text=f"Email Address: {ticket.contact_email}").pack()
        ttk.Label(details_window, text=f"Description: {ticket.description}").pack()
        ttk.Label(details_window, text=f"Response: {ticket.response}").pack()
        ttk.Label(details_window, text=f"Ticket Status: {ticket.status}").pack()

        respond_button = ttk.Button(details_window, text="Respond", command=self.open_response_window)
        respond_button.pack()
        # Create a "Delete" button
        delete_button = ttk.Button(details_window, text="Delete Ticket",
                                   command=lambda: self.delete_ticket(ticket, details_window))
        delete_button.pack()

    def delete_ticket(self, ticket, details_window):
        # Display a "Yes/No/Cancel" messagebox to confirm deletion
        confirmation = tk.messagebox.askyesnocancel("Delete Ticket",
                                                         "Are you sure you want to delete this ticket?")

        if confirmation is None:
            # User clicked "Cancel"
            return
        elif confirmation:
            # User clicked "Yes", proceed with deletion
            if ticket in self.tickets:
                self.tickets.remove(ticket)
                self.update_ticket_listbox()
                details_window.destroy()
        else:
            # User clicked "No", do nothing
            pass

    def open_response_window(self):
        # Create a response window using Toplevel
        response_window = tk.Toplevel(self.root)
        response_window.title("Respond to Ticket")

        # Add a Text widget or Entry for entering the response
        response_entry = ttk.Entry(response_window, width=40)
        response_entry.pack()

        # Add a "Submit" button to save the response and close the window
        submit_button = ttk.Button(response_window, text="Submit",
                                  command=lambda: self.submit_response(response_entry.get(), response_window))
        submit_button.pack()

    def submit_response(self, response, response_window):
        # Handle response submission, update the ticket
        selected_index = self.ticket_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            ticket = self.tickets[selected_index]
            ticket.respond(response)
            self.update_ticket_listbox()

        # Close the response window
        response_window.destroy()

    def on_closing(self):
        # Handle the window close event
        unsaved_changes = self.check_unsaved_changes()

        if unsaved_changes:
            response = messagebox.askyesnocancel("Unsaved Changes",
                                                         "You have unsaved changes. Do you want to save them before quitting?")
            if response is None:
                # User clicked "Cancel" in the messagebox, do nothing
                return
            elif response:
                self.save_tickets()
        self.root.destroy()

    def check_unsaved_changes(self):
        # Check if there are unsaved changes

        # Create a string representation of the current list of tickets
        current_tickets_str = "\n".join(str(ticket) for ticket in self.tickets)

        # Read the previous state of the list from the file
        try:
            with open('tickets.txt', 'r') as file:
                previous_tickets_str = file.read()
        except FileNotFoundError:
            previous_tickets_str = ""

        # Compare the current and previous states to check for changes
        return current_tickets_str != previous_tickets_str


def main():
    root = tk.Tk()
    # Create a themed style
    style = ttk.Style()

    # Choose the 'sv_ttk' theme
    style.theme_use('vista')
    app = HelpDeskGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()
