import requests
import json

# Configurazione SFMC
ID_ORG = '' #like mqfay44mzvt...
CLIENT_ID = "" #like gqfau4n...
CLIENT_SECRET = "" #like qqfaq46...
AUTH_URL = f"https://{IDORG}.rest.auth.marketingcloudapis.com/v2/token"
BASE_URL = f"https://{IDORG}.rest.marketingcloudapis.com"
REQUEST_ID = "" #like c33e9722-28e5-4qfa24..

# Ottieni token di accesso
def get_access_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(AUTH_URL, json=payload)

    print(response)

    response.raise_for_status()
    return response.json()["access_token"]

# Controlla lo stato di un bulk data load
def check_bulk_data_load_status():
    access_token = get_access_token()
    print(access_token)
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    url = f"{BASE_URL}/data/v1/async/{REQUEST_ID}/results"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    status = check_bulk_data_load_status()
    print(json.dumps(status, indent=4))
