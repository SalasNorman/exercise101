# Flask Phonebook Application

This is a simple Phonebook application built using Flask, providing CRUD (Create, Read, Update, Delete) functionality. The application uses SQLite as its database.
NOTE: this project use command for ubuntu wsl

## Features

- Add new contacts to the phonebook.
- View a list of all contacts.
- Update existing contact details.
- Delete contacts from the phonebook.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLite**: A lightweight, file-based database.
- **HTML/CSS**: For the front-end interface.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SalasNorman/exercise101.git
   cd exercise101\flask-phonebook
   ```

2. **Create a Virtual Environment**:
   Note: python must already installed.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**:
   ```bash
   python app.py
   ```

7. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
flask-phonebook/
├── templates/
│   ├── add.html
│   └── edit.html
│   └── index.html
├── app.py  
├── requirements.txt
├── README.md
```

## License

This project is licensed under the MIT License.
