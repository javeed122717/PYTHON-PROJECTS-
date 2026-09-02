# CIT Student Forecast

## Objective
Forecast the number of students joining Chennai Institute of Technology for
the next five academic years using a small, transparent machine-learning model.

## Model
Linear Regression trained on the most recent five observations (2021-22 to
2025-26). The model uses academic year as the predictor.

## Historical target data
- 2015-16 to 2021-22: actual first-year UG admissions reported in NIRF.
- 2022-23 to 2025-26: proxy joiners because a consistent public series of final
  first-year admissions was not available.

Proxy formula:
    approved UG intake × TNEA Round-1 seat-fill rate

The proxy values are estimates and must not be presented as official final
admission counts.

## Forecast
2026-27: 2,717
2027-28: 3,140
2028-29: 3,563
2029-30: 3,985
2030-31: 4,408

Training R² on 2021-22 to 2025-26 = 0.891.

## Enrollment comparison
Enrollment is a different metric from new joiners, so it is shown separately.

2022-23: 3,673 total students
2023-24: 4,480 total students
2024-25: 6,187 total students

The latest official NIRF 2026 student-strength disclosure corresponds to
2024-25; it should not be described as 2025-26 enrollment.

## Files
- cit_student_dataset.csv
- cit_5_year_forecast.csv
- cit_enrollment_comparison.csv
- cit_forecast.py
- cit_joining_forecast.png
- cit_enrollment_trend.png
