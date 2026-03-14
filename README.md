# Mawaed El-Rahman Website  

A web-based platform built using the Django framework (Python) that helps users find and manage Ramadan charity tables (Mawaed El-Rahman) on an interactive map.


## Features

### Authentication System
- **Secure Login/Logout:** Users must have an account to view tables and manage (update or delete) their tables.
- **User-Specific Data:** Only the table owner can update or delete their tables.


### Interactive Map

* **Google Maps Integration:** Display Mawaed El-Rahman locations on an interactive map.
* **Location Markers:** Each table appears as a marker on the map.
* **Table Details:** Clicking a marker shows the table name and description.


### Table Management

* **Add New Table:** Users can add new Mawaed El-Rahman with location information.
* **View Details:** Each table has its own page displaying full information.
* **Edit Table:** Update table details easily.
* **Delete Table:** Remove tables when needed.


## Technologies Used 
* ***Backend:*** Python & Django Framework.
* ***Frontend:*** HTML5, CSS3, and Bootstrap for responsive design.
* ***Maps API:*** Google Maps JavaScript API
* ***Database:*** PostgreSQL.



## How to Run
1. Clone the repository to your local machine.
2. Ensure Python and Django are installed.
3. Install required packages `pip install -r requirements.txt`.
4. Run `py manage.py migrate` to set up the database.
5. Start the server using `py manage.py runserver` .
6. Open http://127.0.0.1:8000/ in your browser.



## Created By
[**Maryam Al Menshawy**](https://github.com/MariamAlMenshawy)
