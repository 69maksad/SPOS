class NonSJF:

    def main(self):
        print("*** Shortest Job First Scheduling (Non Preemptive) ***")
        n = int(input("Enter number of processes: "))
        
        process = list(range(1, n + 1))
        arrival_time = [0] * n
        burst_time = [0] * n
        completion_time = [0] * n
        TAT = [0] * n
        waiting_time = [0] * n
        
        for i in range(n):
            print(" ")
            arrival_time[i] = int(input(f"Enter Arrival Time for process {i + 1}: "))
            burst_time[i] = int(input(f"Enter Burst Time for process {i + 1}: "))

        # Sort processes based on arrival time
        for i in range(n):
            for j in range(n):
                if arrival_time[i] < arrival_time[j]:
                    # Swap process
                    process[i], process[j] = process[j], process[i]
                    # Swap arrival times
                    arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                    # Swap burst times
                    burst_time[i], burst_time[j] = burst_time[j], burst_time[i]

        time = 0
        sum_waiting_time = 0
        comp_total = 0
        avg_wt = 0
        avg_tat = 0

        for k in range(n):
            time += burst_time[k]
            min_burst = burst_time[k]
            for i in range(k, n):
                if time >= arrival_time[i] and burst_time[i] < min_burst:
                    # Swap the process, arrival time, and burst time
                    process[k], process[i] = process[i], process[k]
                    arrival_time[k], arrival_time[i] = arrival_time[i], arrival_time[k]
                    burst_time[k], burst_time[i] = burst_time[i], burst_time[k]

        waiting_time[0] = 0
        for i in range(1, n):
            sum_waiting_time += burst_time[i - 1]
            waiting_time[i] = sum_waiting_time - arrival_time[i]
            avg_wt += waiting_time[i]

        for i in range(n):
            comp_total += burst_time[i]
            completion_time[i] = comp_total
            TAT[i] = comp_total - arrival_time[i]
            avg_tat += TAT[i]

        # Display results
        print("\n*** Shortest Job First Scheduling (Non Preemptive) ***")
        print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        print("-" * 100)

        for i in range(n):
            print(f"P{process[i]}\t\t{arrival_time[i]}ms\t\t{burst_time[i]}ms\t\t"
                  f"{completion_time[i]}ms\t\t{TAT[i]}ms\t\t{waiting_time[i]}ms")

        avg_tat /= n
        avg_wt /= n
        print(f"\nAverage Turnaround Time: {avg_tat:.2f}ms")
        print(f"Average Waiting Time: {avg_wt:.2f}ms")


if __name__ == "__main__":
    scheduler = NonSJF()
    scheduler.main()