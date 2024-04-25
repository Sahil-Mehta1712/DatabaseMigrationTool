import os
import csv
import shutil
import sys
from getQuery import getQuery

def writeCSVScript(srcDatabase,tgtDatabase,databaseIdentifier,tableNameList,conn):
#{
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	csvFilePath = os.path.join(currentDirectory, "..")
	csvFilePath = os.path.join(csvFilePath, "..")
	csvFilePath = os.path.join(csvFilePath, "Generated_Scripts")
	csvFilePath = os.path.join(csvFilePath,tgtDatabase.lower())
	csvFilePath = os.path.join(csvFilePath,"csv_scripts")
	
	if os.path.exists(csvFilePath):
	#{
		shutil.rmtree(csvFilePath)
	#}
	os.makedirs(csvFilePath)
	
	cursor = conn.cursor()
	
	if tableNameList == []:
	#{
		tableQuery = getQuery(srcDatabase,'table')
		cursor.execute(tableQuery)
	
		for row_data in cursor:
		#{
			tableName = row_data[0]
			
			# writeCSVFile each table content to a separate CSV file
			csv_file_dest = csvFilePath + "/" + tableName.upper() + "_TMP.tsv"
			outputCSVFile = open(csv_file_dest,'w',newline='') # 'wb'
			writeCSVFile = csv.writer(outputCSVFile,delimiter = "\t")
			print("Creating CSV Script for " + tableName.upper())
			print ('*' * 120)
			dataQuery = getQuery(srcDatabase,'data')+ " " +tableName.upper()
			cursor1 = conn.cursor()
			cursor1.execute(dataQuery)
			
			for row_data in cursor1: # add table rows
			#{
				writeCSVFile.writerow(row_data)
			#}
		#}
		outputCSVFile.close()
	#}
	else:
	#{
		for tableName in tableNameList:
		#{	
			if tableName != '':
			#{
				tableQuery = getQuery(srcDatabase,'table') + " where table_name = '" + tableName.upper() + "'"
				cursor.execute(tableQuery)
				tableCheck = cursor.fetchall()
				try:
				#{
					if tableCheck == []:
					#{
						raise ValueError("Table Name does not exist in the given database. Please enter a valid Table Name.")
					#}
				#}
				except ValueError as ve:
				#{
					print(ve)
					sys.exit(1)
				#}
			#}
			else:
			#{
				tableQuery = getQuery(srcDatabase,'table')
			#}
			cursor.execute(tableQuery)
				
			for row_data in cursor:
			#{
				tableName = row_data[0]
				
				# writeCSVFile each table content to a separate CSV file
				csv_file_dest = csvFilePath + "/" + tableName.upper() + "_TMP.tsv"
				outputCSVFile = open(csv_file_dest,'w',newline='') # 'wb'
				writeCSVFile = csv.writer(outputCSVFile,delimiter = "\t")
				print("Creating CSV Script for " + tableName.upper())
				print ('*' * 120)
				dataQuery = getQuery(srcDatabase,'data')+ " " +tableName.upper()
				cursor1 = conn.cursor()
				cursor1.execute(dataQuery)
				
				for row_data in cursor1: # add table rows
				#{
					writeCSVFile.writerow(row_data)
				#}
			#}
			outputCSVFile.close()
	#}
	cursor.close()
#}