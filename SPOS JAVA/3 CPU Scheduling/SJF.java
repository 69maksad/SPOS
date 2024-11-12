def main():
    print("*** Shortest Job First Scheduling (Preemptive) ***")
    n = int(input("Enter number of processes: "))
    
    process = [0] * n
    arrival_time = [0] * n
    burst_time = [0] * n
    completion_time = [0] * n
    TAT = [0] * n
    waiting_time = [0] * n
    visit = [0] * n
    rem_burst_time = [0] * n
    
    total = 0
    avg_wt = 0
    avg_TAT = 0
    start = 0

    for i in range(n):
        print("")
        process[i] = i + 1
        arrival_time[i] = int(input(f"Enter Arrival Time for process {i + 1}: "))
        burst_time[i] = int(input(f"Enter Burst Time for process {i + 1}: "))
        rem_burst_time[i] = burst_time[i]
        visit[i] = 0

    # Sorting processes based on arrival time
    for i in range(n):
        for j in range(n):
            if arrival_time[i] < arrival_time[j]:
                process[i], process[j] = process[j], process[i]
                arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                rem_burst_time[i], rem_burst_time[j] = rem_burst_time[j], rem_burst_time[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]

    while True:
        min_burst = float('inf')
        c = n
        if total == n:
            break
        
        for i in range(n):
            if (arrival_time[i] <= start) and (visit[i] == 0) and (burst_time[i] < min_burst):
                min_burst = burst_time[i]
                c = i

        if c == n:
            start += 1
        else:
            burst_time[c] -= 1
            start += 1
            if burst_time[c] == 0:
                completion_time[c] = start
                visit[c] = 1
                total += 1

    for i in range(n):
        TAT[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = TAT[i] - rem_burst_time[i]
        avg_wt += waiting_time[i]
        avg_TAT += TAT[i]

    print("\n*** Shortest Job First Scheduling (Preemptive) ***")
    print("Processor\tArrival time\tBurst time\tCompletion Time\tTurn around time\tWaiting time")
    print("----------------------------------------------------------------------------------------------------------")
    
    for i in range(n):
        print(f"P{process[i]}\t\t{arrival_time[i]}ms\t\t{rem_burst_time[i]}ms\t\t"
              f"{completion_time[i]}ms\t\t\t{TAT[i]}ms\t\t\t{waiting_time[i]}ms")

    avg_TAT /= n
    avg_wt /= n

    print(f"\nAverage turn around time is {avg_TAT:.2f}ms")
    print(f"Average waiting time is {avg_wt:.2f}ms")


if __name__ == "__main__":
    main()