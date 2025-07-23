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

Below is a comprehensive README that explains every template in detail, what they do, how to use them, and some suggestions from cap10.tech to help you lead like a captain.

---

# Cap10.Tech Logbooking Templates

This project is designed to streamline your logging, documentation, and task reporting across multiple areas. Whether you’re debugging code, maintaining servers, managing a team, or logging incident details, these templates provide a consistent and efficient format. Cap10.tech believes that a true captain keeps a meticulous log, every detail matters. Use these templates to stay organized, accountable, and in command of your projects.

---

## Template Categories

The templates are grouped into two main categories:

1. **Markdown Table Templates**  
   Quickly generate markdown tables with various dimensions.

2. **Log Templates for Different Scenarios**  
   Use dedicated templates for software development, IT operations, manufacturing, project management, customer support, and more.

3. **Cap10Bill Custom Shell Templates**  
   Tailored shell-based logging templates for detailed task and content recording.

---

## 1. Markdown Table Templates

These templates let you instantly create markdown tables in your log files. They are named by their dimensions, for example:

- **`..table.1.1`**, **`..table.1.2`**, **`..table.1.3`**  
  These templates create tables with one header column and one, two, or three rows respectively.

- **`..table.2.1`**, **`..table.2.2`**, **`..table.2.3`**  
  These generate tables with two header columns. The numbers indicate how many rows of values follow.

- **`..table.3.1`**, **`..table.3.2`**, **`..table.3.3`**  
  With three header columns, these templates are useful for more complex data arrangements.

- Templates continue for tables up to 8 columns (e.g., **`..table.8.1`**, **`..table.8.2`**, **`..table.8.3`**).

**How to Use:**  
When you activate a table template, your IDE prompts you for header names and cell values. Simply fill in the variables, and your table is generated with proper markdown formatting.

**Cap10 Suggestion:**  
_As a captain, always keep your data organized. Use these table templates to quickly summarize results or action items during your daily standups and team meetings._

---

## 2. Log Templates for Various Scenarios

These templates help capture essential details in different operational contexts. Each log template includes variables that you can customize, ensuring consistency and clarity in your records.

### ..logdev – Debugging/Development Log

- **Purpose:** Capture debugging steps and development issues.
- **Fields Include:**
   - **Project:** The project name.
   - **Issue:** A brief description of the problem (e.g., "Application crashes on startup").
   - **Date:** Automatically filled with the current date.
   - **Steps Taken:** Detailed troubleshooting steps.
   - **Resolution:** How the issue was resolved.

**Usage Tip:**  
Record every step of your debugging process to build a knowledge base for future reference.

**Cap10 Suggestion:**  
_As the captain of your project, leave a clear trail of decisions and actions so that your crew (or team) can learn from every encounter._

---

### ..logit – Server Maintenance Log

- **Purpose:** Log IT operations, such as updates, patch installations, and service restarts.
- **Fields Include:**
   - **Date:** Automatically generated.
   - **Server:** Specify the server name (e.g., "WebServer01").
   - **Actions Taken:** List out maintenance tasks.

**Usage Tip:**  
After every maintenance window, use this log to document actions taken and verify system health.

**Cap10 Suggestion:**  
_A true captain reviews system logs frequently, document maintenance to ensure smooth sailing of your infrastructure._

---

### ..logmanu – Machine Performance Log

- **Purpose:** Record observations and next steps in manufacturing or production environments.
- **Fields Include:**
   - **Machine ID:** Identify the machine (e.g., "CNC-204").
   - **Date:** Current date.
   - **Observations:** Details such as performance metrics or anomalies.
   - **Next Steps:** Planned maintenance or adjustments.

**Usage Tip:**  
Utilize this log to track machine performance over time, helping to anticipate future issues.

**Cap10 Suggestion:**  
_Just as a ship’s captain monitors the engine room, monitor your machines and document their performance to prevent future breakdowns._

---

### ..logkanban – Kanban Board Log

