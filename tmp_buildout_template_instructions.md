# Buildout Instructions: Converting Empty Markdown Files to Full Best-Practices Templates

## Objective
Convert all empty `*.md` files in `tools/scripts/logbooking-templates/` to comprehensive, best-practices `*.md.template` files. Each template should:
- Provide a clear structure for logbook entries relevant to its topic (e.g., SOP, meeting notes, risk assessment).
- Include required fields, prompts, and checklists to guide users in thorough documentation.
- Follow the style and detail level of existing templates (see: `learning-skills.md.template`, `pull-requests.md.template`, `research.md.template`, `troubleshooting-session.md.template`).
- Incorporate best practices for documentation, reflection, and actionable next steps.

## Steps
1. **Research Existing Templates:**
   - Review all current `*.md.template` files for structure, required fields, prompts, and formatting conventions.
   - Note common sections (e.g., Overview, Objectives, Action Items, Lessons Learned, Resources).

2. **Analyze Empty Markdown Files:**
   - Identify the purpose of each empty `*.md` file (e.g., `sop.md` for Standard Operating Procedures, `meeting-notes.md` for meeting documentation).
   - Draft a list of required fields and sections for each based on its topic and best practices.

3. **Design Template Structure:**
   - For each file, create a template with:
     - Title and filename variables (e.g., `TITLE: $TITLE`, `LOGBOOK_ENTRY_FILENAME: $LOGBOOK_ENTRY_FILENAME`)
     - Section headings and checklists for required information
     - Prompts and guides to encourage thorough, actionable documentation
     - Example code blocks or command sections if relevant
     - Best practices and tips for effective logging

4. **Write and Format Templates:**
   - Use markdown formatting: headings, bullet points, checklists, code blocks, block quotes
   - Ensure clarity, completeness, and ease of use
   - Reference internal guides or resources where appropriate

5. **Review and Iterate:**
   - Compare each new template to existing examples for consistency and completeness
   - Solicit feedback from a senior coach/leader/drill sergeant for improvements
   - Revise templates as needed to meet high standards

## Guidance for ChatGPT Agent
- Be thorough and creative: Each template should enable users to capture all relevant details for the log type
- Use prompts and checklists to guide reflection, action, and improvement
- Maintain consistency in style and structure across all templates
- Reference best practices and internal guides where possible
- Ask for feedback and iterate if templates are unclear or incomplete

## Example Template Sections (for reference)
- Title & Filename
- Overview / Purpose
- Required Fields & Prompts
- Action Items / Next Steps
- Lessons Learned / Reflections
- Resources & References
- Best Practices

## Target Files
Convert the following files:
- change-request.md
- compliance-audit.md
- decision-log.md
- kpi-tracker.md
- meeting-notes.md
- process-retrospective.md
- risk-assessment.md
- root-cause-analysis.md
- sop.md
- training-session.md

## Deliverable
For each file, produce a corresponding `*.md.template` file with:
- Full structure and required fields
- Prompts and best practices
- Consistent formatting and style

## Progress Tracker

| Template File                | Status         | Notes |
|-----------------------------|----------------|-------|
| change-request.md.template   | Complete       | Full template drafted and created |
| compliance-audit.md.template | Complete       | Full template drafted and created |
| decision-log.md.template     | Complete       | Full template drafted and created |
| kpi-tracker.md.template      | Complete       | Full template drafted and created |
| meeting-notes.md.template    | Complete       | Full template drafted and created |
| process-retrospective.md.template | Complete   | Full template drafted and created |
| risk-assessment.md.template  | Complete        | Full template drafted and created |
| root-cause-analysis.md.template | In Progress    | Researching structure |
| sop.md.template              | Pending        |       |
| training-session.md.template | Pending        |       |

---

### Current Step
- Researching existing templates and analyzing required fields for root-cause-analysis.md.template.

---

**Senior Coach/Leader/Drill Sergeant Guidance:**
- Review each template for completeness, clarity, and actionable guidance
- Ensure templates drive high-quality, reflective, and useful logbook entries
- Provide feedback and request revisions as needed

---

Ready to begin the buildout. Proceed with research, drafting, and review for each template.
