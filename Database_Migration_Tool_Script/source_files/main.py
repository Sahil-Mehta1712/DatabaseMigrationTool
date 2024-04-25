import os
import sys
from supportedDatabases import supportedDatabases
from writeDbScript import writeDbScript
from writeCSVScript import writeCSVScript
from runDBScript import runDBScript
from databaseConnector import databaseConnector
from runBCP import runBCP

def readInputData():
#{
	global srcDatabaseType
	global tgtDatabaseType
	global databaseIdentifier
	global tableName
	
	print ("Enter the task number for the task to be executed: ")
	print("1. Generate Database Scripts")
	print("2. Generate CSV Files")
	print("3. Create Tables in Target Database")
	print("4. Import data from CSV files to target Database")
	print("0. Exit")
	
	while True:
	#{
		try:
		#{
			option = int(input("Enter Task number:"))
			break
		#}
		except ValueError:
		#{
			print ('*' * 120)
			print("No Option has been entered.")
			print ('*' * 120)
		#}
	#}
	selectedOption(option)
#}

def selectedOption(option):
#{
	srcDatabaseList,tgtDatabaseList = supportedDatabases()
	srcDatabases = ','.join(srcDatabaseList)
	tgtDatabases = ','.join(tgtDatabaseList)
	
	if option == 1:
	#{
		print ('*' * 120)
		print ("Generate Database Scripts")
		print("Leave spaces between table names if multiple entries to be made")
		print ('*' * 120)
		
		while True:
		#{
			print("Valid Source Databases include: " + srcDatabases)
			print ('*' * 120)
			srcDatabaseType = input("Source Database Type (Mandatory): ")
			print ('*' * 120)
			if srcDatabaseType == "":
			#{
				print("Enter a Source Database")
				continue
			#}
			elif srcDatabaseType.lower() not in srcDatabaseList:
			#{
				print("Incorrect Source Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			print("Valid Target Databases include: " + tgtDatabases)
			print ('*' * 120)
			tgtDatabaseType = input("Target Database Type (Mandatory): ")
			print ('*' * 120)
			if tgtDatabaseType == "":
			#{
				print("Enter a Target Database")
				continue
			#}
			elif tgtDatabaseType.lower() not in tgtDatabaseList:
			#{
				print ("Incorrect Target Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			databaseIdentifier = input("Database Identifier (Mandatory): ")
			print ('*' * 120)
			if databaseIdentifier == "":
			#{
				print("Enter Database Identifier")
				print ('*' * 120)
				continue
			#}
			else:
			#{
				break
			#}
		#}

		tmpTableName = input("Table name: ")
		print ('*' * 120)
		tableNameList = tmpTableName.split()
		
		conn =  databaseConnector(srcDatabaseType,databaseIdentifier)
		writeDbScript(srcDatabaseType,tgtDatabaseType,databaseIdentifier,tableNameList,conn)
		conn.close()
		
	#}
	elif option == 2:
	#{
		print ('*' * 120)
		print ("Generate CSV Scripts")
		print("Leave spaces between table names if multiple entries to be made")
		print ('*' * 120)
		
		while True:
		#{
			print("Valid Source Databases include: " + srcDatabases)
			print ('*' * 120)
			srcDatabaseType = input("Source Database Type (Mandatory): ")
			print ('*' * 120)
			if srcDatabaseType == "":
			#{
				print("Enter a Source Database")
				continue
			#}
			elif srcDatabaseType.lower() not in srcDatabaseList:
			#{
				print("Incorrect Source Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			print("Valid Target Databases include: " + tgtDatabases)
			print ('*' * 120)
			tgtDatabaseType = input("Target Database Type (Mandatory): ")
			print ('*' * 120)
			if tgtDatabaseType == "":
			#{
				print("Enter a Target Database")
				continue
			#}
			elif tgtDatabaseType.lower() not in tgtDatabaseList:
			#{
				print ("Incorrect Target Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			databaseIdentifier = input("Database Identifier (Mandatory): ")
			print ('*' * 120)
			if databaseIdentifier == "":
			#{
				print("Enter Database Identifier")
				print ('*' * 120)
				continue
			#}
			else:
			#{
				break
			#}
		#}
		
		tmpTableName = input("Table name: ")
		tableNameList = tmpTableName.split()
		print ('*' * 120)
		
		conn =  databaseConnector(srcDatabaseType,databaseIdentifier)
		writeCSVScript(srcDatabaseType,tgtDatabaseType,databaseIdentifier,tableNameList,conn)
		conn.close()
	#}
	elif option == 3:
	#{
		print ('*' * 120)
		print ("Create Tables in Target Database")
		print ("Leave spaces between table names if multiple entries to be made")
		print ('*' * 120)
		
		while True:
		#{
			print("Valid Target Databases include: " + tgtDatabases)
			print ('*' * 120)
			tgtDatabaseType = input("Target Database Type (Mandatory): ")
			print ('*' * 120)
			if tgtDatabaseType == "":
			#{
				print("Enter a Target Database")
				continue
			#}
			elif tgtDatabaseType.lower() not in tgtDatabaseList:
			#{
				print ("Incorrect Target Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			databaseIdentifier = input("Database Identifier (Mandatory): ")
			print ('*' * 120)
			if databaseIdentifier == "":
			#{
				print("Enter Database Identifier")
				print ('*' * 120)
				continue
			#}
			else:
			#{
				break
			#}
		#}
		
		tmpTableName = input("Table name: ")
		tableNameList = tmpTableName.split()
		print ('*' * 120)
		
		conn =  databaseConnector(tgtDatabaseType,databaseIdentifier)
		runDBScript(tgtDatabaseType,databaseIdentifier,tableNameList,conn)
		conn.close()
	#}
	elif option == 4:
	#{
		print ('*' * 120)
		print ("Import data from CSV files to target Database")
		print ("Leave spaces between table names if multiple entries to be made")
		print ('*' * 120)
		
		while True:
		#{
			print("Valid Target Databases include: " + tgtDatabases)
			print ('*' * 120)
			tgtDatabaseType = input("Target Database Type (Mandatory): ")
			print ('*' * 120)
			if tgtDatabaseType == "":
			#{
				print("Enter a Target Database")
				continue
			#}
			elif tgtDatabaseType.lower() not in tgtDatabaseList:
			#{
				print ("Incorrect Target Database Entered")
				continue
			#}
			else:
			#{
				break
			#}
		#}
		while True:
		#{
			databaseIdentifier = input("Database Identifier (Mandatory): ")
			print ('*' * 120)
			if databaseIdentifier == "":
			#{
				print("Enter Database Identifier")
				print ('*' * 120)
				continue
			#}
			else:
			#{
				break
			#}
		#}
		tmpTableName = input("Table name: ")
		tableNameList = tmpTableName.split()
		
		runBCP(tgtDatabaseType,databaseIdentifier,tableNameList)
	#}
	elif option == 0:
	#{
		print ('*' * 120)
		print("You have exited Successfully")
		print ('*' * 120)
		sys.exit(0)
	#}
	else:
	#{
		print ('*' * 120)
		print("Invalid Option has been selected.")
		print("Valid options include 1,2,3,4 and 0")
		print ('*' * 120)
		readInputData()
	#}
#}

if __name__ == '__main__':
	readInputData()