name: Python workflow

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        # This is the version of the action for setting up Python, not the Python version.
        uses: actions/setup-python@v5
        with:
          # Semantic version range syntax or exact version of a Python version
          python-version: '3.x'
          # Optional - x64 or x86 architecture, defaults to x64
          architecture: 'x64'
      - name: Display Python version
        run: python -c "import sys; print(sys.version)"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
      - name: Print the working directory
        run: |
          pwd
      - name: Execute python script # run file
        run: |
          python python/print_n_numbers.py
