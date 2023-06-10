# Car-System

## Installation

### Change directory to src/

```bash
cd src/
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install fastapi unicorn
```

## How to run

```bash
waitress-serve --port=8080 app:app
```

### References

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)

- [Guide 1](https://flask.palletsprojects.com/en/2.3.x/deploying/waitress/)
