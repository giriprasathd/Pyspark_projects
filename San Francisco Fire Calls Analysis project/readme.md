# San Francisco Fire Calls Analysis

## Project Overview

This project aims to analyze fire call data from San Francisco using PySpark. The dataset contains information about various fire incidents reported in the city, including their types, response times, and the neighborhoods they occurred in. The analysis provides insights into trends and patterns related to fire calls, which can be valuable for fire departments and urban planners.

## Dataset

The dataset used for this project is `sf-fire-calls.csv`, which contains the following columns:

- `CallNumber`: Unique identifier for the call
- `UnitID`: Identifier for the responding unit
- `IncidentNumber`: Unique incident number
- `CallType`: Type of call (e.g., fire, medical, etc.)
- `CallDate`: Date of the call
- `WatchDate`: Date when the call was assigned
- `CallFinalDisposition`: Final disposition of the call
- `AvailableDtTm`: Timestamp when the unit became available
- `Address`: Address of the incident
- `City`: City of the incident
- `Zipcode`: Zip code of the incident location
- `Battalion`: Battalion responsible for the incident
- `StationArea`: Area of the fire station
- `Box`: Box number for the call
- `OriginalPriority`: Original priority of the call
- `Priority`: Current priority of the call
- `FinalPriority`: Final priority of the call
- `ALSUnit`: Indicates if an ALS unit was dispatched
- `CallTypeGroup`: Grouping of call types
- `NumAlarms`: Number of alarms called
- `UnitType`: Type of responding unit
- `UnitSequenceInCallDispatch`: Sequence number of the unit in the dispatch
- `FirePreventionDistrict`: District for fire prevention
- `SupervisorDistrict`: Supervisor district
- `Neighborhood`: Neighborhood where the call occurred
- `Location`: Geographical location of the incident
- `RowID`: Row identifier
- `Delay`: Delay in response time

## Analysis Questions

The following questions were addressed in this analysis:

1. What are all the different types of fire in the call types?
2. How many fire calls in 2018 were categorized as "medical incidents"?
3. What were all the different types of fire calls in 2018?
4. Which neighborhood in San Francisco generated the most fire calls in 2018?
5. Which neighborhoods had the worst response times to fire calls in 2018?
6. What was the average response time for fire calls in each neighborhood in 2018?
7. How many fire calls were handled by ALS units versus non-ALS units in 2018?
8. What were all the different unit types?
9. Is there a correlation between neighborhood, zip code, and number of fire calls?
10. Which year had the most fire calls?
11. How many alarms were called during fire incidents?
12. How many fire calls in 2018 required more than one alarm?
13. How many fire calls required five alarms?
14. What is the trend in the number of non-life-threatening fire calls over the years?
15. How can we use SQL tables to store this data and read it back?

## Setup Instructions

1. **Install PySpark**: Ensure you have PySpark installed in your Python environment. You can install it using pip:
   ```
   pip install pyspark
   ```
2. **Prepare the Dataset**: Download the sf-fire-calls.csv dataset and place it in the project directory.
3. **Run the Notebook**: Open the Jupyter Notebook or your preferred IDE and run the provided code to analyze the dataset.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
