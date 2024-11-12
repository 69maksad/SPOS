class LeastRecentlyUsed:
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
        arr = []
        hit = 0
        fault = 0
        index = 0
        isFull = False

        print("----------------------------------------------------------------------")
        for i in range(noofpages):
            if pages[i] in arr:
                arr.remove(pages[i])
                arr.append(pages[i])
                hit += 1
                print("H", end=" ")
            else:
                if isFull:
                    min_loc = noofpages
                    for j in range(capacity):
                        if frame[j] in arr:
                            temp = arr.index(frame[j])
                            if temp < min_loc:
                                min_loc = temp
                                index = j
                frame[index] = pages[i]
                fault += 1
                print("F", end=" ")
                index += 1
                if index == capacity:
                    index = 0
                    isFull = True
                arr.append(pages[i])

        print("\n----------------------------------------------------------------------")
        for i in range(capacity):
            for j in range(noofpages):
                if j < len(frame):
                    print(f"{frame[j]:3d}", end=" ")
                else:
                    print("   ", end="")
            print()

        print("----------------------------------------------------------------------")
        hitRatio = (hit / noofpages) * 100
        faultRatio = (fault / noofpages) * 100
        print(f"Page Fault: {fault}\nPage Hit: {hit}")
        print(f"Hit Ratio: {hitRatio:.2f} \nFault Ratio: {faultRatio:.2f}")

if __name__ == "__main__":
    lru = LeastRecentlyUsed()
    lru.main()