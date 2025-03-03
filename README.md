# AI HR Assistant

An intelligent HR assistant that helps analyze and match CVs/resumes with job descriptions using AI/ML techniques.

## Overview

This tool streamlines the recruitment process by automatically analyzing candidate CVs against job descriptions to identify the best matches. It uses natural language processing and machine learning to understand both the job requirements and candidate qualifications.

## Features

- CV/Resume analysis
- Job description parsing
- Intelligent matching algorithms
- Qualification scoring
- Skills assessment

## Project Structure

- `ai_hr_assistant.py` - Main application script
- `cv.md` - CV/Resume content for analysis
- `job_description.md` - Job posting requirements
- `requirements.txt` - Python package dependencies
- `.env` - Environment variables and configuration

## Setup

1. Clone the repository:
```bash
git clone https://github.com/[username]/ai-hr-assistant.git
cd ai-hr-assistant
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
- Copy `.env.example` to `.env` (if applicable)
- Update the variables in `.env` with your settings

## Usage

Run the main script:

```bash
python ai_hr_assistant.py
```

The assistant will analyze the provided CV against the job description and generate a matching report.

## Dependencies

See `requirements.txt` for a complete list of Python package dependencies.

## License

[Add your chosen license]

## Contributing

[Add contribution guidelines if applicable]
