# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    heap = [(0, i) for i in range(n_workers)]
    heapq.heapify(heap)
    result = []
    for job in jobs:
        next_free_time, worker = heapq.heappop(heap)
        result.append(AssignedJob(worker, next_free_time))
        heapq.heappush(heap, (next_free_time+job, worker))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
