"""
========================================================
Project Name:
Healthcare Provider Coverage & Historical Lookup System

Author:
Keona Lollis

Description:
This program generates fictional healthcare provider data
and a 61-day on-call schedule covering:

- The previous 30 days
- Today
- The next 30 days

The generated raw-data workbook supports an interactive
Microsoft Excel lookup tool and PivotTable dashboard.

Privacy Notice:
All names, phone numbers, email addresses, provider records,
and schedules are fictional. This project contains no real
healthcare, patient, or employer data.
========================================================
"""

# =====================================================
# Import Required Libraries
# =====================================================

import random
from datetime import date, datetime, time, timedelta

import pandas as pd
from faker import Faker

# =====================================================
# Initialize Faker
# =====================================================

fake = Faker()


# =====================================================
# Create Department and Specialty Pairings
# =====================================================

department_specialties = {
    "Emergency Medicine": "Trauma",
    "Cardiology": "Cardiology",
    "Neurology": "Neurology",
    "Pediatrics": "Pediatrics",
    "Orthopedics": "Orthopedic Surgery",
    "General Surgery": "General Surgery",
    "Radiology": "Radiology",
    "Obstetrics": "Maternal-Fetal Medicine",
    "Intensive Care": "Critical Care",
    "Internal Medicine": "Internal Medicine",
}

departments = list(department_specialties.keys())


# =====================================================
# Create Provider Lookup Lists
# =====================================================

employment_types = [
    "Full-Time",
    "Part-Time",
    "PRN",
]

shift_preferences = [
    "Day",
    "Night",
    "Both",
]


# =====================================================
# Create a Realistic Staffing Plan
# =====================================================

# Each department receives:
# - 3 Residents
# - 1 Fellow
# - 1 Attending
#
# 10 departments × 5 providers = 50 providers.

staffing_plan = {
    "Emergency Medicine": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Cardiology": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Neurology": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Pediatrics": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Orthopedics": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "General Surgery": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Radiology": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Obstetrics": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Intensive Care": {"Resident": 3, "Fellow": 1, "Attending": 1},
    "Internal Medicine": {"Resident": 3, "Fellow": 1, "Attending": 1},
}

# =====================================================
# Generate Fictional Provider Records
# =====================================================

providers = []
provider_number = 1

for primary_department, level_counts in staffing_plan.items():
    specialty = department_specialties[primary_department]
    department_provider_number = 1

    for provider_level, provider_count in level_counts.items():
        for _ in range(provider_count):
            # Assign realistic experience based on provider level.
            if provider_level == "Resident":
                years_of_experience = random.randint(1, 5)
            elif provider_level == "Fellow":
                years_of_experience = random.randint(5, 8)
            else:
                years_of_experience = random.randint(8, 35)

            # Generate a hire date that roughly matches
            # the provider's years of experience.
            hire_date = fake.date_between(
                start_date=f"-{years_of_experience}y",
                end_date=f"-{max(years_of_experience - 1, 0)}y",
            )

            # Guarantee that at least two providers in every
            # department are active and available for scheduling.
            if department_provider_number <= 2:
                provider_status = "Active"
            else:
                provider_status = random.choices(
                    ["Active", "On Leave", "Vacation"],
                    weights=[90, 5, 5],
                    k=1,
                )[0]

            provider = {
                "Provider ID": f"DR{provider_number:03}",
                "Provider Name": f"Dr. {fake.name()}",
                "Primary Department": primary_department,
                "Specialty": specialty,
                "Provider Level": provider_level,
                "Hire Date": hire_date,
                "Years of Experience": years_of_experience,
                "Employment Type": random.choice(employment_types),
                "Shift Preference": random.choice(shift_preferences),
                "Status": provider_status,
                "Phone Number": fake.phone_number(),
                "Extension": random.randint(1000, 9999),
                "Email": fake.email(),
            }

            providers.append(provider)

            provider_number += 1
            department_provider_number += 1


# =====================================================
# Convert Provider Records Into a DataFrame
# =====================================================

providers_df = pd.DataFrame(providers)


# =====================================================
# Set the Schedule Date Range
# =====================================================

