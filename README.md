# 🧠 ML & DL Journey — CS229 (Stanford)

This repository documents my personal journey learning **Machine Learning** and **Deep Learning**, starting with **CS229 (Stanford)**.


## 📚 Structure

- `notes/`: course notes.  
- `extra-notes/`: additional notes from the course.  
- `problem-sets/`: homework/programming assignments and associated notebooks. Here you’ll find my solutions.  
- `problem-sets-solutions/`: official solutions to the problem sets.  
- `utils/`: reusable helpers.  

## ⚙️ Entorno (pip)

Use **pip** with an isolated virtual environment:

```bash
python -m venv .venv
# Linux/Mac:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
pre-commit install
```

Update dependencies to match the current environment:
```bash
pip freeze > requirements.txt
```

## 🧼 Clean notebooks
The pre-commit hook cleans notebook outputs (nbstripout) and enforces formatting with Black and Ruff.




**Course:** All lecture notes, slides and assignments for https://cs229.stanford.edu/ course by Stanford University.
The videos of all lectures are available [on YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU).
