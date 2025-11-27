import multiprocessing
import time

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} finished")

if __name__ == "__main__":
    # Create processes
    p1 = multiprocessing.Process(target=task, args=("A",))
    p2 = multiprocessing.Process(target=task, args=("B",))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("All tasks finished")
