<img align=left src="map.gif" width=300/><br clear=left>
## Where in the world is the International Space Station (ISS) ?

### Objectives
- Use the requests package to query real-world data
- Improve skills with dictionaries and indexing
- Learn about the built-in Python [Turtle](https://docs.python.org/3.3/library/turtle.html?highlight=turtle) graphics library

### Part A
Using this public API, write a python program to obtain a list of the astronauts who are currently in space.  Print their full names, the spacecraft they are currently on board, and the total number of astronauts in space.
> [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json)

### Part B
Using another public API, obtain the current geographic coordinates (lat/lon) of the space station, along with a timestamp.
> [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)

### Part C
With the [turtle](https://docs.python.org/2/library/turtle.html) graphics library (part of standard Python), create a graphics screen with the world map background image.  Use turtle methods such as `Screen`, `setup`, `bgpic`, `setworldcoordinates`.  Register an icon image for the ISS station within the turtle screen context, and create a `turtle.Turtle()` context to move the ISS station to its current lat/lon on the map.  Use methods such as `shape`, `setheading`, `penup`, and `goto`.

### Part D
Find out the next time that the ISS will be overhead of Indianapolis IN.  Use our geographic lat/lon to plot a yellow dot on the map.  Use this public API to query the next pass:
>[http://api.open-notify.org/iss-pass.json](http://api.open-notify.org/iss-pass.json)

You will need to supply the lat/lon coordinates as query parameters to this url.  The passover times are returned as timestamps, so you will need to use the `time.ctime()` method to convert them to human-readable text.  Render the next passover time next to the Indianapolis location dot that you plotted earlier.
