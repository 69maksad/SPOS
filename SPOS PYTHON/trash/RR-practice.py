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

# Round Robin (Preemptive)
def round_robin(processes, time_quantum):
    time = 0
    queue = [p for p in processes if p.arrival_time <= time]
    completed = 0
    n = len(processes)
    while completed < n:
        if queue:
            process = queue.pop(0)
            if process.remaining_time > time_quantum:
                time += time_quantum
                process.remaining_time -= time_quantum
            else:
                time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed += 1
            # Add new processes that have arrived up to the current time
            for p in processes:
                if p.arrival_time <= time and p.remaining_time > 0 and p not in queue and p != process:
                    queue.append(p)
            # Re-add the current process if it has remaining time
            if process.remaining_time > 0:
                queue.append(process)
        else:
            time += 1
            # Add any new processes that have arrived at the current time
            for p in processes:
                if p.arrival_time <= time and p.remaining_time > 0 and p not in queue:
                    queue.append(p)
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
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i+1}: "))
        burst_time = int(input(f"Enter burst time for Process {i+1}: "))
        priority = int(input(f"Enter priority for Process {i+1} (optional, enter 0 if not applicable): "))
        processes.append(Process(i+1, arrival_time, burst_time, priority))

    # Time Quantum Input
    time_quantum = int(input("Enter time quantum for Round Robin scheduling: "))

    # Round Robin Scheduling
    rr_result = round_robin(processes, time_quantum)
    display_results(rr_result, f"Round Robin (Time Quantum = {time_quantum})")
