class OptimalPageReplacement:
    def main(self):
        noofpages = int(input("Enter the number of pages you want to enter: "))
        pages = []

        # Read pages one by one
        print("Enter the pages one by one:")
        for _ in range(noofpages):
            page = int(input())
            pages.append(page)

        capacity = int(input("Enter the capacity of frame: "))
        frame = [-1] * capacity
        table = [[0] * capacity for _ in range(noofpages)]
        ptr = 0
        hit = 0
        fault = 0
        isFull = False

        print("----------------------------------------------------------------------")
        for i in range(noofpages):
            search = -1
            for j in range(capacity):
                if frame[j] == pages[i]:
                    search = j
                    hit += 1
                    print("H", end=" ")
                    break
            if search == -1:
                if isFull:
                    index = [0] * capacity
                    index_flag = [False] * capacity
                    for j in range(i + 1, noofpages):
                        for k in range(capacity):
                            if (pages[j] == frame[k]) and (not index_flag[k]):
                                index[k] = j
                                index_flag[k] = True
                                break

                    max_index = index[0]
                    ptr = 0
                    if max_index == 0:
                        max_index = 200  # Arbitrary large number
                    for j in range(capacity):
                        if index[j] == 0:
                            index[j] = 200
                        if index[j] > max_index:
                            max_index = index[j]
                            ptr = j

                frame[ptr] = pages[i]
                fault += 1
                print("F", end=" ")
                if not isFull:
                    ptr += 1
                    if ptr == capacity:
                        ptr = 0
                        isFull = True

            # Copy current frame state to table
            table[i] = frame.copy()

        print("\n----------------------------------------------------------------------")
        for i in range(capacity):
            for j in range(noofpages):
                print(f"{table[j][i]:3d}", end=" ")
            print()

        print("----------------------------------------------------------------------")
        hitRatio = (hit / noofpages) * 100
        faultRatio = (fault / noofpages) * 100
        print(f"Page Fault: {fault}\nPage Hit: {hit}")
        print(f"Hit Ratio: {hitRatio:.2f} \nFault Ratio: {faultRatio:.2f}")

if __name__ == "__main__":
    opr = OptimalPageReplacement()
    opr.main()