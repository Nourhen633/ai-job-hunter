# AI Job Hunter 🎯

**An AI-powered job search assistant built with Python, FastAPI, PostgreSQL, and AI.**

AI Job Hunter is a personal project designed to make the job-search process smarter, more organized, and more efficient.

The application aims to help users manage job opportunities, analyze job descriptions, identify skill matches, generate tailored application documents, and track their applications in one place.

> 🚧 **Project Status: In Development**
>
> The project is currently in its early development stage. Database setup and the initial backend implementation are underway. AI-powered analysis and the user interface are planned features.

---

## 🎯 Project Goals

Finding a suitable job involves more than simply browsing job portals. Candidates need to understand job requirements, evaluate their qualifications, adapt their CVs, and manage multiple applications.

AI Job Hunter aims to simplify this process by providing:

- Centralized job offer management.
- AI-powered job description analysis.
- Skills comparison and matching scores.
- Personalized CV and cover letter generation.
- Application status tracking.

## ✨ Planned Features

### 1. Job Offer Management
- Add and save job opportunities.
- Store job descriptions, company information, and source links.
- Organize opportunities in one place.

### 2. AI-Powered Job Analysis
- Extract skills and qualifications from job descriptions.
- Identify required and preferred competencies.
- Compare job requirements with the user's profile.
- Calculate an explainable skills-matching score.

### 3. Application Document Generation
- Generate tailored CV content.
- Create personalized cover letters.
- Adapt application documents to individual job requirements.
- Ensure that generated content reflects the user's actual qualifications and experience.

### 4. Application Tracking
- Track application statuses.
- Store notes and important dates.
- Monitor application progress.

### 5. Dashboard
- Display saved job opportunities.
- Visualize skills matches.
- Monitor application statistics.
- Provide an overview of the job-search process.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend API |
| PostgreSQL | Relational database |
| SQLAlchemy | Database interaction |
| Pydantic | Data validation |
| Streamlit | Planned user interface |
| AI / LLM | Planned job analysis and document generation |
| Git & GitHub | Version control |

## 🏗️ Project Structure

```text
ai-job-hunter/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── dashboard/
│
├── documents/
│
├── data/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: The structure may evolve as development progresses.*

## 🗄️ Database Design

The initial PostgreSQL database contains three main tables:

**Users**
- User information
- Email address
- Skills

**Job Offers**
- Job title
- Company
- Location
- Job description
- Source URL

**Applications**
- User reference
- Job offer reference
- Application status
- Notes
- Application date

The database uses primary keys and foreign keys to maintain relationships between users, job offers, and applications.

## 🚀 Getting Started

### Prerequisites

Make sure you have installed:

- Python 3.10+
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ai-job-hunter.git
cd ai-job-hunter
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_job_hunter
DB_USER=postgres
DB_PASSWORD=your_password
```

Replace the example password with your local PostgreSQL password.

**Important:** Never commit your `.env` file or expose database credentials.

### 5. Start the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

*The setup instructions describe the intended local development workflow; some functionality is still under development.*

## 🗺️ Development Roadmap

- [x] Create project structure and Python environment.
- [x] Set up PostgreSQL database.
- [x] Create initial database tables and relationships.
- [x] Test Python–PostgreSQL connectivity.
- [ ] Complete FastAPI backend setup.
- [ ] Integrate database operations into API endpoints.
- [ ] Implement job offer management.
- [ ] Develop AI-powered job analysis.
- [ ] Implement skills-matching functionality.
- [ ] Generate tailored CVs and cover letters.
- [ ] Implement application tracking.
- [ ] Build the Streamlit dashboard.
- [ ] Add automated tests and improve security.
- [ ] Prepare the first complete release.

## 🔒 Privacy & Security

This project is designed to handle personal information such as CVs, skills, and application details.

Privacy and security considerations include:

- Keeping credentials in environment variables.
- Excluding private documents from version control.
- Protecting user data.
- Reviewing AI-generated content before using it.
- Requiring explicit user approval before submitting applications.

## 🎓 Learning Objectives

This project is also an opportunity to develop practical software engineering skills, including:

- Backend development and REST API design.
- Relational database design and SQL.
- Python application architecture.
- AI integration and prompt engineering.
- Data validation and error handling.
- Version control and software testing.

## 👩‍💻 Author

Developed as a personal learning and portfolio project.

**AI Job Hunter — Making the job search smarter, one application at a time.**
