import json

import zmq


def search_villagers(search_term):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send the search term to the server
    socket.send_string(search_term)

    # Receive and print the search results
    search_results = socket.recv_json()
    print(json.dumps(search_results, indent=2))


if __name__ == "__main__":
    search_term = input("Enter search term (species or personality type): ")
    search_villagers(search_term)
