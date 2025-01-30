import requests
import json


def get_access_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": "",
        "client_secret": "",
    }
    url = ""  # like mc2399af9poaporlqfwch-x2ad0.
    response = requests.post(
        f"https://{url}.auth.marketingcloudapis.com/v2/token", json=payload
    )

    print(response)

    response.raise_for_status()
    return response.json()["access_token"]


# Controlla lo stato di un bulk data load
def check_bulk_data_load_status(job_id):
    access_token = get_access_token()
    print(access_token)
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    url = ""  # like mc2399af9poaporlqfwch-x2ad0.
    url = f"https://{url}.rest.marketingcloudapis.com/data/v1/async/{job_id}/results"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = [
        '{"requestId":"nqwn2367-aca7-r31qw-1242-90cdqwqwffccf","resultMessages":[]}'
    ]
    parsed_data = [json.loads(item)['requestId'] for item in data]

    for el in parsed_data:
        status = check_bulk_data_load_status(el)
        print(json.dumps(status, indent=4))
