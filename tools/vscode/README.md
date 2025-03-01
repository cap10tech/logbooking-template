# VS Code Snippets Installation Instructions

This guide explains how to install custom code snippets in Visual Studio Code using the provided JSON files.

## Files Provided

- **cap10-tech-logbooking-template.json**
- **logbooking-templates.json**

## Installation Steps

1. **Open VS Code:**  
   Launch Visual Studio Code.

2. **Open User Snippets:**  
   - Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on macOS) to open the Command Palette.
   - Type and select **"Preferences: Configure User Snippets"**.

3. **Create or Select a Snippet File:**  
   - To add global snippets, select **"New Global Snippets file"** and provide a name (for example, `custom-snippets.code-snippets`).
   - Alternatively, if your snippets are language-specific, choose the corresponding snippet file.

4. **Paste the JSON Snippets:**  
   Open one of the provided JSON files (either `cap10-tech-logbooking-template.json` or `logbooking-templates.json`), copy its content, and paste it into your user snippet file.

5. **Save the File:**  
   Save your snippet file. VS Code will automatically load the new snippets.

6. **Verify Installation:**  
   Open or create a file in the relevant language and type one of the snippet prefixes (such as `.sh` or `.s`) to confirm the snippet suggestion appears.

Your custom snippets are now installed and ready for use in VS Code.

---

###  Logbooking Tools Directory Structure

```
tools
|--+ jetbrains
|--+ scripts
`-- vscode
    |-- README.md (* This File)
    |-- cap10-tech-logbooking-template.json
    `-- logbooking-templates.json
```

