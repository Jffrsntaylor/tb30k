# Warhammer Companion App

This project provides a desktop companion for **Horus Heresy 2nd Edition** and **Warhammer 40,000 5th Edition**. It includes an army-list builder, in-game reference, fuzzy rule search, and data editor.

## Setup

Requires Python 3.12. Install in editable mode:

```bash
pip install -e .
```

## Running

Launch the application with:

```bash
python -m companion
```

## Data Editing

Choose **Edit → Data Files…** from the menu to modify the built-in JSON files. The editor validates against `data/schema.json`.

Army lists are saved to the `lists/` folder as JSON.
