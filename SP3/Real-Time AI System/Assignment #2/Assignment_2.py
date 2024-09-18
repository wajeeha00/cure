import multiprocessing
import service_a
import service_b
 
def run_services(max_iterations):
    service_a_process = multiprocessing.Process(target=service_a.service_a, args=(max_iterations,))
    service_b_process = multiprocessing.Process(target=service_b.service_b, args=(max_iterations,))
 
    service_a_process.start()
    service_b_process.start()
 
    service_a_process.join()
    service_b_process.join()
 
if __name__ == "__main__":
    max_iterations = int(input("Enter the number of iterations: "))
    run_services(max_iterations)