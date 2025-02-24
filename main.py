import requests


def send_payload(resident_id, resident_room, pet_id, pet_name):
    # Replace with your web service URL
    url = "http://192.168.1.236:5000/api/receive"

    # Construct the JSON payload
    payload = {
        "resident_id": resident_id,
        "resident_room": resident_room,
        "pet_id": pet_id,
        "pet_name": pet_name
    }

    try:
        # Send a POST request with the JSON payload
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        print("Payload successfully sent!")
        print("Response:", response.json())
    except requests.exceptions.RequestException as error:
        print("Error sending payload:", error)


if __name__ == "__main__":
    # Example values; replace with your actual data
    send_payload("R001", "101", "P001", "Fluffy")

