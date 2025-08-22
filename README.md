## Database Setup
This project uses **PostgreSQL** as the database. Follow the steps below to set it up:

# Switch to postgres user (Linux/MacOS)
sudo -i -u postgres
psql

# Inside psql
CREATE DATABASE gallery;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

# Replace DB Details
go to db_helpers/db_connection.py and replace the details

# Install Dependencies
Install Python 3.x Verison
Install Dependencies using : pip install -r requirements.txt

# Run Backend App using following Cmd
uvicorn gallery_backend_app.main:app --reload
