#!/usr/bin/env python3
"""
generate-new-logbook-entry.py

This script will:
  - Scan the "tools/scripts/logbooking-templates" directory for markdown template files.
  - Allow the user to select a template (which also determines the logbook type).
  - Parse the template for $VARIABLE occurrences.
  - Auto-fill variables ($DATE, $DATE_TIME, $LOGBOOK_ENTRY_FILENAME, $EPOCH) and prompt the user for any others.
  - Display all entered variables with the option to edit them.
  - Replace the variables in the template and generate a new log file under "logbooks/<LOGBOOK_NAME>".
  - Output the final file content and location, then wait for the user to press Enter before exiting.

Assumed Repository Structure:
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
    |   `-- logbooking-templates            <-- Template directory to scan:
    |       |-- learning-skills.md.template
    |       |-- pull-requests.md.template
    |       |-- research.md.template
    |       `-- troubleshooting-session.md.template
    `-- vscode
        |-- README.md
        |-- cap10-tech-logbooking-template.json
        `-- logbooking-templates.json
"""

import os
import sys
import re
import datetime
import time

# Define directories relative to this script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "logbooking-templates")

# Functions to auto-generate variable values.
def get_current_date():
    return datetime.date.today().strftime("%Y-%m-%d")

def get_current_date_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_epoch():
    return str(int(time.time()))

def get_filename_timestamp():
    # Replace colons with hyphens for filesystem compatibility.
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Auto-handled variable names.
AUTO_VARIABLES = {
    "DATE": get_current_date,
    "DATE_TIME": get_current_date_time,
    "EPOCH": get_current_epoch,
}

def scan_template_variables(template_text):
    """
    Scan the template text for occurrences of $VARIABLE.
    Returns a sorted list of unique variable names (without the $).
    """
    vars_found = re.findall(r'\$([A-Z0-9_]+)\b', template_text)
    return sorted(set(vars_found))

def prompt_for_variable(var_name):
    """
    Prompt the user for a value for a given variable.
    """
    return input(f"Enter a value for ${var_name}: ").strip()

def display_variables(variables):
    """
    Display all variable names and their current values with an index.
    """
    print("\nCurrent Variables:")
    for idx, (key, value) in enumerate(variables.items(), start=1):
        print(f"  {idx}. {key} = {value}")

def main():
    print("=== New Logbook Entry Generator ===\n")

    # List available template files in TEMPLATE_DIR ending with .md.template.
    try:
        template_files = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith(".md.template")]
    except FileNotFoundError:
        print(f"Template directory not found: {TEMPLATE_DIR}")
        sys.exit(1)

    if not template_files:
        print("No template files found in the logbooking-templates directory.")
        sys.exit(1)

    print("Available Logbook Templates:")
    for idx, file in enumerate(template_files, start=1):
        template_name = file.replace(".md.template", "")
        print(f"  {idx}. {template_name}")

    # Select a template.
    while True:
        try:
            choice = int(input("\nSelect a template by number: "))
            if 1 <= choice <= len(template_files):
                selected_template_file = template_files[choice - 1]
                break
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

    # The logbook name is derived from the template file name.
    logbook_name = selected_template_file.replace(".md.template", "")
    print(f"\nSelected Logbook Type: {logbook_name}")

    # Read the selected template.
    template_path = os.path.join(TEMPLATE_DIR, selected_template_file)
    try:
        with open(template_path, "r", encoding="utf-8") as file:
            template_text = file.read()
    except IOError as e:
        print(f"Error reading template file: {e}")
        sys.exit(1)

    # Extract variables from the template.
    variables_in_template = scan_template_variables(template_text)

    # Prepare dictionary to hold variable values.
    variables = {}
    for var in variables_in_template:
        if var == "LOGBOOK_NAME":
            variables[var] = logbook_name
        elif var == "LOGBOOK_ENTRY_FILENAME":
            # This will be overridden later to include the title.
            variables[var] = get_filename_timestamp() + ".md"
        elif var in AUTO_VARIABLES:
            variables[var] = AUTO_VARIABLES[var]()
        else:
            variables[var] = prompt_for_variable(var)

    # Ask for additional details about the log entry.
    title = input("\nEnter log entry title: ").strip()
    if title:
        variables["TITLE"] = title
    else:
        variables["TITLE"] = logbook_name  # Fallback if not provided.

    # Update LOGBOOK_ENTRY_FILENAME to include the log entry title and a timestamp.
    # Sanitize the title by replacing non-word characters with underscores.
    safe_title = re.sub(r'\W+', '_', variables["TITLE"]).strip('_')
    variables["LOGBOOK_ENTRY_FILENAME"] = f"{safe_title}_{get_filename_timestamp()}.md"

    # Allow user to review and edit variable values.
    while True:
        display_variables(variables)
        edit_choice = input("\nEnter the number of a variable to edit (or press Enter to continue): ").strip()
        if not edit_choice:
            break
        try:
            idx = int(edit_choice)
            if 1 <= idx <= len(variables):
                var_key = list(variables.keys())[idx - 1]
                new_value = input(f"Enter new value for ${var_key} (current: {variables[var_key]}): ").strip()
                if new_value:
                    variables[var_key] = new_value
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    # Final confirmation before generating the log entry.
    print("\nFinal Variables:")
    display_variables(variables)
    confirm = input("\nConfirm and generate log entry? (Y/n): ").strip().lower()
    if confirm not in ("", "y", "yes"):
        print("Log entry generation cancelled.")
        sys.exit(0)

    # Replace variables in the template.
    def variable_replacer(match):
        var_name = match.group(1)
        return variables.get(var_name, match.group(0))

    final_content = re.sub(r'\$([A-Z0-9_]+)\b', variable_replacer, template_text)

    # Determine output directory relative to repository root.
    # Assuming this script is in tools/scripts and logbooks is in the repo root.
    repo_root = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
    output_dir = os.path.join(repo_root, "logbooks", logbook_name)
    os.makedirs(output_dir, exist_ok=True)

    output_filename = variables.get("LOGBOOK_ENTRY_FILENAME", get_filename_timestamp() + ".md")
    output_path = os.path.join(output_dir, output_filename)

    try:
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write(final_content)
        print("\n=== Log Entry Generated Successfully ===")
        print(f"File Location: {output_path}\n")
    except IOError as e:
        print(f"Error writing log entry file: {e}")
        sys.exit(1)

    # Display the final file content.
    print("Final File Content:\n")
    print(final_content)

    print("\nYou may open this file to review or further edit it.")
    input("Press Enter to exit the script...")

if __name__ == "__main__":
    main()
