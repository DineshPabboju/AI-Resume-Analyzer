
fastapi-backend/
├── app/
│   ├── api/                    # API Routers & Controllers
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py     # Authentication (JWT login, register)
│   │   │   │   ├── resumes.py  # File upload & retrieval
│   │   │   │   └── analysis.py # AI resume analysis & job matching
│   │   │   └── router.py       # Aggregated v1 API router
│   ├── core/                   # Central Application Config
│   │   ├── config.py           # Pydantic Settings (.env handling)
│   │   ├── database.py         # Async SQLAlchemy engine & session maker
│   │   └── security.py         # Password hashing & JWT token handling
│   ├── models/                 # SQLAlchemy DB Entities
│   │   ├── user.py
│   │   ├── resume.py
│   │   └── analysis.py
│   ├── schemas/                # Pydantic Schemas (API DTOs & LLM Outputs)
│   │   ├── user.py
│   │   ├── resume.py
│   │   └── analysis.py         # Structured AI output schemas
│   ├── services/               # Core Business & AI Logic
│   │   ├── ai_analyzer.py      # LLM prompt orchestration & parsing
│   │   ├── extractor.py        # PDF/DOCX text parsing
│   │   └── storage.py          # Local/S3 file management
│   └── main.py                 # FastAPI application instantiation & middleware
├── alembic/                    # Database migration files
├── tests/                      # Pytest unit & integration tests
├── .env.example                # Sample environment variables
├── Dockerfile                  # Multi-stage container build
├── pyproject.toml              # Dependencies (using Poetry or uv)
└── README.md

