class NonPriorityScheduling:

    def main(self):
        print("*** Priority Scheduling (Non Preemptive) ***")

        n = int(input("Enter Number of Processes: "))
        process = list(range(1, n + 1))
        arrival_time = [0] * n
        burst_time = [0] * n
        completion_time = [0] * n
        priority = [0] * n
        TAT = [0] * n
        waiting_time = [0] * n
        arrival_time_copy = [0] * n
        burst_time_copy = [0] * n

        for i in range(n):
            print("")
            arrival_time[i] = int(input(f"Enter Arrival Time for process {i + 1}: "))
            burst_time[i] = int(input(f"Enter Burst Time for process {i + 1}: "))
            priority[i] = int(input(f"Enter Priority for process {i + 1}: "))

        # Sort processes based on arrival time and priority
        for i in range(n - 1):
            for j in range(i + 1, n):
                if arrival_time[i] > arrival_time[j] or (arrival_time[i] == arrival_time[j] and priority[j] > priority[i]):
                    # Swap process
                    process[i], process[j] = process[j], process[i]
                    # Swap arrival times
                    arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                    # Swap burst times
                    burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                    # Swap priorities
                    priority[i], priority[j] = priority[j], priority[i]

        # Copy original arrays for processing
        arrival_time_copy = arrival_time[:]
        burst_time_copy = burst_time[:]

        total_time = sum(burst_time)
        min_arrival_time = min(arrival_time)
        total_time += min_arrival_time

        tLap = min_arrival_time
        current_index = 0
        while tLap < total_time:
            min_index = None
            for i in range(n):
                if arrival_time_copy[i] <= tLap:
                    if min_index is None or priority[i] < priority[min_index]:
                        min_index = i
            if min_index is not None:
                tLap += burst_time_copy[min_index]
                completion_time[min_index] = tLap
                priority[min_index] = float('inf')  # Mark as processed

        # Calculate TAT and Waiting Time
        avg_TAT = 0
        avg_WT = 0
        print("\nPriority Scheduling (Non Preemptive)")
        print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        print("-" * 100)

        for i in range(n):
            TAT[i] = completion_time[i] - arrival_time[i]
            waiting_time[i] = TAT[i] - burst_time[i]
            avg_TAT += TAT[i]
            avg_WT += waiting_time[i]
            print(f"P{process[i]}\t\t{arrival_time[i]}ms\t\t{burst_time[i]}ms\t\t"
                  f"{completion_time[i]}ms\t\t{TAT[i]}ms\t\t{waiting_time[i]}ms")

        avg_WT /= n
        avg_TAT /= n
        print(f"\nAverage Waiting Time: {avg_WT:.2f}ms")
        print(f"Average Turnaround Time: {avg_TAT:.2f}ms")


if __name__ == "__main__":
    scheduler = NonPriorityScheduling()
    scheduler.main()