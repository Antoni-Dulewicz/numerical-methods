<font size="6">
What is simulated annealing?
</font>
<br>
<font size="1">
<a href="../README.md" style="color: purple">CLICK HERE TO RETURN TO THE MAIN PAGE</a>
</font>

But first, lets find out **for what problems we can use simulated annealing**:


CLICK HERE TO FIND OUT -> <a href="europe_trip.md" style="color: orange;text-decoration: underline;">TRIP TO EUROPE</a>

**In this repository I implemented the simulated annealing algorithm to solve:** 
<ol>
<li><a href="tsp.md" style="color: orange;text-decoration: underline;">The traveling salesman problem (TSP).</a></li>
<li><a href="binary.md" style="color: orange;text-decoration: underline;">Generating binary images.</a></li>
<li><a href="sudoku.md" style="color: orange;text-decoration: underline;">Sudoku Solver</a></li>
</ol> 

Simulated annealing is a probabilistic technique used for finding an approximate solution to an optimization problem. To find the solution to a problem, it explores the solution space by randomly selecting a solution and then accepting or rejecting it based on a probability distribution function. The probability distribution function is determined by the current temperature and the difference between the current solution and the new solution. The temperature is gradually decreased over time, which allows the algorithm to escape local minima and explore the solution space more thoroughly. Simulated annealing is inspired by the process of annealing in metallurgy, where a material is heated and then slowly cooled to increase its strength and reduce defects. Similarly, in simulated annealing, the algorithm starts with a high temperature and then gradually cools down to find the optimal solution to the problem.

**Each of the implementations will return**:
<ol>
<li>Temperature plot</li>
<li>Energy plot</li>
<li>Final solution.</li>
</ol> 

In all implementations I added functionality to reheat the system if the algorithm gets stuck in a local minimum. This allows the algorithm to escape the local minimum and continue exploring the solution space. This is how this functionality works:

```python
Iteration 1170000, temparature: 0.8293333983735268, current score: 4.496138392658936  Best score: 4.488657169538599
Program is stuck - rehating from: 0.8187118407659479 to: 8.18711840765948
Iteration 1180000, temparature: 7.504115156672787, current score:13.01670172044894  Best score: 4.488657169538599
```

ENJOY!

<a href="../README.md" style="color: purple">CLICK HERE TO RETURN TO THE MAIN PAGE</a>
