# JetBrains Live Template Installation Instructions

This guide explains how to install custom live templates for your JetBrains IDE (e.g., IntelliJ IDEA, PyCharm, WebStorm) by manually copying the XML files into the correct configuration folder.

## Files Provided

- **cap10-tech-logbooking-templates.xml**
- **logbooking-templates.xml**

## Installation Steps

### Windows

1. **Locate Your Configuration Folder:**  
   Open File Explorer and navigate to: ```C:\Users\<username>\AppData\Roaming\JetBrains\<application_version_folder>\templates```
   - Replace `<username>` with your Windows username and `<application_version_folder>` with your IDE’s folder (e.g., `IntelliJIdea2023.2`, `PyCharm2023.1`, etc.).

2. **Copy the Template File:**  
   Choose the desired XML file (either `cap10-tech-logbooking-templates.xml` or `logbooking-templates.xml`) and copy it into the `templates` folder.

3. **Restart Your IDE:**  
   Close and reopen your JetBrains IDE so it loads the new live templates.

4. **Verify Installation:**  
   In your IDE, go to **File > Settings** (or **[IDE Name] > Preferences** on macOS) and navigate to **Editor > Live Templates**. Confirm that your new templates are listed.

### macOS

1. **Locate Your Configuration Folder:**  
   Open Finder and navigate to:  
   ```~/Library/Application Support/JetBrains/<application_version_folder>/templates   ```  
   -   Replace `<application_version_folder>` with your IDE’s folder name.

2. **Copy the Template File:**  
   Copy your chosen XML file into the `templates` folder.

3. **Restart Your IDE:**  
   Close and reopen your IDE.

4. **Verify Installation:**  
   Check **Preferences > Editor > Live Templates** to see your new templates.

### Linux

1. **Locate Your Configuration Folder:**  
   Open your file manager or terminal and navigate to:  
   ```~/.config/JetBrains/<application_version_folder>/templates```  
   - Replace `<application_version_folder>` with the correct folder for your IDE.

2. **Copy the Template File:**  
   Copy the desired XML file into this directory.

3. **Restart Your IDE:**  
   Restart your JetBrains IDE.

4. **Verify Installation:**  
   In your IDE settings under **Editor > Live Templates**, verify that the new templates are available.

Your live templates are now installed and ready to use.

---

### Logbooking Template Tools Directory Structure

```shell

tools
|-- jetbrains
|   |-- README.md (* This File)
|   |-- cap10-tech-logbooking-templates.xml
|   `-- logbooking-templates.xml
|--+ scripts
`--+ vscode
```

