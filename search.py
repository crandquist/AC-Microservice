import zmq
import json


def search_villagers(search_term):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send the search term to the server
    socket.send_string(search_term)

    # Receive the search results
    search_results = socket.recv_json()
    return search_results


if __name__ == "__main__":
    while True:
        search_term = input("Enter search term (species or personality type, 'exit' to quit): ")

        if search_term.lower() == 'exit':
            break

        # Search for villagers based on the entered term
        results = search_villagers(search_term)

        # Display the search results
        if not results:
            print("No matching villagers found.")
        else:
            print("\nMatching villagers:")
            for result in results:
                print(json.dumps(result, indent=2))
            print("\n")
