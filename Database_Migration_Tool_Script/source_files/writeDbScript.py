import sys
import shutil
import os
from databaseConnector import databaseConnector
from getQuery import getQuery
from supportedDatabases import supportedDatabases
from createTableScript import *


def writeDbScript(srcDatabase,tgtDatabase,databaseIdentifier,tableNameList,conn):
#{
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	dbFilePath = os.path.join(currentDirectory, "..")
	dbFilePath = os.path.join(dbFilePath, "..")
	dbFilePath = os.path.join(dbFilePath, "Generated_Scripts")
	dbFilePath = os.path.join(dbFilePath,tgtDatabase.lower())
	dbFilePath = os.path.join(dbFilePath,"database_scripts")

	if os.path.exists(dbFilePath):
	#{
		shutil.rmtree(dbFilePath)
	#}
	os.makedirs(dbFilePath)
	
	cursor = conn.cursor()
	
	if tableNameList == []:
	#{
		tableQuery = getQuery(srcDatabase,'table')
		cursor.execute(tableQuery)
		
		for tables in cursor:
		#{
			table_name = tables[0]
			scriptPath = dbFilePath + "/" + table_name.upper() + "_TMP.sql"
			outputFile = open(scriptPath,'w')
			outputFile.write(createTableScript(srcDatabase,databaseIdentifier,table_name,conn))
			outputFile.write(primaryKeyCheck(srcDatabase,databaseIdentifier,table_name,conn))
			outputFile.write(uniqueKeyCheck(srcDatabase,databaseIdentifier,table_name,conn))
			outputFile.write(indexCheck(srcDatabase,databaseIdentifier,table_name,conn))
			print("Creating Database Script for " + table_name.upper())
			print ('*' * 120)
			outputFile.close()
			(foreignTemplate,foreignColumnCount) = foreignKeyCheck(srcDatabase,databaseIdentifier,table_name,conn)
			if foreignColumnCount != 0:
			#{
				fkeyScriptPath = dbFilePath + "/" + table_name.upper() + "_FKEY_TMP.sql"
				outputForeignKeyFile = open(fkeyScriptPath,'w')
				outputForeignKeyFile.write(foreignTemplate)
				print("Creating Foreign Script for " + table_name.upper())
				print ('*' * 120)
				outputForeignKeyFile.close()
			#}		
		#}
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
			
			for tables in cursor:
			#{
				#table_name = ''.join(tables)
				table_name = tables[0]
				scriptPath = dbFilePath + "/" + table_name.upper() + "_TMP.sql"
				outputFile = open(scriptPath,'w')
				outputFile.write(createTableScript(srcDatabase,databaseIdentifier,table_name,conn))
				outputFile.write(primaryKeyCheck(srcDatabase,databaseIdentifier,table_name,conn))
				outputFile.write(uniqueKeyCheck(srcDatabase,databaseIdentifier,table_name,conn))
				outputFile.write(indexCheck(srcDatabase,databaseIdentifier,table_name,conn))
				print("Creating Database Script for " + table_name.upper())
				print ('*' * 120)
				outputFile.close()
				(foreignTemplate,foreignColumnCount) = foreignKeyCheck(srcDatabase,databaseIdentifier,table_name,conn)
				if foreignColumnCount != 0:
				#{
					fkeyScriptPath = dbFilePath + "/" + table_name.upper() + "_FKEY_TMP.sql"
					outputForeignKeyFile = open(fkeyScriptPath,'w')
					outputForeignKeyFile.write(foreignTemplate)
					print("Creating Foreign Script for " + table_name.upper())
					print ('*' * 120)
					outputForeignKeyFile.close()
				#}	
			#}
		#}
	#}
	cursor.close()
#}