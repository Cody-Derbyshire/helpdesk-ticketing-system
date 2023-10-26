# Help Desk Ticketing System

The Help Desk Ticketing System is a simple Python application that allows you to manage and track help desk tickets from staff members within an organization. It provides a user-friendly graphical interface for creating new tickets, responding to tickets, and viewing ticket statistics.

## Features

- Create new help desk tickets with the following information:
  - Staff ID
  - Ticket creator name
  - Contact email
  - Description of the issue

- Automatic assignment of internal ticket numbers, starting from 2000.
- Respond to tickets and update their status.
- View and list all created tickets.
- Display ticket statistics, including the number of created, resolved, and open tickets.
- Reopen previously closed tickets.
- Save and load tickets to maintain data across sessions.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python)
- sv_ttk (for themed GUI)

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/Cody-Derbyshire/helpdesk-ticketing-system.git
   cd helpdesk-ticketing-system
   
   # OR
   
   gh repo clone Cody-Derbyshire/helpdesk-ticketing-system
   cd helpdesk-ticketing-system
   ```

## Run

Run with GUI
```bash
python gui.py
```

Run with CLI
```bash
python main.py
```

## Usage

- Open the application to access the Help Desk Ticketing System.
- Create new tickets by providing staff ID, creator name, contact email, and a description of the issue.
- Respond to tickets and update their status as resolved or reopened.
- View and list all created tickets in the main window.
- Click on a ticket in the list to view its details.
- Display ticket statistics to track the number of created, resolved, and open tickets.

### Enjoy!

Created by Cody Derbyshire - October 2023

