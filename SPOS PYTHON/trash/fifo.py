def fifo_page_replacement():
    no_of_pages = int(input("Enter the number of pages you want to enter: "))
    pages = []

    print("Enter the page numbers:")
    for i in range(no_of_pages):
        page = int(input())
        pages.append(page)

    capacity = int(input("Enter the capacity of frame: "))
    frame = [-1] * capacity  # Initialize frame with -1
    table = [[-1] * capacity for _ in range(no_of_pages)]  # Table to store the frame status

    hit = 0
    fault = 0
    index = 0

    print("\n----------------------------------------------------------------------")
    for i in range(no_of_pages):
        search = -1
        # Check if the page is already in the frame (page hit)
        for j in range(capacity):
            if frame[j] == pages[i]:
                search = j
                hit += 1
                print(f"{'H':>4}", end="")
                break
        
        # Page fault occurs if the page is not found in the frame
        if search == -1:
            frame[index] = pages[i]
            fault += 1
            print(f"{'F':>4}", end="")
            index = (index + 1) % capacity  # Circularly increment index
        
        # Copy current frame status to table for display
        for k in range(capacity):
            table[i][k] = frame[k]
    
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
fifo_page_replacement()