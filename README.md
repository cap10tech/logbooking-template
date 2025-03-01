# LogBooking Template

Welcome to the **LogBooking Template** repository. This project provides a collection of automated log templates and scripts to help you generate different types of logs—such as research logs, pull request logs, troubleshooting sessions, and more—with minimal effort.

The repository is organized to help you quickly set up your logbooks, configure your IDE templates, and eventually use scripts that prompt for key information before generating the log files.

## Repository Overview

- **[logbooks](./logbooks/)**  
  Contains base directories for different log categories:
  - [learning-skills](./logbooks/learning-skills)
  - [pull-requests](./logbooks/pull-requests)
  - [research](./logbooks/research)
  - [troubleshooting-session](./logbooks/troubleshooting-session)

- **[tools](./tools/)**  
  Provides IDE-specific template files:
  - **JetBrains**  
    Live templates in XML format. See [tools/jetbrains/README.md](./tools/jetbrains/README.md) for installation instructions.
  - **VS Code**  
    Code snippets in JSON format. See [tools/vscode/README.md](./tools/vscode/README.md) for details.
  - **scripts**  
    *(Coming soon)* Contains clean, well-documented scripts to automate log generation.

- **[guides](./guides/)**  
  Documentation to help you understand log booking and related workflows:
  - [Git Repositories](./guides/git-repositories.md)
  - [Markdown Logbooking](./guides/markdown-logbooking.md)

- **[examples](./examples/)**  
  Example documents to get you started:
  - [PostgreSQL Install Guide](./examples/postgresql-install.md)

- **logbook.md**  
  A sample logbook file demonstrating the template structure.

## Automated Log Generation Scripts

Our goal is to provide scripts (in the **tools/scripts/** directory) that will:
- **Prompt for Key Information:**  
  Ask for log title, description, date, and other parameters to create a new log file.
- **Generate Log Files:**  
  Automatically create log files in the corresponding `logbooks/<bookname>` directory.
- **Review & Re-Edit Configuration:**  
  Allow you to review and adjust configuration settings before finalizing the log entry.

Each script is written with clean code practices, includes meaningful naming, and provides inline explanations of the logic and decisions made. This makes it easy to understand, maintain, and extend the functionality for different types of logs such as research, pull requests, or troubleshooting sessions.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/cap10tech/logbooking-template.git
   cd logbooking-template
   ```

2. **Review the Repository Structure:**  
   Familiarize yourself with the layout by exploring the folders listed in the [Repository Overview](#repository-overview).

3. **Set Up Your IDE Templates:**
  - **JetBrains IDEs:** Follow the instructions in [tools/jetbrains/README.md](./tools/jetbrains/README.md).
  - **VS Code:** Follow the instructions in [tools/vscode/README.md](./tools/vscode/README.md).

4. **Run the Log Generation Scripts:**  
   Once available in **tools/scripts/**, run the scripts to generate log files. They will guide you through entering required details and placing the files in the appropriate logbook directories.

5. **Customize and Review:**  
   After a log file is generated, review its configuration section. You can re-edit the file as needed to tailor it to your requirements.

## Contribution

Contributions are welcome! If you have improvements, additional templates, or enhanced scripts, please open an issue or submit a pull request.

---

For more information, please check out the key areas of the repository:
- [JetBrains Templates](./tools/jetbrains/README.md)
- [VS Code Snippets](./tools/vscode/README.md)
- [Guides](./guides/)
- [Examples](./examples/)

Happy logging!
