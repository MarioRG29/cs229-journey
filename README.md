# 🧠 ML & DL Journey — CS229 (Stanford)

Este repositorio documenta mi recorrido personal aprendiendo *Machine Learning* y *Deep Learning*, comenzando con **CS229** (Stanford).

## 📚 Estructura

- `notes/`: apuntes **propios**, resúmenes y derivaciones. *No* subo PDFs ni notas oficiales; los enlazo en `references/`.
- `psets_theory/`: resoluciones **propias** de los problem sets teóricos.
- `problem-sets/`: tareas/programming assignments y notebooks asociados.
- `notebooks/`: notebooks exploratorios adicionales.
- `utils/`: helpers reutilizables.
- `data/`, `outputs/`, `models/`: carpetas ignoradas para datasets/resultados/modelos.
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

## 🗂️ Datos
No subo datasets. Colócalos en `data/` o `practical/*/data/` y documenta su origen en el `README.md` del ejercicio. Para versionar binarios grandes usa Git LFS o DVC si lo necesitas.


**Curso base:** https://cs229.stanford.edu/
