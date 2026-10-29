# Blood Donor Management System

A Python-based blood donor management project using MySQL for data storage and Streamlit for a simple web interface.

## Project Status

A learning project that demonstrates database operations and a basic interface for managing blood donor records.

## Current Features

- Add donor records with name, blood group, phone number, city, and last donation date.
- View donor records in a table.
- Retrieve an individual donor by ID through the management class.
- Update donor details through the management class.
- Delete donor records through the management class.

## Technologies Used

- Python
- MySQL
- `mysql-connector-python`
- Streamlit

## Project Files

- `bd_views.py` — donor database operations, including create, read, update, and delete methods.
- `gui.py` — Streamlit interface for adding and viewing donor records.
- `task.py` — a separate student-record insertion exercise used for database practice.

## Setup

1. Install Python and MySQL.
2. Create the required database and tables.
3. Install the dependencies:

```bash
pip install mysql-connector-python streamlit
```

4. Configure database credentials securely using environment variables.
5. Run the Streamlit application:

```bash
streamlit run gui.py
```

## Security Note

This is a learning project, not a production-ready blood donation platform. Do not use real donor data without appropriate privacy and security safeguards.

## Future Improvements

- Add input validation and clearer error messages.
- Add a search feature for donor records.
- Improve database connection handling.
- Separate the unrelated student database exercise from the donor-management project.
- Improve security and data privacy before any real-world use.
