
# ScrapedBooks

Utilisez les bases de Python pour l'analyse de marché.

OpenClassRooms

## Installation de l'environement virtuel

Cree un environement virtuel.

```bash
python -m venv <environement name>
```

Pour activer l'environement.

```bash
# Linux
source env/bin/activate

# Windos PowerShell
cd env/Scripts
./Activate.ps1
```

Pour quitter l'environement.

```bash
# Linux
deactivate
```

## Installation des dependances

Pour installer des dependances.
```bash
pip install <dep name>
```

Cree un fichier requirements.txt avec no dependances.
```bash
pip freeze > requirements.txt
```

Pour install les dependances de pui notre fichier requirements.txt
```bash
pip install -r requirements.txt
```

## Demo

Pour executer le script.
```bash
python main.py
```
