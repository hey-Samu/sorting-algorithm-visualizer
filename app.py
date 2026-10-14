
import random
import time
import streamlit as st

st.set_page_config(
    page_title="Sorting Algorithm Visualizer",
    page_icon="📊",
    layout="wide"
)


# ---------------- SORTING ALGORITHMS ----------------

def bubble_sort(numbers):
    arr = numbers.copy()
    steps = []
    comparisons = 0
    swaps = 0

    start = time.perf_counter()

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        steps.append(arr.copy())

        if not swapped:
            break

    elapsed = (time.perf_counter() - start) * 1000
    return arr, steps, comparisons, swaps, elapsed


def selection_sort(numbers):
    arr = numbers.copy()
    steps = []
    comparisons = 0
    swaps = 0

    start = time.perf_counter()

    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        steps.append(arr.copy())

    elapsed = (time.perf_counter() - start) * 1000
    return arr, steps, comparisons, swaps, elapsed


def insertion_sort(numbers):
    arr = numbers.copy()
    steps = []
    comparisons = 0
    shifts = 0

    start = time.perf_counter()

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
        steps.append(arr.copy())

    elapsed = (time.perf_counter() - start) * 1000
    return arr, steps, comparisons, shifts, elapsed


# ---------------- USER INTERFACE ----------------

st.title("📊 Sorting Algorithm Visualizer")
st.write(
    "Explore how sorting algorithms arrange numbers "
    "step by step."
)

st.sidebar.header("⚙️ Settings")

algorithm = st.sidebar.selectbox(
    "Choose an algorithm",
    ["Bubble Sort", "Selection Sort", "Insertion Sort"]
)

speed = st.sidebar.slider(
    "Animation speed (seconds per step)",
    min_value=0.05,
    max_value=0.8,
    value=0.2,
    step=0.05
)

st.sidebar.info(
    "Bubble Sort: O(n²) average case\n\n"
    "Selection Sort: O(n²) average case\n\n"
    "Insertion Sort: O(n²) average case"
)

# Random number generator
if "numbers_input" not in st.session_state:
    st.session_state.numbers_input = "45, 12, 78, 23, 56, 9, 34"

if st.button("🎲 Generate Random Numbers"):
    random_numbers = [
        random.randint(1, 100)
        for _ in range(8)
    ]
    st.session_state.numbers_input = ", ".join(
        map(str, random_numbers)
    )

input_text = st.text_input(
    "Enter numbers separated by commas or spaces",
    key="numbers_input",
    help="Enter between 1 and 30 integers."
)

start_button = st.button(
    "▶️ Start Sorting",
    type="primary"
)

if start_button:
    try:
        numbers = list(
            map(
                int,
                input_text.replace(",", " ").split()
            )
        )

        if not numbers:
            st.error("Please enter at least one number.")

        elif len(numbers) > 30:
            st.error("Please enter a maximum of 30 numbers.")

        else:
            st.subheader("Original Array")
            st.write(numbers)

            if algorithm == "Bubble Sort":
                result = bubble_sort(numbers)
                complexity_best = "O(n)"
                complexity_average = "O(n²)"
                complexity_worst = "O(n²)"

            elif algorithm == "Selection Sort":
                result = selection_sort(numbers)
                complexity_best = "O(n²)"
                complexity_average = "O(n²)"
                complexity_worst = "O(n²)"

            else:
                result = insertion_sort(numbers)
                complexity_best = "O(n)"
                complexity_average = "O(n²)"
                complexity_worst = "O(n²)"

            sorted_arr, steps, comparisons, operations, elapsed = result

            st.subheader("Sorting Animation")

            chart_area = st.empty()
            progress_area = st.empty()

            # Display the original array first
            chart_area.bar_chart(
                {"Value": numbers},
                height=350
            )

            progress = st.progress(0)

            if steps:
                for index, current_step in enumerate(steps):
                    chart_area.bar_chart(
                        {"Value": current_step},
                        height=350
                    )

                    progress_area.caption(
                        f"Step {index + 1} of {len(steps)}"
                    )

                    progress.progress(
                        (index + 1) / len(steps)
                    )

                    time.sleep(speed)

            chart_area.bar_chart(
                {"Value": sorted_arr},
                height=350
            )

            progress_area.success("Sorting completed!")

            st.subheader("📈 Performance Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Comparisons",
                comparisons
            )

            col2.metric(
                "Swaps / Shifts",
                operations
            )

            col3.metric(
                "Execution Time",
                f"{elapsed:.4f} ms"
            )

            st.subheader("✅ Sorted Array")
            st.write(sorted_arr)

            st.subheader("⏱️ Theoretical Time Complexity")

            c1, c2, c3 = st.columns(3)

            c1.metric("Best Case", complexity_best)
            c2.metric("Average Case", complexity_average)
            c3.metric("Worst Case", complexity_worst)

            st.caption(
                "Execution time measures the sorting algorithm only. "
                "It excludes the animation delay. Actual time varies "
                "with the computer and input data."
            )

    except ValueError:
        st.error(
            "Invalid input! Enter integers separated by commas or spaces."
        )
