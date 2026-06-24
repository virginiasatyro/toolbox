# Toolbox

Toolbox is a desktop utility app built with Python and PySide6. It collects small everyday tools in one Qt interface, grouped by category.

## Features

### Text

- Word counter
- Lorem ipsum generator
- Base64 encode/decode
- Hashtag converter

### Network

- Domain to IP lookup with country and ISP details
- DNS record lookup

### Image

- Resize images
- Rotate images
- Flip images
- Convert PNG to ICO

### Calculator and Converter

- Percentage calculator
- Age calculator
- Temperature converter
- Data size converter

## Requirements

- Python 3.12+
- PySide6
- dnspython
- Pillow
- pytest, for running tests

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run The App

From the project root:

```bash
python -m src.main
```

On Windows, if you use a virtual environment or conda environment, activate it first.

## Run Tests

Run the full test suite:

```bash
pytest tests
```

Run a single test file:

```bash
pytest tests/test_base64_logic.py
```

The project includes a `pytest.ini` file so tests can import modules from `src`.

## Project Structure

```text
src/
  core/          Tool base class and registry
  tools/         Individual tool logic and Qt widgets
  ui/            Main window and navigation
tests/           Unit tests for tool logic
```

Each tool is split into two parts:

- `*_logic.py` contains testable business logic.
- `*_tool.py` contains the PySide6 widget used by the desktop app.

## Adding A Tool

1. Add the logic module under the matching `src/tools/<category>/` folder.
2. Add a Qt tool widget that extends `Tool`.
3. Register the tool in `src/main.py`.
4. Add focused tests under `tests/`.

## License

This project is licensed under the terms in [LICENSE](LICENSE).
