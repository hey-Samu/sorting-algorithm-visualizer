
import time


def bubble_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    start_time = time.perf_counter()

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        print(f"Pass {i + 1}: {arr}")
        time.sleep(0.2)

        if not swapped:
            break

    end_time = time.perf_counter()

    print("\n--- Bubble Sort Results ---")
    print("Sorted array:", arr)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print(f"Execution time: {(end_time - start_time) * 1000:.4f} milliseconds")
    print("Best-case time complexity: O(n)")
    print("Average-case time complexity: O(n^2)")
    print("Worst-case time complexity: O(n^2)")


def selection_sort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    start_time = time.perf_counter()

    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i + 1}: {arr}")
        time.sleep(0.2)

    end_time = time.perf_counter()

    print("\n--- Selection Sort Results ---")
    print("Sorted array:", arr)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print(f"Execution time: {(end_time - start_time) * 1000:.4f} milliseconds")
    print("Best-case time complexity: O(n^2)")
    print("Average-case time complexity: O(n^2)")
    print("Worst-case time complexity: O(n^2)")


def insertion_sort(arr):
    arr = arr.copy()
    comparisons = 0
    shifts = 0

    start_time = time.perf_counter()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

        print(f"Pass {i}: {arr}")
        time.sleep(0.2)

    end_time = time.perf_counter()

    print("\n--- Insertion Sort Results ---")
    print("Sorted array:", arr)
    print("Comparisons:", comparisons)
    print("Shifts:", shifts)
    print(f"Execution time: {(end_time - start_time) * 1000:.4f} milliseconds")
    print("Best-case time complexity: O(n)")
    print("Average-case time complexity: O(n^2)")
    print("Worst-case time complexity: O(n^2)")


def main():
    print("=" * 45)
    print("       SORTING ALGORITHM VISUALIZER")
    print("=" * 45)

    while True:
        print("\nChoose a sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "4":
            print("Thank you for using the Sorting Visualizer!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please select 1, 2, 3, or 4.")
            continue

        try:
            user_input = input(
                "Enter numbers separated by spaces: "
            ).strip()

            if not user_input:
                print("Please enter at least one number.")
                continue

            arr = list(map(int, user_input.split()))

            if len(arr) > 30:
                print("Please enter a maximum of 30 numbers.")
                continue

            print("\nOriginal array:", arr)
            print("\nSorting in progress...\n")

            if choice == "1":
                bubble_sort(arr)
            elif choice == "2":
                selection_sort(arr)
            elif choice == "3":
                insertion_sort(arr)

        except ValueError:
            print("Invalid input! Please enter integers only.")

        print("\n" + "-" * 45)


if __name__ == "__main__":
    main()
