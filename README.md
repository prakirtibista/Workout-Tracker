# Workout Tracker

This is a Python-based workout tracker that integrates with the [Nutritionix API](https://www.nutritionix.com/business/api) to track exercises and the [Sheety API](https://sheety.co/) to log workouts in a Google Sheet. The app allows users to input their exercise activity, retrieve nutritional data (such as calories burned), and log the exercise details such as calories burned, duration, and more.

## Features

- Track workouts: Log exercises by providing a query (e.g., "walked for 1 hour").
- Nutritional data: Fetch calories burned, exercise duration, and other related data from the Nutritionix API.
- Sheety API integration: Send workout details (date, time, exercise, duration, and calories burned) to a Google Sheet using the Sheety API.

## Requirements

- Python 3.x
- `dotenv` module (for loading environment variables)
- `requests` module (for making API requests)

## Setup

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/workout-tracker.git
cd workout-tracker
```

## Install Dependencies

python -m venv .venv
# On Windows
.venv\Scripts\activate

## Setup environment variables

SHEETY_TOKEN=<Your_Sheety_API_Token>
APP_ID=<Your_Nutritionix_APP_ID>
APP_KEY=<Your_Nutritionix_APP_KEY>
NUTRITION_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise
SHEETY_URL=https://api.sheety.co/691cfc9c37be42a9ae53eb475a297c86/copyOfMyWorkouts/workouts
WEIGHT=<Your_weight>
AGE=<Your_age>
HEIGHT=<Your_height>

## Run the script

```bash
python3 main.py
```

## Input Exercise

When prompted, enter the exercise you performed (e.g., "walked for 1 hour"). The app will fetch nutritional data for that exercise and log the details in your Google Sheet.

## Example Output

```
What exercise did you do? walked for 1 hour
```

## Contributing

Feel free to fork the project, create a branch, make your changes, and create a pull request. Contributions are welcome!



