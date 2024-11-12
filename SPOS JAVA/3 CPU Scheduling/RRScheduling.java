from collections import deque

class Process:
    def __init__(self, process_id, arrival, burst):
        self.process_id = process_id
        self.arrival = arrival
        self.burst = burst
        self.remaining_time = burst
        self.finish = 0
        self.completion_time = 0
        self.waiting = 0
        self.turn_around = 0

def main():
    print("*** RR Scheduling (Preemptive) ***")
    n = int(input("Enter Number of Processes: "))
    processes = []

    sum_burst = 0

    for i in range(n):
        arrival = int(input(f"Enter the arrival time for P{i + 1}: "))
        burst = int(input(f"Enter the burst time for P{i + 1}: "))
        processes.append(Process(i + 1, arrival, burst))
        sum_burst += burst
        print()

    quantum = int(input("Enter time quantum: "))
    
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival)

    q = deque()
    q.append(0)  # Start with the first process
    time = processes[0].arrival

    while time < sum_burst:
        i = q.popleft()
        if processes[i].remaining_time <= quantum:
            time += processes[i].remaining_time
            processes[i].remaining_time = 0
            processes[i].finish = 1
            processes[i].completion_time = time
            processes[i].waiting = time - processes[i].arrival - processes[i].burst
            processes[i].turn_around = time - processes[i].arrival
            
            # Add new processes to the queue
            for j in range(n):
                if processes[j].arrival <= time and processes[j].finish != 1 and j not in q:
                    q.append(j)
        else:
            time += quantum
            processes[i].remaining_time -= quantum
            
            # Add new processes to the queue
            for j in range(n):
                if processes[j].arrival <= time and processes[j].finish != 1 and i != j and j not in q:
                    q.append(j)
            q.append(i)  # Re-add the current process to the queue

    # Display results
    print("\n*** RR Scheduling (Preemptive) ***")
    print("Processor\tArrival time\tBurst time\tCompletion Time\tTurn around time\tWaiting time")
    print("-" * 100)
    
    avg_wt = 0
    avg_tat = 0
    
    for p in processes:
        print(f"P{p.process_id}\t\t{p.arrival}ms\t\t{p.burst}ms\t\t{p.completion_time}ms\t\t\t{p.turn_around}ms\t\t\t{p.waiting}ms")
        avg_wt += p.waiting
        avg_tat += p.turn_around

    print(f"\nAverage turn around time of processor: {avg_tat / n:.2f}ms")
    print(f"Average waiting time of processor: {avg_wt / n:.2f}ms")

if __name__ == "__main__":
    main()