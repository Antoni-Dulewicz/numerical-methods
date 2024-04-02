<font size="6">
Generating binary images using simulated annealing
</font>
<br>
<font size="2">
<a href="README.md" style="color: purple">CLICK HERE TO RETURN TO SIMULATED ANNEALING PAGE</a>
</font>

We will consider 3 types of energy functions for generating binary images:
<br>
<font size="3">
<ol>
<li>Counting the four neighbours of pixel with the same colour</li>
<li>Counting the eight neighbours of pixel with the same colour</li>
<li>Counting the 2-corner neighbours of pixel with the same colour</li>
<li>Counting the 4-corner neighbours of pixel with the same colour</li>
</ol> 
</font>

Multiple highs and lows in the energy and temperature plot are due to the reheat functionality. 

<br>
<font size="5">

**Using the four-neighbours energy function:**
</font>
<font size="3">

This is the energy plot for the solution:

![energy](binary_img/images_for_md/output_fours/energy_plot.png)

Temperature plot for the solution:

![temperature](binary_img/images_for_md/output_fours/temp_plot.png)

Final solution:

![solution](binary_img/images_for_md/output_fours/gif_output.gif)

</font>

<font size="5">

**Using the eight-neighbours energy function:**
</font>
<font size="3">

This is the energy plot for the solution:

![energy](binary_img/images_for_md/output_eights/energy_plot.png)

Temperature plot for the solution:

![temperature](binary_img/images_for_md/output_eights/temp_plot.png)

Final solution:

![solution](binary_img/images_for_md/output_eights/gif_output.gif)

</font>


<font size="5">

**Using the 2-corners energy function for smaller img:**
</font>
<font size="3">

This is the energy plot for the solution:

![energy](binary_img/images_for_md/output_corners_10/energy_plot.png)

Temperature plot for the solution:

![temperature](binary_img/images_for_md/output_corners_10/temp_plot.png)

Final solution:

![solution](binary_img/images_for_md/output_corners_10/gif_output.gif)

</font>


<font size="5">

**Using the 2-corners energy function for bigger img:**
</font>
<font size="3">

This is the energy plot for the solution:

![energy](binary_img/images_for_md/output_corners/energy_plot.png)

Temperature plot for the solution:

![temperature](binary_img/images_for_md/output_corners/temp_plot.png)

Final solution:

![solution](binary_img/images_for_md/output_corners/gif_output.gif)

</font>


<font size="5">

**Using the 4-corners energy function for bigger img:**
</font>
<font size="3">

This is the energy plot for the solution:

![energy](binary_img/images_for_md/output_4_corners/energy_plot.png)

Temperature plot for the solution:

![temperature](binary_img/images_for_md/output_4_corners/temp_plot.png)

Final solution:

![solution](binary_img/images_for_md/output_4_corners/gif_output.gif)

</font>

<font size="2">
<a href="README.md" style="color: purple">CLICK HERE TO RETURN TO SIMULATED ANNEALING PAGE</a>
</font>