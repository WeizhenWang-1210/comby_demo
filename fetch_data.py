import requests

def fetch_data_from_api():
    """
    Fetch data from an external API using a GET request.
    """
    try:
        # Sending a GET request using requests.request (BAD)
        response = requests.request("get", "https://api.example.com/data", params={"key": "value"})

        # Check if the request was successful
        if response.status_code == 200:
            print("Data fetched successfully:")
            print(response.json())
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_data_from_api()
