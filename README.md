# 🧠 ML & DL Journey — CS229 (Stanford)

Este repositorio documenta mi recorrido personal aprendiendo *Machine Learning* y *Deep Learning*, comenzando con **CS229** (Stanford).

## 📚 Estructura

- `notes/`: apuntes **propios**, resúmenes y derivaciones. *No* subo PDFs ni notas oficiales; los enlazo en `references/`.
- `problem-sets/`: tareas/programming assignments y notebooks asociados. Aqui estan mis soluciones.
- `notebooks/`: notebooks exploratorios adicionales.
- `utils/`: helpers reutilizables.
- `references/`: enlaces a materiales oficiales.

## ⚙️ Entorno (pip)

Usa **pip** con un entorno virtual aislado:

```bash
python -m venv .venv
# Linux/Mac:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
pre-commit install
```

Actualizar dependencias a lo instalado actualmente:
```bash
pip freeze > requirements.txt
```

## 🧼 Notebooks limpios
El pre-commit limpia los outputs de los notebooks (nbstripout) y ejecuta Black/Ruff.




**Curso base:** https://cs229.stanford.edu/
