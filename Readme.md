# AI Resume Analyzer

## Project Structure

```text
AI-Resume-Analyzer/
├── backend/
│   ├── alembic/
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── analysis.py
│   │   │       │   ├── auth.py
│   │   │       │   └── resumes.py
│   │   │       └── router.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── analysis.py
│   │   │   ├── resume.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── analysis.py
│   │   │   ├── resume.py
│   │   │   └── user.py
│   │   └── services/
│   │       ├── ai_analyzer.py
│   │       ├── extractor.py
│   │       └── storage.py
│   ├── alembic.ini
│   ├── main.py
│   ├── pyproject.toml
│   ├── README.md
│   └── uv.lock
├── frontend/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── public/
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── eslint.config.mjs
│   ├── next-env.d.ts
│   ├── next.config.ts
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.mjs
│   ├── README.md
│   └── tsconfig.json
└── README.md
```
