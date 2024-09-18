from threading import Thread
import queue

class IncrementThread(Thread):

    def __init__(self, increment_to_square, square_to_increment, A, MAX_ITER):

        super().__init__()
        self.increment_to_square = increment_to_square
        self.square_to_increment = square_to_increment
        self.A = A
        self.MAX_ITER = MAX_ITER

    def run(self):

        for _ in range(self.MAX_ITER):
            X = self.increment_to_square.get() #The thread stops here until it gets a value from the other function in the array
            X = (self.A * X) + 1  
            print(f"Increment Thread X = {X}") 
            self.square_to_increment.put(X)  #pushing to queue
class SquareThread(Thread):

    def __init__(self, square_to_increment, increment_to_square, A, MAX_ITER):

        super().__init__()
        self.square_to_increment = square_to_increment
        self.increment_to_square = increment_to_square
        self.A = A
        self.MAX_ITER = MAX_ITER

    def run(self):

        for _ in range(self.MAX_ITER):
            X = self.square_to_increment.get() # The thread stops here until it gets a value from the other Thread
            X = self.A * X  
            X = X * X
            print(f"Square Thread X = {X}")
            self.increment_to_square.put(X)  # pushing to queue

def main():

    A = 2
    B = 6 
    MAX_ITER = int(input("Enter the Number of Iterations: "))

    increment_to_square = queue.Queue()
    square_to_increment = queue.Queue()

    # storing initial value in the first queue
    increment_to_square.put(B)

    increment_thread = IncrementThread(increment_to_square, square_to_increment, A, MAX_ITER)
    square_thread = SquareThread(square_to_increment, increment_to_square, A, MAX_ITER)

    increment_thread.start()
    square_thread.start()

    # waiting for both threads to finish
    increment_thread.join()
    square_thread.join()

    print("Processing complete.")

if __name__ == "__main__":
    main()
