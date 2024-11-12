class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.remaining_time = burst_time

# Priority Scheduling (Non-Preemptive)
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

    return processes


# Helper function to calculate averages
def calculate_averages(processes):
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    total_waiting_time = sum(p.waiting_time for p in processes)
    n = len(processes)
    
    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    
    return avg_turnaround_time, avg_waiting_time


# Helper function to display the results
def display_results(processes, algorithm_name):
    print(f"\n{algorithm_name}:")
    print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for process in processes:
        print(f"{process.pid:<10}{process.arrival_time:<10}{process.burst_time:<10}{process.priority:<10}{process.completion_time:<15}{process.turnaround_time:<15}{process.waiting_time:<10}")

    avg_turnaround_time, avg_waiting_time = calculate_averages(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


if __name__ == "__main__":
    processes = [
        Process(1, 0, 8, 3),
        Process(2, 1, 4, 1),
        Process(3, 2, 9, 4),
        Process(4, 3, 5, 2),
    ]

    # Priority Scheduling
    priority_result = priority_scheduling(processes.copy())
    display_results(priority_result, "Priority Scheduling (Non-Preemptive)")