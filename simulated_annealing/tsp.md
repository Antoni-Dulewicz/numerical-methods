<font size="6">
Solving TSP (Traveling-Salesman-Problem) using simulated anealing algorithm:
</font>

<br>
<font size="2">
<a href="README.md" style="color: purple">CLICK HERE TO RETURN TO SIMULATED ANNEALING PAGE</a>
</font>
<br>
<br>
We will consider 3 types of generating points:
<br>
<font size="3">
<ol>
<li>Using random.uniform() function</li>
<li>Using random.multivariate_normal() function</li>
<li>Randomly generating points in 9 clusters</li>
</ol> 
</font>
<br>

Energy function is defined as the total distance of the route. The algorithm will try to minimize this energy function.

Multiple highs and lows in the energy and temperature plot are due to the reheat functionality. 

<br>
<font size="5">

Using random.uniform() function:
</font>
<font size="3">

This is the energy plot for the solution:

![energy](tsp/images_for_md/uniform/energy_plot.png)

Temperature plot for the solution:

![temperature](tsp/images_for_md//uniform/temparature_plot.png)

Final solution:

![solution](tsp/images_for_md/uniform/gif_output.gif)

</font>

<font size="5">

Using random.multivariate_normal function:
</font>

<font size="3">
 This is the energy plot for the solution:

![energy](tsp/images_for_md/normal/energy_plot.png)

Temperature plot for the solution:

![temperature](tsp/images_for_md/normal/temparature_plot.png)

Final solution:

![solution](tsp/images_for_md/normal/gif_output.gif)

</font>

<font size="5">

Randomly generating points in 9 clusters
</font>

<font size="3">
 This is the energy plot for the solution:

![energy](tsp/images_for_md/clusters/energy_plot.png)

Temperature plot for the solution:

![temperature](tsp/images_for_md/clusters/temparature_plot.png)

Final solution:

![solution](tsp/images_for_md/clusters/gif_output.gif)

</font>

<a href="README.md" style="color: purple">CLICK HERE TO RETURN TO SIMULATED ANNEALING PAGE</a>
