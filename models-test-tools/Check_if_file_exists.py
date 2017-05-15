
#**********************************************************************
# Description:
# Tests if a field exists and outputs two booleans:
#   Exists - true if the field exists, false if it doesn't exist
#   Not_Exists - true if the field doesn't exist, false if it does exist
#                (the logical NOT of the first output).
#
# Arguments:
#  0 - Table name
#  1 - Exists (boolean - see above)
#  2 - Not_Exists (boolean - see above)
#
# Created by: ESRI
#**********************************************************************

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Get input arguments - table name
#
in_Table = gp.GetParameterAsText(0)

# Branch depending on whether table exists. Issue a
#  message, and then set our two output variables accordingly
#
if not gp.Exists(in_Table):
	gp.SetParameterAsText(1, "False")
	gp.SetParameterAsText(2, "True")
else:
	gp.SetParameterAsText(1, "True")
	gp.SetParameterAsText(2, "False")

