def main():
    n = int(input("Enter Number of Processes: "))
    process = list(range(1, n + 1))
    arrival_time = []
    burst_time = []
    completion_time = [0] * n
    TAT = [0] * n
    waiting_time = [0] * n
    total_tat = 0
    total_wt = 0

    # Input arrival and burst times
    for i in range(n):
        arrival_time.append(int(input(f"\nEnter Arrival Time for process {process[i]}: ")))
        burst_time.append(int(input(f"Enter Burst Time for process {process[i]}: ")))

    # Sort processes based on arrival time
    processes = sorted(zip(arrival_time, burst_time, process), key=lambda x: x[0])
    arrival_time, burst_time, process = zip(*processes)

    # Calculate completion time
    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = max(completion_time[i - 1], arrival_time[i]) + burst_time[i]

    # Display results
    print("\n*** First Come First Serve Scheduling ***")
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    print("-" * 80)

    for i in range(n):
        TAT[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = TAT[i] - burst_time[i]
        total_tat += TAT[i]
        total_wt += waiting_time[i]
        print(f"P{process[i]}\t\t{arrival_time[i]}ms\t\t{burst_time[i]}ms\t\t{completion_time[i]}ms\t\t{TAT[i]}ms\t\t{waiting_time[i]}ms")

    print(f"\nAverage Turnaround Time: {total_tat / n:.2f}ms")
    print(f"Average Waiting Time: {total_wt / n:.2f}ms")

if __name__ == "__main__":
    main()