- **Purpose:** Track progress and status for tasks in a Kanban system.
- **Fields Include:**
   - **Project:** Name of the project.
   - **Task:** Brief description of the task.
   - **Status:** Current status (default “In Progress”).
   - **Assignee:** Person responsible.
   - **Date:** Automatically generated.
   - **Notes:** Additional information.

**Usage Tip:**  
Use this template during agile meetings to quickly update the status of tasks on your board.

**Cap10 Suggestion:**  
_As captain, keeping a visible log of tasks ensures that your crew knows their assignments and progress is clear to everyone._

---

### ..logshift – Shift Report Log

- **Purpose:** Document shift changes and issues encountered during a work shift.
- **Fields Include:**
   - **Shift:** Specify the shift (default “Morning”).
   - **Date:** Automatically set.
   - **Supervisor:** Name of the supervisor.
   - **Issues:** Report any issues observed.
   - **Actions Taken:** What was done to address the issues.
   - **Comments:** Extra remarks.

**Usage Tip:**  
Keep a daily shift report to help with handovers between teams.

**Cap10 Suggestion:**  
_Effective leadership means clear communication, ensure every shift has a complete and honest report._

---

### ..logpr – Pull Request Checklist

- **Purpose:** Ensure quality in pull requests with an interactive checklist.
- **Fields Include:**
   - **Functionality, Correctness, Code Style, Readability, Testing, Documentation, Comments, Error Handling, Performance, Security, Dependencies, Backward Compatibility, Commit Quality, Code Duplication, Peer Feedback:**  
     These checkboxes help you verify that every aspect of your code meets the required standards.
   - **Additional Comments/Notes:** For any extra details.

**Usage Tip:**  
Before merging a pull request, run through this checklist to catch potential issues.

**Cap10 Suggestion:**  
_A captain double-checks all details before setting sail, make sure your code is battle-ready before it’s merged._

---

### ..logsupport – Customer Support Log

- **Purpose:** Document customer support interactions and resolutions.
- **Fields Include:**
   - **Customer:** Name of the customer.
   - **Date:** Current date.
   - **Issue Reported:** Summary of the reported problem.
   - **Support Agent:** The agent’s name.
   - **Resolution:** How the issue was resolved.
   - **Follow-up:** Any follow-up actions required.

**Usage Tip:**  
Keep a detailed support log to track recurring issues and improve service quality.

**Cap10 Suggestion:**  
_A captain values every member of the crew, recording support details ensures that customer issues are resolved and learning is shared._

---

### ..logretro – Project Retrospective Log

- **Purpose:** Capture lessons learned after project completion.
- **Fields Include:**
   - **Project:** Project name.
   - **Date:** Current date.
   - **What Went Well:** Positive aspects.
   - **Challenges:** Areas that need improvement.
   - **Action Items:** Steps to address challenges.
   - **Overall Rating:** A summary rating.

**Usage Tip:**  
Use this retrospective log in post-mortem meetings to drive continuous improvement.

**Cap10 Suggestion:**  
_The best captains learn from every voyage, reflect on successes and challenges to improve future operations._

---

### ..logincident – Incident Response Log

- **Purpose:** Record details of critical incidents.
- **Fields Include:**
   - **Incident ID:** Unique identifier for the incident.
   - **Date:** When the incident occurred.
   - **Impact:** Describe the impact.
   - **Cause:** What triggered the incident.
   - **Actions Taken:** Steps taken to mitigate the issue.
   - **Resolution:** Final resolution details.

**Usage Tip:**  
This log is essential for high-severity events. Use it to conduct thorough post-incident reviews.

**Cap10 Suggestion:**  
_Every crisis teaches a lesson, document incidents carefully so that future risks are minimized._

---

### ..logqa – Quality Assurance Log

- **Purpose:** Track quality assurance activities and outcomes.
- **Fields Include:**
   - **Project:** The project under review.
   - **Date:** Current date.
   - **Tested By:** Name of the tester.
   - **Issues Found:** Document bugs or issues.
   - **Recommendations:** Suggestions for improvement.

**Usage Tip:**  
Regularly update this log during testing cycles to ensure that all issues are tracked.

**Cap10 Suggestion:**  
_A good captain inspects every detail, ensure quality by systematically logging your QA reports._

