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

## Templating Logic Explained

The Python script leverages a simple templating engine to transform Markdown templates into complete log entries. Here’s how it works in detail:

1. **Scanning for Placeholders**  
   The template files (ending with `.md.template`) contain placeholders in the format `$VARIABLE`. The script uses a regular expression (`r'\$([A-Z0-9_]+)\b'`) to scan the template text and extract all unique placeholder names (e.g., `DATE`, `TITLE`).
  - **Example:** In a template, occurrences of `$DATE` and `$TITLE` are identified for later replacement.

2. **Populating Variables**  
   Once the placeholders are identified, the script builds a dictionary of variable values:
  - **Auto-Populated Values:**  
    Variables like `$DATE`, `$DATE_TIME`, and `$EPOCH` are automatically set using helper functions (e.g., `get_current_date()`).
  - **Pre-Defined Values:**  
    Special variables such as `$LOGBOOK_NAME` (derived from the template’s filename) and an initial `$LOGBOOK_ENTRY_FILENAME` are set.
  - **User Input:**  
    For any placeholder that isn’t auto-generated, the script prompts the user for a value. It also asks for a log entry title, which is used to refine the filename by sanitizing the title and appending a timestamp.

3. **Review and Edit Loop**  
   Before finalizing, the script displays all collected variable values and offers an opportunity to edit any of them. This interactive step ensures that every placeholder is assigned the correct and desired value.

4. **Substitution Process**  
   The script uses a custom replacement function within a regular expression substitution. Every occurrence of `$VARIABLE` in the template text is replaced with its corresponding value from the dictionary:
  - **Replacement Function:**  
    A helper function (`variable_replacer`) looks up each placeholder in the dictionary. If a value exists, it replaces the placeholder; otherwise, it leaves the original text intact.

5. **Generating the Final Log Entry**  
   After all placeholders are replaced, the final content is written to a new log file within a designated logbook directory (e.g., `logbooks/<LOGBOOK_NAME>`). The new file’s name is generated using the sanitized title and a timestamp, ensuring it is both unique and descriptive.

This templating process automates the conversion of raw templates into fully customized log entries, ensuring consistency, reducing manual errors, and allowing you to focus on capturing your insights and experiences. Feel free to modify 
or add your own templates.

Happy logging!