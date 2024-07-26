# Sorting-Algorithms

This repository contains implementations of various sorting algorithms in Python. Each algorithm is implemented in its own Python file for clarity and ease of use.

## Table of Contents

- [Bubble Sort](#bubble-sort)
- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)
- [Quicksort](#quicksort)
- [Selection Sort](#selection-sort)

## Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

File: `Bubble_Sort.py`

## Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

File: `Insertion_Sort.py`

## Merge Sort

Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

File: `Merge_Sort.py`

## Quicksort

Quicksort is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. Developed by Tony Hoare in 1959, it is still a commonly used algorithm for sorting.

File: `Quicksort.py`

## Selection Sort

Selection Sort is an in-place comparison sorting algorithm. It has an O(n²) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort.

File: `Selection_Sort.py`

## Usage

Each file can be run individually to see the sorting algorithm in action. Simply execute the Python file from the command line:

```bash
python Bubble_Sort.py