---

### ..logsales – Sales Call Log

- **Purpose:** Record details of sales calls and follow-up actions.
- **Fields Include:**
   - **Client:** Name of the client.
   - **Date:** Current date.
   - **Sales Rep:** The salesperson’s name.
   - **Discussion Points:** Key points discussed.
   - **Next Steps:** Planned follow-up actions.

**Usage Tip:**  
Keep your sales interactions logged to refine your pitch and improve client relations.

**Cap10 Suggestion:**  
_Leadership in sales comes from knowing your numbers, log every call to chart your course for success._

---

### ..logfinance – Financial Transaction Log

- **Purpose:** Track financial transactions and related details.
- **Fields Include:**
   - **Transaction ID:** Unique ID for the transaction.
   - **Date:** When the transaction occurred.
   - **Amount:** The transaction value.
   - **Type:** Type of transaction.
   - **Account:** Related account details.
   - **Notes:** Any additional commentary.

**Usage Tip:**  
Ensure all financial dealings are clearly recorded for auditing and reporting purposes.

**Cap10 Suggestion:**  
_A financial captain never loses sight of the details, accurate logs prevent future turbulence._

---

### ..logmarketing – Marketing Campaign Log

- **Purpose:** Document marketing efforts and campaign results.
- **Fields Include:**
   - **Campaign:** Name of the marketing campaign.
   - **Date:** When the campaign was launched.
   - **Channel:** Marketing channel used.
   - **Objective:** Campaign goals.
   - **Results:** Outcomes and metrics.
   - **Next Steps:** Follow-up actions.

**Usage Tip:**  
Use this log to measure campaign effectiveness and adjust strategies accordingly.

**Cap10 Suggestion:**  
_As your captain, steer your marketing campaigns with precision, each log is a beacon for future strategy._

---

## 3. Cap10Bill Custom Shell Templates

These templates are provided in the separate **cap10-tech-logbooking-templates.xml** file. They focus on shell-based logging for content and task recording.

### ..s – Simple Shell Block

- **Purpose:** A straightforward shell snippet for content logging.
- **Usage:**
   - **DESCRIPTION:** A brief summary.
   - **CONTENTS:** The shell commands or content block.
   - **NOTES:** Additional remarks.

**Cap10 Suggestion:**  
_Keep it simple and effective, your logs should be as clear as the captain’s orders._

---

### ..sh – Shell Block with Task/Step Description

- **Purpose:** Similar to the simple shell template, but designed to include a detailed task or step description.
- **Usage:**
   - Fill in the **DESCRIPTION**, **CONTENTS**, and **NOTES** fields.

**Cap10 Suggestion:**  
_Clarify your actions like a true captain, explain what needs to be done and why, so your team follows suit._

---

### ..shm – Full Logbooking Template with Multiple Shell Blocks

- **Purpose:** A comprehensive template featuring five separate shell blocks for complex logging.
- **Usage:**
   - **DESCRIPTION:** Overall summary.
   - **CONTENTS, ADDITIONAL_CONTENT, MORE_CONTENT, FURTHER_CONTENT, FINAL_CONTENT:** Use these blocks to break down your logging into multiple steps or phases.
   - **NOTES:** Final remarks or observations.

**Cap10 Suggestion:**  
_When operations get complex, detail every step, your logs are your battle plan. A captain who documents every phase ensures the crew is always informed._

---

## Final Thoughts

Cap10.tech’s suite of logbooking templates is designed to empower you to be the captain of your projects. Whether you are debugging code, maintaining systems, or managing teams, these templates help you capture every critical detail in a structured and efficient manner.

**Captain’s Advice:**
- **Customize:** Tailor each template to your specific needs, modify the default values and adjust fields if necessary.
- **Review Regularly:** Your logs are a living document; update them as projects evolve.
- **Share and Learn:** Use your logs to reflect on successes and failures, and share lessons learned with your team.

By using these templates, you not only save time but also create a reliable record that guides you and your team through calm and storm alike. Lead with clarity, precision, and the confidence of a true captain.

---

