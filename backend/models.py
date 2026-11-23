"""
Database models for AI Job Hunter.

This module defines the structure of our PostgreSQL tables:
1. User
2. JobOffer
3. Application

Each Python class represents one database table.
"""

from datetime import datetime, timezone

# Import SQLAlchemy tools for defining columns and relationships.
from sqlalchemy import String, Text, DateTime, ForeignKey

# Import tools for defining typed columns and relationships.
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Import our shared Base class.
from backend.database import Base


# ==================================================
# 1. USER MODEL
# ==================================================

class User(Base):
    """
    Represents a user of AI Job Hunter.

    Stores the user's basic profile information and skills.
    """

    # Name of the PostgreSQL table.
    __tablename__ = "users"

    # Unique identifier for each user.
    id: Mapped[int] = mapped_column(primary_key=True)

    # User's full name.
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)

    # User's email address. Each email must be unique.
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    # Skills stored as text for our initial MVP.
    skills: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Optional path to the user's CV.
    cv_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # Date and time when the user record was created.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # One user can have multiple applications.
    applications: Mapped[list["Application"]] = relationship(
        back_populates="user"
    )


# ==================================================
# 2. JOB OFFER MODEL
# ==================================================

class JobOffer(Base):
    """
    Represents a job opportunity collected by AI Job Hunter.

    Stores the job title, company, description and source.
    """

    __tablename__ = "job_offers"

    # Unique identifier for each job offer.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Job title, for example: Working Student Python Developer.
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    # Company offering the position.
    company: Mapped[str] = mapped_column(String(255), nullable=False)

    # Job location, for example: Darmstadt.
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # Full job description.
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Original link to the job advertisement.
    source_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    # Date and time when we saved the job offer.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # One job offer can be associated with multiple applications.
    applications: Mapped[list["Application"]] = relationship(
        back_populates="job_offer"
    )


# ==================================================
# 3. APPLICATION MODEL
# ==================================================

class Application(Base):
    """
    Represents an application submitted by a user.

    Connects a user with a job offer and tracks the
    application's status and submission date.
    """

    __tablename__ = "applications"

    # Unique identifier for each application.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Foreign key referencing the users table.
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    # Foreign key referencing the job_offers table.
    job_offer_id: Mapped[int] = mapped_column(
        ForeignKey("job_offers.id"),
        nullable=False
    )

    # Current application status.
    # Examples: saved, applied, interview, rejected, accepted.
    status: Mapped[str] = mapped_column(
        String(50),
        default="saved",
        nullable=False
    )

    # Optional notes about the application.
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Date and time when the application record was created.
    applied_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relationship back to the user.
    user: Mapped["User"] = relationship(
        back_populates="applications"
    )

    # Relationship back to the job offer.
    job_offer: Mapped["JobOffer"] = relationship(
        back_populates="applications"
    )