"""
John Boren
In Class Assignment
2.4.19
"""

import arcpy
from arcpy import env

arcpy.env.overwriteOutput = True
env.workspace = "D:\\Home Work\\GeoSpatial\\HW_3"

out_dir = "\\Results"
facilities = "Exercise05\\facilities.shp"
parks = "Exercise05\\parks.shp"

outfile = env.workspace + out_dir + "facilities_parks.shp"

try:

    if arcpy.Exists(outfile):
        print "Warning: about to delete", outfile
        arcpy.Delete_management(outfile)
        print "Warning: deleted: ", outfile

    if arcpy.Exists(facilities):
        if arcpy.Exists(parks):
            print "\n\nCreating Clip of: \t\t", facilities
            print "\t\t\t\t\t\tand", parks
            print "\nCalled: ", outfile
            arcpy.Clip_analysis(facilities, parks, outfile)

        else:
            print "shp files do not exist"
    else:
        print "No such files"
except Exception as err:
    print err
    print type(err)
    print "Problem..."
    print arcpy.GetMessages()

