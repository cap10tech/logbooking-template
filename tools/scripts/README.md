# Python Environment Setup for Logbook Entry Generator

This repository contains a Python script to generate new logbook entries based on markdown templates. This guide explains how to set up a Python virtual environment (venv) and configure IntelliJ IDEA for proper Python interpreter support.

## Prerequisites

- **Python 3:** Ensure you have Python 3.8 or later installed.
- **IntelliJ IDEA with Python Plugin:** Make sure the Python plugin is installed in IntelliJ.

## Setting Up the Virtual Environment

1. **Open a Terminal in the Repository Root**

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

  - **macOS/Linux/Windows gitbash:**
    ```bash
    source ./venv/Scripts/activate
    ```
  - **Windows (Command Prompt):**
    ```cmd
    .\venv\Scripts\activate
    ```
  - **Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

4. **Upgrade pip (Optional)**

   ```bash
   pip install --upgrade pip
   ```

5. **Install Dependencies (if needed)**

   This script uses only standard Python libraries. If you add external packages later, list them in a `requirements.txt` file and install with:

   ```bash
   pip install -r requirements.txt
   ```

## Configuring IntelliJ IDEA

1. **Open IntelliJ IDEA.**

2. **Configure the Python Interpreter for the Module:**

  - Go to `File` > `Project Structure` > `Modules`.
  - Select your Python module.
  - Click on "Add" (or the gear icon) to add a new interpreter.
  - Choose "Add Local Interpreter" and select the virtual environment you created:
    - For macOS/Linux: `venv/bin/python`
    - For Windows: `venv\Scripts\python.exe`
  - Apply the changes.

3. **Verify Interpreter Settings:**

   Ensure that the Python interpreter is correctly set for your module to avoid the “No Python interpreter configured for the module” warning.

## Running the Script

1. **Activate the Virtual Environment (if not already active):**

  - macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
  - Windows:
    ```cmd
    venv\Scripts\activate
    ```

2. **Run the Script:**

   From the repository root, run:
   ```bash
   ./tools/scripts/generate-new-logbook-entry.py
   ```
   Or on Windows:
   ```cmd
   python tools\scripts\generate-new-logbook-entry.py
   ```

3. **Follow the On-Screen Prompts:**

   The script will display available markdown templates, prompt for variable values, and generate a new logbook entry in the appropriate directory.

## Repository Structure Overview

```
.
|-- README.md
|-- examples
|   `-- postgresql-install.md
|-- guides
|   |-- git-repositories.md
|   `-- markdown-logbooking.md
|-- logbook.md
|-- logbooks
|   |-- learning-skills
|   |-- pull-requests
|   |-- research
|   `-- troubleshooting-session
`-- tools
    |-- jetbrains
    |   |-- README.md
    |   |-- cap10-tech-logbooking-templates.xml
    |   `-- logbooking-templates.xml
    |-- scripts
    |   |-- generate-new-logbook-entry.py    <-- This file
    |   `-- logbooking-templates            <-- Directory containing templates:
    |       |-- learning-skills.md.template
    |       |-- pull-requests.md.template
    |       |-- research.md.template
    |       `-- troubleshooting-session.md.template
    `-- vscode
        |-- README.md
        |-- cap10-tech-logbooking-template.json
        `-- logbooking-templates.json
```

## Additional Notes

- **IntelliJ Configuration:** Make sure the virtual environment is activated in IntelliJ to prevent interpreter warnings.
- **Modifying Dependencies:** If your project grows to require third-party packages, update your `requirements.txt` accordingly.
- **Script Shebang:** The script uses `#!/usr/bin/env python3` at the top, so it should run with the correct Python interpreter once the environment is configured.

Happy logging!
