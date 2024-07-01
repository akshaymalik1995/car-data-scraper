import requests  # Import the requests library to make HTTP requests
from utils import (
    get_soup,
    get_data_from_table,
    extract_name_and_price,
)  # Import the helper functions
from pathlib import (
    Path,
)  # Import the Path class from the pathlib module to work with file paths

# Prompt the user to enter the slug of the car. Show the user an example of the slug format
print(
    "Enter the details of the car. For example, for https://www.cardekho.com/mahindra/thar, the car company is 'mahindra' and the car model is 'thar'"
)
car_company = input("Enter the car company: ")  # Get the car company from the user
car_model = input("Enter the car model: ")  # Get the car model from the user

if not car_company or not car_model:  # Check if the car company or car model is empty
    print("Please enter a valid car company and model")  # Print an error message
    exit()

car_slug = (
    f"{car_company}/{car_model}"  # Combine the car company and model to form the slug
)

# URL of the website
car_url = f"https://www.cardekho.com/{car_slug}"  # URL of the car page
car_specs_url = f"{car_url}/specs"  # URL of the car specs page

session = requests.Session()  # Create a session object to persist the cookies

car_page = None  # Initialize the car page to None
car_specs_page = None  # Initialize the car specs page to None

try:
    # Get the car page and car specs page
    car_page = get_soup(car_url, session)  # Get the car page
    car_specs_page = get_soup(car_specs_url, session)  # Get the car specs page
except Exception as e:  # Catch any exceptions that occur during the request
    print(f"Error getting the car page: {e}")  # Print the error message
    exit()  # Exit the program


output = {}  # Initialize the output dictionary to store the extracted data

# Extract the name and price of the car
car_data = {}
try:
    car_data = extract_name_and_price(car_page)
    for key, value in car_data.items():
        output[key] = value
except Exception as e:
    print(f"Error extracting car name and price: {e}")


try:  # Extract the key specs of the car
    key_specs_tables = car_specs_page.find("div", id="technicalSpecsTop").find_all(
        "table"
    )  # Find all tables in the key specs section

    for table in key_specs_tables:  # Loop through the tables
        data = get_data_from_table(table)  # Get the data from the table
        for key, value in data.items():  # Loop through the data
            output[key] = value  # Add the key and value to the output dictionary
except Exception as e:  # Catch any exceptions that occur during extraction of key specs
    print(f"Error extracting key specs: {e}")  # Print the error message


try:
    specs_table = car_specs_page.find("section", id="technicalSpecs").find_all(
        "table"
    )  # Find all tables in the technical specs section

    for table in specs_table:  # Loop through the tables
        # Delete certain div tags
        for div in table.find_all("div", class_="tooltipDesc"):
            div.decompose()  # Remove the div tag from the table

        data = get_data_from_table(table)  # Get the data from the table
        for key, value in data.items():  # Loop through the data
            output[key] = value  # Add the key and value to the output dictionary

except Exception as e:  # Catch any exceptions that occur during extraction of specs
    print(f"Error extracting specs: {e}")  # Print the error message


try:
    # Get the root path of the project
    cwd = Path(__file__).parent

    output_file = Path.joinpath(
        cwd, f"{car_data['car_name']}.csv"
    )  # Create the file path

    with open(output_file, "w", newline="") as csvfile:  # Open the file in write mode
        csvfile.write("NAME,VALUE\n")  # Write the header row
        for key, value in output.items():  # Loop through the output dictionary
            csvfile.write(
                f"{key},{value.replace(',' , ' | ')}\n"
            )  # Write the key and value to the file
    print(f"Output saved to {output_file}")  # Print the success message

except Exception as e:  # Catch any exceptions that occur during file writing
    print(f"Error saving the output to a file: {e}")  # Print the error message
