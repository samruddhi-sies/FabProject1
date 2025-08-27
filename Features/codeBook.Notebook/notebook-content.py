# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "77af8710-4855-46ba-9e78-707d8533619d",
# META       "default_lakehouse_name": "dataHouse1",
# META       "default_lakehouse_workspace_id": "0a2d977a-355b-4c78-b1a2-eeb7f4a62ef4",
# META       "known_lakehouses": [
# META         {
# META           "id": "77af8710-4855-46ba-9e78-707d8533619d"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
Print('Hello')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("abfss://FeatureWsp@onelake.dfs.fabric.microsoft.com/dataHouse1.Lakehouse/Files/sales.csv")
# df now is a Spark DataFrame containing CSV data from "abfss://FeatureWsp@onelake.dfs.fabric.microsoft.com/dataHouse1.Lakehouse/Files/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
