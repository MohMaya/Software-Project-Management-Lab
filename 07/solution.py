# Write a program to implement
#      COCOMO II

#### NOTES ####

# Revised Version of Original COCOMO
# Includes 3 Stages : 
#   1. Application Composition Estimation
#   2. Early Design Estimation
#   3. Post-Architecture Estimation

# DETAILED INFO

# 1. Application Composition Estimation
#
# @ Focuses on those applications which can be developed quickly using interoperable components
# Ex. GUI, Database, Control Packages for specific domains
#   Can also be used during prototyping phase of a project
# STEPS : 
#       1. Assess object counts - Estimate no. of screens, reports, 3GL Components
#       2. Classify complexity level of each object into Simple Medium Difficult    
#               Screens on the basis of # of Views + Sources
#               Reports on the basis of # of Sections + Sources
#       3. Assign Complexity weight to each object. i.e. Weight for each screen based on its no. of sources
#                       classify 3GL components as always difficult
#       4. Add all these complexity weights to get total object points count
#       5. Compute new object points by involving re-usable component
#                       NOP = (ObjectPoints)*(100-reusable%)/100
#       6. Calculate Productivity Rate (PROD) - Calculated from past project data 
#                       PROD = NOP/Person-Months        [Get PROD from the table]
#       7. Hence Final Effort in Person Months : NOP/PROD

#   PS : THE TABLES ARE PROVIDED IN THE SS IN THE SAME FOLDER


