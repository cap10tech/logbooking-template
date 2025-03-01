
## Code Template Groups Overview

Our template set is divided into three main groups:

1. **Basic Log Templates:** Quickly capture shell commands, Python snippets, and short logs.
2. **Markdown Table Templates:** Neatly format data into tables (from 1x1 up to 8x3).
3. **Specialized Log Templates:** For debugging, server maintenance, pull request reviews, incident response, and more.
4. **Cap10Bill Logbooking Templates:** Advanced templates for detailed shell logging with multiple blocks.

---

## 1. Basic Log Templates

| **Shortcut** | **Description**                               | **Example Usage** |
|--------------|-----------------------------------------------|-------------------|
| `.sh`        | **Quick Shell Script Log Template** – Capture a shell command along with a brief description and notes. | <pre>- System Update Log  
```shell
sudo apt-get update && sudo apt-get upgrade
```  
> Updated packages and applied security patches.
</pre> |
| `.py`        | **Quick Python Log Template** – Document Python code snippets and debugging sessions. | <pre>- API Debugging Log  
```python
import requests
response = requests.get("https://api.example.com/data")
print(response.json())
```  
> Resolved API endpoint issue.
</pre> |

---

## 2. Markdown Table Templates

Use these templates to insert preformatted Markdown tables. Simply type the shortcut and expand the template to fill in your headers and data.

| **Shortcut**    | **Description**                | **Example Usage**                                                                                           |
|-----------------|--------------------------------|-------------------------------------------------------------------------------------------------------------|
| `.table.1.1`    | Markdown Table (1x1)           | <pre>|Header1|  
|-------------|
|Value1|</pre>                                                     |
| `.table.1.2`    | Markdown Table (1x2)           | <pre>|Header1|  
|-------------|
|Value1|
|Value2|</pre>                                                   |
| `.table.1.3`    | Markdown Table (1x3)           | Similar structure with three rows under one header.                                                       |
| `.table.2.1`    | Markdown Table (2x1)           | <pre>|Header1|Header2|  
|-------------|-------------|
|Value1|Value2|</pre>                                                    |
| `.table.2.2`    | Markdown Table (2x2)           | <pre>|Header1|Header2|  
|-------------|-------------|
|Value1|Value2|
|Value3|Value4|</pre>                                              |
| `.table.2.3`    | Markdown Table (2x3)           | Similar to 2x2 with an extra row for additional values.                                                   |
| `.table.3.1`    | Markdown Table (3x1)           | …                                                                                                           |
| `.table.3.2`    | Markdown Table (3x2)           | …                                                                                                           |
| `.table.3.3`    | Markdown Table (3x3)           | …                                                                                                           |
| `.table.4.1` to `.table.8.3` | Markdown Tables of varying sizes (4x1 up to 8x3) | Use these templates for larger data sets. Example for `.table.4.1`: <pre>|H1|H2|H3|H4|  
|-------------|-------------|-------------|-------------|  
|V1|V2|V3|V4|</pre>  |

*(For full details, refer to the XML template definitions in your template set.)*

---

## 3. Specialized Log Templates

| **Shortcut**      | **Description**                                  | **Example Usage**                                                                                   |
|-------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `.logdev`         | **Debugging Log Template** – Document issues, steps, and resolutions.  | <pre># Debugging Log - MyProject  
**Issue:** Application crashes on startup  
**Date:** 2025-02-28  
**Steps Taken:**
- Checked error logs
- Identified missing dependency  
  **Resolution:** Installed missing package</pre>  |
  | `.logit`          | **Server Maintenance Log** – Track server updates and actions.         | <pre># Server Maintenance Log  
  **Date:** 2025-02-28  
  **Server:** WebServer01  
  **Actions Taken:**
- Updated security patches
- Restarted services
- Verified connectivity</pre> |
  | `.logmanu`        | **Machine Performance Log** – Log observations and next steps for manufacturing equipment. | <pre># Machine Performance Log - CNC-204  
  **Date:** 2025-02-28  
  **Observations:**
- Temperature within normal range
- Minor vibration detected  
  **Next Steps:** Schedule preventive maintenance</pre> |
  | `.logkanban`      | **Kanban Board Log Template** – Track task status and notes.           | <pre># Kanban Board Log - Project X  
  **Task:** Refactor authentication  
  **Status:** In Progress  
  **Assignee:** John Doe  
  **Date:** 2025-02-28  
  **Notes:** Needs further code review</pre>  |
  | `.logshift`       | **Shift Report Log Template** – Record shift details and issues.       | <pre># Shift Report - Morning  
  **Date:** 2025-02-28  
  **Supervisor:** Jane Smith  
  **Issues:** Delayed deployments  
  **Actions Taken:** Restarted CI server  
  **Comments:** Monitor next shift for improvements</pre>  |
  | `.logpr`          | **Pull Request Checklist Template** – Interactive checklist for PR reviews. | <pre># Pull Request Checklist
