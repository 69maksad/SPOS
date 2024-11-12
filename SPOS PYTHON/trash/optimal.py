def optimal_page_replacement():
    no_of_pages = int(input("Enter the number of pages you want to enter: "))
    pages = []

    print("Enter the page numbers:")
    for i in range(no_of_pages):
        page = int(input())
        pages.append(page)

    capacity = int(input("Enter the capacity of frame: "))
    frame = []
    table = [[-1] * capacity for _ in range(no_of_pages)]  # Table to store the frame status

    hit = 0
    fault = 0

    print("\n----------------------------------------------------------------------")
    for i in range(no_of_pages):
        page = pages[i]

        # Check if page is already in the frame (page hit)
        if page in frame:
            hit += 1
            print(f"{'H':>4}", end="")
        else:
            fault += 1
            # If the frame is not full, simply append the page
            if len(frame) < capacity:
                frame.append(page)
            else:
                # Find the page that will not be used for the longest period in the future
                farthest = -1
                index_to_replace = 0
                for j in range(len(frame)):
                    if frame[j] not in pages[i+1:]:
                        index_to_replace = j
                        break
                    else:
                        next_use = pages[i+1:].index(frame[j]) + i + 1
                        if next_use > farthest:
                            farthest = next_use
                            index_to_replace = j

                # Replace the chosen page
                frame[index_to_replace] = page
            print(f"{'F':>4}", end="")

        # Update table for current state of the frame
        for j in range(len(frame)):
            table[i][j] = frame[j]

    print("\n----------------------------------------------------------------------")

    # Display the page frame table
    for i in range(capacity):
        for j in range(no_of_pages):
            print(f"{table[j][i]:>3}", end=" ")
        print()

    print("----------------------------------------------------------------------")
    
    # Calculate hit ratio and fault ratio
    fault_ratio = (fault / no_of_pages) * 100
    hit_ratio = (hit / no_of_pages) * 100

    print(f"Page Faults: {fault}\nPage Hits: {hit}")
    print(f"Hit Ratio: {hit_ratio:.2f}%\nFault Ratio: {fault_ratio:.2f}%")

# Run the function
optimal_page_replacement()