from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_name_and_price(soup):
    """
    Extracts the name and price of a car from the given BeautifulSoup object.

    Parameters:
    - soup: A BeautifulSoup object representing the HTML content of a car page.

    Returns:
    - output: A dictionary containing the extracted car name and price.
              The keys are 'car_name' and 'car_price'.
    """
    output = {}  # Initialize an empty dictionary to store the extracted data
    car_name = soup.find("h1").text  # Find the car name and extract the text
    output["car_name"] = car_name  # Add the car name to the dictionary
    car_price = soup.find(
        "div", class_="price"
    ).text  # Find the car price and extract the text
    output["car_price"] = car_price.split("*")[0]  # Add the car price to the dictionary
    return output  # Return the dictionary containing the extracted data


def get_data_from_table(table):
    """
    Extracts data from a table from a BeautifulSoup object.

    Args:
        table (BeautifulSoup): The BeautifulSoup object representing the table.

    Returns:
        dict: A dictionary containing the extracted data from the table.
    """
    data = {}  # Initialize an empty dictionary to store the data
    rows = table.find_all("tr")  # Find all rows in the table
    for row in rows:  # Loop through the rows
        columns = row.find_all("td")  # Find all columns in the row
        if len(columns) < 2:  # Skip rows with less than 2 columns
            continue
        # Loop through the columns and extract the data
        key = columns[0].text.strip()  # Extract the key from the first column
        value_column = columns[1]  # Get the second column as the value column
        if value_column.find(
            "i", class_="icon-deletearrow"
        ):  # Check if the value is "No"
            value = "No"
        elif value_column.find("i", class_="icon-check"):  # Check if the value is "Yes"
            value = "Yes"
        else:
            value = value_column.text.strip()

        data[key] = value  # Add the key-value pair to the dictionary
    return data


def get_soup(url, session):
    """
    Retrieves the BeautifulSoup object for a given URL using the provided session.

    Args:
        url (str): The URL to retrieve the HTML from.
        session (requests.Session): The session object to use for making the HTTP request.

    Returns:
        BeautifulSoup: The BeautifulSoup object representing the parsed HTML.
    """
    # Adding the user agent to avoid the 403 forbidden error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    session.headers.update(headers)  # Update the session headers
    response = session.get(url)  # Make the HTTP GET request
    if response.status_code != 200:
        raise Exception(
            f"Invalid car details provided. Please check the car company and model."
        )
    soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML content

    return soup  # Return the BeautifulSoup object
