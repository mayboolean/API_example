import requests
import time
QUERIES = ["Great Wall of China", "Petra", "Colosseum",
            "Chichen Itza", "Machu Picchu", "Taj Mahal", "Christ the Redeemer"
]
def main():
    dict = {}
    for q in QUERIES:
        response = get_response(q)
        if response:
            dict[q] = response
    print(dict)
    return dict

def get_response(q, retries=3, delay=2):
    path = "https://us1.locationiq.com/v1/search.php"
    API_KEY = "......"

    query_params = {
        "key": API_KEY,
        "q": q,
        "format": "json"
    }

    for attempt in range(retries):
        try:
            response = requests.get(path, params=query_params)

            response_body = response.json()

            # Access the first element directly
            lat = response_body[0]['lat']
            lon = response_body[0]['lon']
            return {"latitude": lat, "longitude": lon}

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {q}: {e}")
        
        except (KeyError, IndexError) as e:
            print(f"Unexpected data format for {q}: {e}. Retrying...")

        time.sleep(delay)  # Wait before retrying in case of API issues

    return None  # Return None after retries are exhausted

main()