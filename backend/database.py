
"""
Database connection configuration for AI Job Hunter.

This module:
1. Loads database credentials from the project's .env file.
2. Creates a SQLAlchemy engine.
3. Provides a function to test the PostgreSQL connection.
"""

# Import os to read environment variables.
import os

# Import Path to work with file and folder paths.
from pathlib import Path

# Import load_dotenv to load variables from the .env file.
from dotenv import load_dotenv

# Import create_engine to create the SQLAlchemy database engine.
# Import text to execute a simple SQL statement.
from sqlalchemy import create_engine, text

# Import URL to construct the database connection URL safely.
from sqlalchemy.engine import URL

# Import SQLAlchemyError to handle database-related errors.
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import DeclarativeBase

# --------------------------------------------------
# 1. FIND THE PROJECT ROOT
# --------------------------------------------------

# database.py is inside backend/.
# Its parent directory is the main ai-job-hunter folder.
#.resolve() — converts it into an absolute, resolved path
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

# Load database credentials from the .env file.
# This keeps sensitive information out of our Python code.
load_dotenv(PROJECT_ROOT / ".env")


# --------------------------------------------------
# 3. READ DATABASE CONFIGURATION
# --------------------------------------------------

# Read the PostgreSQL host.
DB_HOST = os.getenv("DB_HOST", "localhost")

# Read the PostgreSQL port and convert it into an integer.
DB_PORT = int(os.getenv("DB_PORT", "5432"))

# Read the database name.
DB_NAME = os.getenv("DB_NAME")

# Read the PostgreSQL username.
DB_USER = os.getenv("DB_USER")

# Read the PostgreSQL password.
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Check whether all required settings are available.
if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise ValueError(
        "Missing database settings. "
        "Please check DB_NAME, DB_USER, and DB_PASSWORD in your .env file."
    )


# --------------------------------------------------
# 4. CREATE THE DATABASE URL
# --------------------------------------------------

# URL.create safely builds the connection URL.
# It also handles special characters in the password.
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)


# --------------------------------------------------
# 5. CREATE THE SQLALCHEMY ENGINE
# --------------------------------------------------

# The engine manages connections between Python and PostgreSQL.
# pool_pre_ping checks connections before reusing them.
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

# Base class for all database models.
# Every model will inherit from this class.
"""base is empty: we use it so that the classes in models enherits from it then 
they belong to the same family """
class Base(DeclarativeBase):
    pass

# --------------------------------------------------
# 6. TEST THE DATABASE CONNECTION
# --------------------------------------------------

def test_connection():
    """
    Test whether Python can communicate with PostgreSQL.

    The function opens a database connection and executes
    SELECT 1, a simple SQL statement used for testing.
    """

    try:
        # Open a connection to the PostgreSQL database.
        with engine.connect() as connection:

            # Execute a simple SQL query.
            result = connection.execute(text("SELECT 1"))

            # Read the result returned by PostgreSQL.
            value = result.scalar_one()

            # Confirm that the query returned the expected value.
            if value == 1:
                print("Successfully connected to PostgreSQL!")
                print(f"Database: {DB_NAME}")

    except SQLAlchemyError as error:
        # Display a helpful message if the connection fails.
        print("Database connection failed.")
        print(f"Error: {error}")


# --------------------------------------------------
# 7. RUN THE CONNECTION TEST
# --------------------------------------------------

# This condition ensures the test runs only when
# database.py is executed directly.
if __name__ == "__main__":
    test_connection()