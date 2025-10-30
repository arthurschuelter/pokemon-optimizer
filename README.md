# pokemon-optimizer
A Python tool that optimizes a Pokémon team based on type coverage and resistances. This project focuses on type matchups and type diversity to build balanced framework for building Pokémon teams.

## Features

- Builds a framework, with the best 6 type combination. 
- Analyzes type effectiveness across until Generation V.

### Future Improvements
- [ ] Analyze type effectiveness across all generations.
- [ ] Consider dual-type Pokémon.

## Setup

### First-Time Setup

Create a virtual environment:
```bash
python3.12 -m venv env
```

### Running the Optimizer

1. Activate the virtual environment:
```bash
   source env/bin/activate
```

2. Install dependencies:
```bash
   pip3 install -r requirements.txt
```

3. Run the optimizer:
```bash
   python3 src/main.py
```

4. When finished, deactivate the environment:
```bash
   deactivate
```

## Development

### Updating Dependencies

After installing new packages, update the requirements file:
```bash
pip3 freeze > requirements.txt
```

## Project Structure
```
pokemon-optimizer/
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```
