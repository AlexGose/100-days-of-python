import requests
import os
import datetime

PIXELA_API_KEY = os.getenv("PIXELA_API_KEY")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_RECORD_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}"


def get_option():
    option_message = "1 Add a new pixel\n2 Update an old pixel\n3 Delete an old pixel" \
                     + "\n\nEnter an option (1-3): "
    option = int(input(option_message))
    if option not in [1,2,3]:
        raise ValueError(f"Option {option} is not a valid option")
    return option


def date_str(days_ago):
    if days_ago < 0:
        raise ValueError(f"{days_ago} days ago is negative and must be positive.")
    date_days_ago = datetime.datetime.now() - datetime.timedelta(days=days_ago)
    return date_days_ago.strftime('%Y%m%d')


def get_update_endpoint(date_string):
    return f"{PIXELA_RECORD_ENDPOINT}/{date_string}"


def get_date_str():
    days_ago = int(input('How many days ago? (Examples: 0, 1, 2, etc.): '))
    if days_ago < 0:
        raise ValueError(f"{days_ago} days ago is negative and must be positive")
    return (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime('%Y%m%d')


def get_quantity():
    quantity = input('What is the quantity? ')
    if float(quantity) < 0:
        raise ValueError(f'quantity {quantity} is negative and must be positive')
    return quantity


if __name__ == '__main__':
    headers = {
        "X-USER-TOKEN": PIXELA_API_KEY
    }

    try:
        option = get_option()
        if option == 1:
            parameters = {
                'date': get_date_str(),
                'quantity': get_quantity()
            }
            response = requests.post(url=PIXELA_RECORD_ENDPOINT, json=parameters, headers=headers)
        elif option == 2:
            date_str = get_date_str()
            parameters = {
                'date': date_str,
                'quantity': get_quantity()
            }
            response = requests.put(url=get_update_endpoint(date_str), json=parameters, headers=headers)
        elif option == 3:
            response = requests.delete(url=get_update_endpoint(get_date_str()), headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(e)
