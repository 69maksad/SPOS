# First Come First Serve Scheduling in Python

def main():
    n = int(input("Enter Number of Processes: "))
    process = list(range(1, n + 1))
    arrivaltime = []
    burstTime = []
    completionTime = [0] * n
    TAT = [0] * n
    waitingTime = [0] * n
    avgtat = 0
    avgwt = 0

    for i in range(n):
        arrivaltime.append(int(input(f"\nEnter Arrival Time for process {process[i]}: ")))
        burstTime.append(int(input(f"Enter Burst Time for process {process[i]}: ")))

    # Sort processes based on arrival time
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arrivaltime[i] > arrivaltime[j]:
                arrivaltime[i], arrivaltime[j] = arrivaltime[j], arrivaltime[i]
                burstTime[i], burstTime[j] = burstTime[j], burstTime[i]
                process[i], process[j] = process[j], process[i]

    # Calculate completion time
    for i in range(n):
        if i == 0:
            completionTime[i] = arrivaltime[i] + burstTime[i]
        else:
            completionTime[i] = max(completionTime[i - 1], arrivaltime[i]) + burstTime[i]

    # Display results
    print("\n*** First Come First Serve Scheduling ***")
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    print("-" * 80)

    for i in range(n):
        TAT[i] = completionTime[i] - arrivaltime[i]
        waitingTime[i] = TAT[i] - burstTime[i]
        avgtat += TAT[i]
        avgwt += waitingTime[i]
        print(f"P{process[i]}\t\t{arrivaltime[i]}ms\t\t{burstTime[i]}ms\t\t{completionTime[i]}ms\t\t{TAT[i]}ms\t\t{waitingTime[i]}ms")

    print(f"\nAverage Turnaround Time: {avgtat / n}ms")
   
