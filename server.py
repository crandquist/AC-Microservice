import json

import zmq

# Load your villagers data from the JSON file.
with open('villagers.json', 'r') as file:
    villagers_data = json.load(file)


def search_villagers(search_term):
    results = [
        villager for villager in villagers_data
        if search_term.lower() in villager['species'].lower()
        or search_term.lower() in villager['personality'].lower()
    ]
    return results


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_string()
        print(f"Received search term: {message}")

        # Search for villagers based on the received search term
        search_results = search_villagers(message)

        # Send the results back as JSON
        socket.send_json(search_results)


if __name__ == "__main__":
    main()
