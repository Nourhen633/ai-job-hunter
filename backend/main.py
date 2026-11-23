
"""
Main entry point for the AI Job Hunter backend.

This module creates the FastAPI application.
FastAPI will allow our frontend to communicate
with the Python backend through HTTP requests.
"""

# Import FastAPI to create our backend application.
from fastapi import FastAPI


# Create the FastAPI application instance.
app = FastAPI(
    title="AI Job Hunter API",
    description="Backend API for our personal AI Job Hunter.",
    version="1.0.0"
)


# Define a simple welcome endpoint.
@app.get("/")
def home():
    """
    Return a welcome message when someone visits the API root.
    """
    return {
        "message": "Welcome to AI Job Hunter!",
        "status": "Backend is running"
    }
