# Healthcare Provider Coverage System

## Overview

The Healthcare Provider Coverage System is a Python and Excel-based project that simulates a healthcare provider scheduling system. It automatically generates realistic provider and scheduling data, then uses Excel dashboards, XLOOKUPs, PivotTables, and data validation to quickly retrieve and analyze provider coverage.

This project demonstrates how Python can automate data generation while Excel provides powerful reporting and analysis tools.

---

## Features

- Generate realistic provider and schedule data using Python
- Create automated Excel workbooks
- Interactive provider lookup dashboard
- XLOOKUP-based provider search
- Data validation drop-down lists
- PivotTables for staffing analysis
- Department and shift coverage reporting
- Historical and future schedule tracking

---

## Technologies Used

- Python
- pandas
- Faker
- openpyxl
- Microsoft Excel
- XLOOKUP
- PivotTables
- Data Validation
- Git
- GitHub

---

## Project Structure

```
create_schedule.py
Healthcare_OnCall_Dashboard.xlsx
Healthcare_OnCall_Raw_Data.xlsx
requirements.txt
README.md
.gitignore
screenshots/
```

---

## Business Problem

Healthcare organizations must ensure that every department has provider coverage while making provider schedules easy to search and analyze.

This project demonstrates how automation can reduce manual data entry and provide fast access to provider scheduling information through an interactive Excel dashboard.

---

## How to Run

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run:

```bash
python create_schedule.py
```

4. Open **Healthcare_OnCall_Dashboard.xlsx** to explore the dashboard and reports.

---

## Future Enhancements

- Store provider schedules in Amazon RDS instead of Excel
- Use Amazon S3 for file storage
- Integrate SQL queries for reporting
- Add AI-powered schedule analysis
- Build a web interface using React
- Automate dashboard refreshes

---

## Screenshots
### Dashboard Overview

Interactive dashboard that allows users to select a date, department, and shift to instantly retrieve the assigned healthcare provider using XLOOKUP.

![Dashboard Overview](screenshots/dashboard-overview.png)

---

### Providers Dataset

Healthcare provider master dataset generated with Python.

![Providers Dataset](screenshots/providers-table.png)

---

### Schedule Dataset

Automatically generated provider schedule containing department assignments, shifts, and scheduling status.

![Schedule Dataset](screenshots/schedule-table.png)

---

### Department Shift Coverage Summary

PivotTable summarizing assigned shifts by department and month.

![Department Shift Coverage Summary](screenshots/department-coverage-pivot.png)

---

### Provider Workload Summary

PivotTable showing the distribution of assigned shifts across healthcare providers.

![Provider Workload Summary](screenshots/provider-workload-pivot.png)

---

### Provider Level Distribution

PivotTable displaying the staffing mix of Residents, Fellows, and Attendings.

![Provider Level Distribution](screenshots/provider-level-distribution.png)

---

### Schedule Status Summary

PivotTable summarizing the status of scheduled shifts.

![Schedule Status Summary](screenshots/schedule-status-summary.png)

---

## Author

**Keona Lollis**

- GitHub: https://github.com/kekaleka
- LinkedIn: www.linkedin.com/in/keona-lollis-924176266