- [ ] **Functionality:** Verify intended problem is solved
  - *Notes:* Validate edge cases.
- [ ] **Correctness:** Check error handling
  - *Notes:* Ensure tests pass.  
    …  
    Additional Comments: $ADDITIONAL$</pre>  |
    | `.logsupport`     | **Customer Support Log Template** – Document support interactions.     | <pre># Customer Support Log - ACME Corp  
    **Date:** 2025-02-28  
    **Issue Reported:** Unable to login  
    **Support Agent:** Alice  
    **Resolution:** Reset password  
    **Follow-up:** Confirm login success</pre>  |
    | `.logretro`       | **Project Retrospective Log Template** – Reflect on project outcomes.   | <pre># Project Retrospective - Project Y  
    **Date:** 2025-02-28  
    **What Went Well:** Timely delivery  
    **Challenges:** Scope creep  
    **Action Items:** Tighten project specs  
    **Overall Rating:** 8/10</pre>  |
    | `.logincident`    | **Incident Response Log Template** – Track incidents and resolutions.   | <pre># Incident Response Log - INC-123  
    **Date:** 2025-02-28  
    **Impact:** System downtime  
    **Cause:** Misconfiguration  
    **Actions Taken:** Corrected config  
    **Resolution:** System restored</pre>  |
    | `.logqa`          | **QA Report Log Template** – Record QA testing outcomes.                | <pre># QA Report - Project Z  
    **Date:** 2025-02-28  
    **Tested By:** Bob  
    **Issues Found:** Minor UI glitches  
    **Recommendations:** Improve responsiveness</pre>  |
    | `.logsales`       | **Sales Call Log Template** – Document sales interactions.              | <pre># Sales Call Log - ACME Corp  
    **Date:** 2025-02-28  
    **Sales Rep:** Carol  
    **Discussion Points:** New product features  
    **Next Steps:** Schedule follow-up call</pre>  |
    | `.logfinance`     | **Financial Transaction Log Template** – Log transaction details.       | <pre># Financial Transaction Log - TXN-789  
    **Date:** 2025-02-28  
    **Amount:** $1,000  
    **Type:** Credit  
    **Account:** BankXYZ  
    **Notes:** Payment processed successfully</pre>  |
    | `.logmarketing`   | **Marketing Campaign Log Template** – Record campaign details.          | <pre># Marketing Campaign Log - Summer Promo  
    **Date:** 2025-02-28  
    **Channel:** Social Media  
    **Objective:** Increase engagement  
    **Results:** +20% interactions  
    **Next Steps:** Optimize ads</pre>  |

---

## 4. Cap10Bill Logbooking Templates

| **Shortcut** | **Description**                                                   | **Example Usage**                                                                                                      |
|--------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `.s`         | **Simple Shell Block for Content Logging** – Basic template for quick notes with a shell code block. | <pre>- Simple Update Note  
```shell
echo "System updated"
```  
> Quick note on system update.
</pre> |
| `.sh`        | **Shell Block with Task/Step Description** – Capture task details and corresponding shell commands. | <pre>- Deploy Application  
```shell
scp app.zip user@server:/deployments/
```  
> Deployment initiated.
</pre> |
| `.shm`       | **Full Logbooking Template for Task/Step Logging (5 Shell Blocks)** – Detailed log with multiple code blocks for different stages of a task. | <pre>- Comprehensive Deployment Log  
```shell
# Step 1: Upload package
scp app.zip user@server:/deployments/
```  
```shell
# Step 2: SSH into server
ssh user@server
```  
```shell
# Step 3: Unzip package
unzip app.zip -d /deployments/app
```  
```shell
# Step 4: Restart service
sudo systemctl restart app.service
```  
```shell
# Step 5: Check service status
sudo systemctl status app.service
```  
> Deployment completed successfully.
</pre> |

---

## Quick Reference: How to Use These Templates

1. **Triggering a Template:**
  - **IntelliJ IDEA:**  
    Type the template shortcut (e.g., `.sh`, `.logpr`) in the editor and press **Tab** to expand.
  - **Visual Studio Code:**  
    Type the snippet prefix (e.g., `logsh`) and select the snippet from the suggestion list, then press **Enter**.

2. **Filling in Placeholders:**
  - Navigate through placeholders (e.g., `$TITLE$`, `$CONTENTS$`, `$NOTES$`) using the **Tab** key.
  - Replace the variables with your specific log entry details.

3. **Customizing Your Log Entries:**
  - Edit the expanded template to add any additional notes or commands.
  - Save your log entries in your project repository for version control.

4. **Version Control Integration:**
  - Store your logbook files in your repository.
  - Use Git to track changes and review historical logs.

---

Happy logbooking and keep crushing it!

*For more tips and advanced techniques, visit [cap10.tech](https://cap10.tech).*