# ACO_GA_Code

This repository contains Python code for solving the Vehicle Routing Problem with Time Windows (VRPTW) using Ant Colony Optimization (ACO) and Genetic Algorithm (GA).

## Overview

The VRPTW is a combinatorial optimization problem where a fleet of vehicles must deliver goods to a set of customers within specified time windows. This code implements a solution using a combination of ACO and GA.

## Code Structure

- `iterUpdate.py`: Module for visualization purposes.
- `objFcn.py`: Objective function calculation and path information classes.
- `vehicleUpdate.py`: Ant class for updating vehicles and local search.
- `ACOGA.py`: Main module combining ACO and GA to solve VRPTW.

## How to Use

### Dependencies

Ensure you have the following Python libraries installed:

- `numpy`
- `matplotlib`

### Running the Code

1. Clone the repository:

   ```bash
   git clone https://github.com/jaikeerthy/ACO_GA_Code.git

   Navigate to the project directory:

bash
Copy code
cd ACO_GA_Code
Run the code:

bash
Copy code
python ACOGA.py
Customization
Adjust parameters in the acoGA_Fcn class constructor in ACOGA.py to fit your specific problem instance.
Modify the code to read your own data if needed.
Visualization
Enable visualization by setting whether_or_not_to_show_figure=True in the acoGA_Fcn class constructor.
