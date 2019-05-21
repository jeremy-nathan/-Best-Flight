import gmplot

gmap2 = gmplot.GoogleMapPlotter.from_geocode( "Dehradun, India" )
gmap2.draw("map2.html")
