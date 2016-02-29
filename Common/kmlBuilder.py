import simplekml 
from Helpers import helpers


class kml():


    def __init__(self):
        print helpers.color("[*] Started KML", bold=False)
        self.points = []
        kml = simplekml.Kml()

    def build(self): #Pass SSID name
        #Build the instance
        # kml = simplekml.Kml()
        #If you pass description data, place it into the point.
        kml.save("output.kml")

    def buildPoints(self, ssid, geo_lat, geo_long, desc_data=""):
        # Build the list of points
        #start the Point data.
        pnt = kml.newpoint(name=ssid, coords=[(geo_lat, geo_long)])  # lon, lat, optional height
        if desc_data != "":
            pnt.description = desc_data






    

