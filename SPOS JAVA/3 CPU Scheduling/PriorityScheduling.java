class PriorityScheduling:

    def main(self):
        print("*** Priority Scheduling (Preemptive) ***")
        n = int(input("Enter Number of Processes: "))
        
        process = list(range(1, n + 1))
        arrival_time = [0] * n
        burst_time = [0] * n
        completion_time = [0] * n
        priority = [0] * (n + 1)
        TAT = [0] * n
        waiting_time = [0] * n
        burst_time_copy = [0] * n
        
        for i in range(n):
            print("")
            arrival_time[i] = int(input(f"Enter Arrival Time for process {i + 1}: "))
            burst_time[i] = int(input(f"Enter Burst Time for process {i + 1}: "))
            priority[i] = int(input(f"Enter Priority for process {i + 1}: "))

        # Sorting processes based on arrival time and priority
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

        burst_time_copy = burst_time[:]
        priority[n] = float('inf')
        count = 0
        time = 0
        
        while count != n:
            min_index = n
            for i in range(n):
                if arrival_time[i] <= time and priority[i] < priority[min_index] and burst_time[i] > 0:
                    min_index = i
            
            if min_index < n:  # If a valid process is found
                burst_time[min_index] -= 1
                
                if burst_time[min_index] == 0:
                    count += 1
                    end = time + 1
                    completion_time[min_index] = end
                    waiting_time[min_index] = end - arrival_time[min_index] - burst_time_copy[min_index]
                    TAT[min_index] = end - arrival_time[min_index]
            time += 1

        avg_TAT = sum(TAT) / n
        avg_WT = sum(waiting_time) / n
        
        # Display results
        print("\n*** Priority Scheduling (Preemptive) ***")
        print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        print("-" * 100)

        for i in range(n):
            print(f"P{process[i]}\t\t{arrival_time[i]}ms\t\t{burst_time_copy[i]}ms\t\t"
                  f"{completion_time[i]}ms\t\t{TAT[i]}ms\t\t{waiting_time[i]}ms")

        print(f"\nAverage Waiting Time: {avg_WT:.2f}ms")
        print(f"Average Turnaround Time: {avg_TAT:.2f}ms")


if __name__ == "__main__":
    scheduler = PriorityScheduling()
    scheduler.main()