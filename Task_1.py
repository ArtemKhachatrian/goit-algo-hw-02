
from queue import Queue
from itertools import count

queue = Queue()
request_id = count(1)


def generate_request():
    request = f"request #{next(request_id)}"
    queue.put(request)
    print(f"Created: {request}")


def process_request():
    if queue.empty():
        print("Queue is empty")
    else:
        request = queue.get()
        print(f"Processing: {request}")


if __name__ == "__main__":
    while True:
        command = input("Press Enter for continue or q for logout: ")

        if command.lower() == "q":
            break

        generate_request()
        process_request()