# Create schedules for:
# - The previous 30 days
# - Today
# - The next 30 days

schedule_start_date = date.today() - timedelta(days=30)
schedule_end_date = date.today() + timedelta(days=30)


# =====================================================
# Create Standard 12-Hour Shift Times
# =====================================================

day_shift_start = time(7, 0)
day_shift_end = time(19, 0)

night_shift_start = time(19, 0)
night_shift_end = time(7, 0)


# =====================================================
# Generate On-Call Schedule Records
# =====================================================

schedule_records = []

schedule_number = 1
current_date = schedule_start_date

while current_date <= schedule_end_date:
    for department in departments:
        # Find active providers assigned to the department.
        eligible_providers = [
            provider
            for provider in providers
            if provider["Primary Department"] == department
            and provider["Status"] == "Active"
        ]

        # Safety fallback: use any provider from the department.
        if not eligible_providers:
            eligible_providers = [
                provider
                for provider in providers
                if provider["Primary Department"] == department
            ]

        # Final fallback to prevent random.choice from
        # receiving an empty list.
        if not eligible_providers:
            eligible_providers = providers

        # Select the day provider.
        day_provider = random.choice(eligible_providers)

        # Try to assign a different provider to the night shift.
        night_candidates = [
            provider
            for provider in eligible_providers
            if provider["Provider ID"] != day_provider["Provider ID"]
        ]

        if night_candidates:
            night_provider = random.choice(night_candidates)
        else:
            night_provider = day_provider

        # Assign the appropriate time period and status.
        if current_date < date.today():
            time_period = "Historical"
            schedule_status = "Completed"
        elif current_date == date.today():
            time_period = "Current"
            schedule_status = "Active"
        else:
            time_period = "Future"
            schedule_status = "Scheduled"

        # Create exact day-shift timestamps.
        day_start_datetime = datetime.combine(
            current_date,
            day_shift_start,
        )

        day_end_datetime = datetime.combine(
            current_date,
            day_shift_end,
        )

        # Create exact night-shift timestamps.
        night_start_datetime = datetime.combine(
            current_date,
            night_shift_start,
        )

        night_end_datetime = datetime.combine(
            current_date + timedelta(days=1),
            night_shift_end,
        )

        # Create the day-shift record.
        day_record = {
            "Schedule ID": f"SCH{schedule_number:05}",
            "Date": current_date,
            "Day of Week": current_date.strftime("%A"),
            "Time Period": time_period,
            "Department": department,
            "Shift": "Day",
            "Start Date/Time": day_start_datetime,
            "End Date/Time": day_end_datetime,
            "Shift Length": 12,
            "Provider ID": day_provider["Provider ID"],
            "Schedule Status": schedule_status,
        }

        schedule_records.append(day_record)
        schedule_number += 1

        # Create the night-shift record.
        night_record = {
            "Schedule ID": f"SCH{schedule_number:05}",
            "Date": current_date,
            "Day of Week": current_date.strftime("%A"),
            "Time Period": time_period,
            "Department": department,
            "Shift": "Night",
            "Start Date/Time": night_start_datetime,
            "End Date/Time": night_end_datetime,
            "Shift Length": 12,
            "Provider ID": night_provider["Provider ID"],
            "Schedule Status": schedule_status,
        }

        schedule_records.append(night_record)
        schedule_number += 1

    current_date += timedelta(days=1)


# =====================================================
# Convert Schedule Records Into a DataFrame
# =====================================================

schedule_df = pd.DataFrame(schedule_records)


# =====================================================
# Export the Raw Data Workbook
# =====================================================

# This raw-data file is separate from the manually designed
# Healthcare_OnCall_Dashboard.xlsx workbook.

output_file = "Healthcare_OnCall_Raw_Data.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl",
) as writer:
    providers_df.to_excel(
        writer,
        sheet_name="Providers",
        index=False,
    )

    schedule_df.to_excel(
        writer,
        sheet_name="Schedule",
        index=False,
    )


# =====================================================
# Display Completion Message
# =====================================================

print(f"{output_file} has been created successfully!")
print(f"Providers created: {len(providers_df)}")
print(f"Schedule records created: {len(schedule_df)}")
