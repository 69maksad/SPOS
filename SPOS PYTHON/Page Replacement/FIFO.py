def main():
    noofpages = int(input("Enter the number of pages you want to enter: "))
    pages = []

    for _ in range(noofpages):
        pages.append(int(input()))

    capacity = int(input("Enter the capacity of frame: "))
    frame = [-1] * capacity
    table = [[0] * capacity for _ in range(noofpages)]

    index = 0
    hit = 0
    fault = 0

    print("\n----------------------------------------------------------------------")
    for i in range(noofpages):
        search = -1
        for j in range(capacity):
            if frame[j] == pages[i]:
                search = j
                hit += 1
                print(f"{'H':>4}", end="")
                break

        if search == -1:
            frame[index] = pages[i]
            fault += 1
            print(f"{'F':>4}", end="")
            index += 1
            if index == capacity:
                index = 0

        # Copy the current state of the frame to the table
        for j in range(capacity):
            table[i][j] = frame[j]

    print("\n----------------------------------------------------------------------")
    for i in range(capacity):
        for j in range(noofpages):
            print(f"{table[j][i]:>3}", end=" ")
        print()

    print("----------------------------------------------------------------------")
    faultRatio = (fault / noofpages) * 100
    hitRatio = (hit / noofpages) * 100
    print(f"Page Fault: {fault}\nPage Hit: {hit}")
    print(f"Hit Ratio: {hitRatio:.2f} \nFault Ratio: {faultRatio:.2f}")

if __name__ == "__main__":
    main()