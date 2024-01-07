# ------------------------------------------------------
# Generating database with trivia questions
# ------------------------------------------------------

# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
import requests
# ------------------------------------------------------

# ------------------------------------------------------
# Set variables
# ------------------------------------------------------
# Set params as in https://opentdb.com/api_config.php after generating the API URL
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 17,
}
# ------------------------------------------------------

# ------------------------------------------------------
# Obtain data from a web page
# ------------------------------------------------------
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
# ------------------------------------------------------
