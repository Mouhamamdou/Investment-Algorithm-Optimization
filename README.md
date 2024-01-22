# Investment Algorithm Optimization Project

## Description

This project was developed for AlgoInvest&Trade, aimed at optimizing investment strategies using algorithms. It includes a brute force solution (bruteforce.py) and an optimized algorithm version (optimized.py) to select the most profitable stocks within a defined budget constraint.

## Components

1. bruteforce.py: A Python script implementing a brute force approach to find the most profitable combination of stocks under the given constraints.
2. optimized.py: An optimized version of the algorithm, designed for larger datasets and quicker execution times.
3. Presentation Slides: A set of slides explaining the analysis of both algorithms, their comparative performance, and the data exploration report comparing the algorithm outputs with historical investment decisions.

## Installation

To run these scripts, you need Python 3.x installed on your system. No additional libraries are required.

    ```bash
     https://github.com/Mouhamamdou/Investment-Algorithm-Optimization.git
     cd Investment-Algorithm-Optimization

## Usage

Run the scripts via the command line:

    ```bash
    python bruteforce.py
    python optimized.py


## Data Format

The scripts expect input data in the following format:

. Action name

. Cost per action (in Euros)

. Profit percentage after two years

## Constraints

. Each action can only be purchased once.

. No fractional action purchases.

. Maximum spending limit of 500 Euros per client.

## Algorithme Overview

. Brute Force (bruteforce.py): Iterates over all possible combinations of stocks and selects the one with the highest profit within the budget constraint. This method ensures the identification of the absolute best combination but can be inefficient for large datasets due to its exponential time complexity.

. Optimized Algorithm (optimized.py): Implements a greedy approach for faster execution suitable for larger datasets. The algorithm selects stocks based on the best profit at each step, aiming to maximize overall profit without exceeding the budget limit. This approach significantly improves the execution time while still providing a near-optimal solution.

## Performance Analysis

The brute force algorithm guarantees an optimal solution but is inefficient for larger datasets due to its exponential time complexity.

The greedy algorithm, while not always guaranteeing the absolute best solution, offers a significant improvement in execution time, making it a more practical choice for larger datasets and real-time applications.
