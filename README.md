# Animal Crossing Villager Search Microservice

This microservice allows you to search for Animal Crossing villagers based on species or personality type.

## Prerequisites

- Python 3.x
- ZeroMQ (pyzmq)

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/crandquist/AC-Microservice
    cd ac-microservice
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Microservice (Server):

    ```bash
    python server.py
    ```

    The microservice will start listening for search requests on `tcp://localhost:5555`.

4. Run the Search Program:

    ```bash
    python search.py
    ```

    The search program will prompt you to enter search terms and display matching villagers.

    - To exit the search program, enter 'exit'.

## Customization

- Replace the `villagers.json` file with your own villagers' data in the specified format.
- Modify the search logic in `server.py` to meet your specific requirements.

## Additional Notes

- This microservice is a demonstration and may require further customization for production use.
- Ensure the microservice is running before using the search program or client.

## Acknowledgments

- [ZeroMQ](https://zeromq.org/)
- [Animal Crossing Data Source](https://nookipedia.com/wiki/Main_Page)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
