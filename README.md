ByteKart Inventory Management System

ByteKart is a Python-based inventory management system designed to help small businesses efficiently track inventory, generate sales reports, and streamline day-to-day operations. The system features a user-friendly interface, robust authentication, and scalable data storage.

Table of Contents
Project Overview
Features
Technologies Used
Installation
Usage
File Structure
Future Enhancements
Contributors

Project Overview

ByteKart is a lightweight yet powerful inventory management tool tailored for small businesses. It leverages a client-server architecture to support multiple functions, including inventory tracking, sales reporting, and user authentication.

Features

Python-based Client-Server Architecture for fast and scalable operations.
Tkinter GUI for a user-friendly interface.
User Authentication to ensure secure access.
SQLite Database for local data storage and management.
Tracking Inventory: Easily add, update, and delete inventory items.
Generating Sales Reports: Comprehensive reporting of sales trends and best-selling items.
Product Barcode Scanning for quick data entry.
Mobile App Support for managing inventory on the go (future).
AI-powered Sales Forecasting to predict sales trends.
Cloud Integration for secure and centralized data storage (future).
Loyalty Program Integration to engage customers.

Technologies Used
Programming Language: Python
GUI Library: Tkinter
Database: SQLite
Version Control: Git
Other Tools: Matplotlib for generating visualizations like burndown charts.
Installation
Prerequisites
Python 3.8 or higher installed.
Git installed on your system.

Virtual Environment for Python dependencies.



Steps
Clone the repository:

git clone https://github.com/airbik-codes/ByteKart.git
cd ByteKart

Set up a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run the application:

python src/main.py

Usage
Running the System
Launch the application by running src/main.py.
Log in with your credentials (set up in the database).
Use the intuitive GUI to manage inventory, generate reports, and view data.

Sample Commands
Adding Items: Use the "Add Item" form to input product details.
Generating Reports: Click the "Generate Report" button to view sales data.

File Structure


ByteKart/
│
├── env/                        # Virtual environment directory (not tracked in Git)
├── src/                        # Source code
│   ├── main.py                 # Main application entry point
│   ├── database.py             # SQLite database setup and functions
│   ├── gui.py                  # GUI implementation using Tkinter
│   └── utils/                  # Utility scripts
├── inventory.db                # SQLite database file
├── requirements.txt            # Python dependencies
├── burndown_chart.png          # Burndown chart for sprint tracking
├── README.md                   # Project documentation
├── ReadMe ByteKart Inventory Management System.pdf
├── Test Plan for ByteKart Python Inventory Management System.pdf
└── project run instructions.txt


Future Enhancements

Integrating AI-based sales forecasting.
Supporting a mobile app for managing inventory remotely.
Adding cloud-based storage for centralized data.
Expanding loyalty program support.

License
This project is licensed under the MIT License. See the LICENSE file for details.
