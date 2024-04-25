from getQuery import getQuery
from databaseMapping import getDatabaseMapping
from template import *

def createTableScript(srcDatabase,databaseIdentifier,tableName,conn):
#{
	srcDatatypeList, tgtDatatypeList = getDatabaseMapping(srcDatabase)
	columnQuery = getQuery(srcDatabase,'column') + " where ut.table_name = '" + tableName.upper() + "'"

	cursor = conn.cursor()
	cursor.execute(columnQuery)
	columnNameList = []
	targetDatatypeList = []
	dataLengthList = []
	dataPrecisionList = []
	dataScaleList = []
	nullableList = []
	for columns in cursor:
	#{
		columnName = columns[1]
		columnNameList.append(columnName)
		srcDatatype = columns[2].lower()
		dataLength = columns[3]
		dataLengthList.append(dataLength)
		dataPrecision = columns[4]
		dataPrecisionList.append(dataPrecision)
		dataScale = columns[5]
		dataScaleList.append(dataScale)
		nullable = columns[6]
		nullableList.append(nullable)

		if srcDatatype in srcDatatypeList:
		#{
			if srcDatatype.lower() == 'number' and dataPrecision != '0' and dataScale != 0:
			#{
				tgtDatatype = 'decimal'
			#}
			else:
			#{
				positionOfDatatype = srcDatatypeList.index(srcDatatype)
				tgtDatatype = tgtDatatypeList[positionOfDatatype]
			#}
		#}
		else:
		#{
			tgtDatatype = srcDatatype
		#}
		targetDatatypeList.append(tgtDatatype)
	#}
	createTableScript = "'Create table " + tableName.upper() + "_tmp' + char(10) + \n" 
	createTableScript += "\t\t\t\t\t'(' + char(10) + \n"
	for loopCounter in range(len(columnNameList)):
	#{
		if len(columnNameList) == loopCounter + 1:
		#{
			createTableScript += "\t\t\t\t\t'\t" + columnNameList[loopCounter].lower() + " "
			if targetDatatypeList[loopCounter] == 'decimal':
			#{
				createTableScript += targetDatatypeList[loopCounter].upper() + "(" + str(dataPrecisionList[loopCounter]) + "," + str(dataScaleList[loopCounter]) + ") NULL' + char(10) +\n" 
			#}
			elif nullableList[loopCounter] == 'N' and targetDatatypeList[loopCounter] == 'integer':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NOT NULL' + char(10) +\n"
			#}
			elif nullableList[loopCounter] == 'N' and targetDatatypeList[loopCounter] == 'timestamp':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NOT NULL' + char(10) +\n"
			#}
			elif nullableList[loopCounter] == 'N':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + "(" + str(dataLengthList[loopCounter]) + ") NOT NULL ' + char(10) +\n" 
			#}
			elif targetDatatypeList[loopCounter] == 'integer':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL' + char(10) +\n"
			#}
			elif targetDatatypeList[loopCounter] == 'timestamp':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL' + char(10) +\n"
			#}
			elif targetDatatypeList[loopCounter] == 'datetime':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL' + char(10) +\n"
			#}
			else:
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + "(" + str(dataLengthList[loopCounter]) + ") NULL' + char(10) +\n"
			#}
		#}
		else:
		#{
			createTableScript += "\t\t\t\t\t'\t" + columnNameList[loopCounter].lower() + " "
			if targetDatatypeList[loopCounter] == 'decimal':
			#{
				createTableScript += targetDatatypeList[loopCounter].upper() + "(" + str(dataPrecisionList[loopCounter]) + "," + str(dataScaleList[loopCounter]) + ") NULL,' + char(10) + \n" 
			#}
			elif nullableList[loopCounter] == 'N' and targetDatatypeList[loopCounter] == 'integer':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NOT NULL,' + char(10) +\n"
			#}
			elif nullableList[loopCounter] == 'N' and targetDatatypeList[loopCounter] == 'timestamp':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NOT NULL,' + char(10) +\n"
			#}
			elif nullableList[loopCounter] == 'N':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + "(" + str(dataLengthList[loopCounter]) + ") NOT NULL,' + char(10) +  \n" 
			#}
			elif targetDatatypeList[loopCounter] == 'integer':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL,' + char(10) +\n"
			#}
			elif targetDatatypeList[loopCounter] == 'timestamp':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL,' + char(10) +\n"
			#}
			elif targetDatatypeList[loopCounter] == 'datetime':
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + " NULL,' + char(10) +\n"
			#}
			else:
			#{
				createTableScript += str(targetDatatypeList[loopCounter]).upper() + "(" + str(dataLengthList[loopCounter]) + ") NULL, ' + char(10) +\n"
			#}
		#}
	#}
	createTableScript += "\t\t\t\t\t')'"
	tableTemplate=createTableTemplate(tableName,createTableScript)
	return tableTemplate
	cursor.close()
#}	

def primaryKeyCheck(srcDatabase,databaseIdentifier,tableName,conn):
#{
	primaryQuery = getQuery(srcDatabase,'primary') + " and uc.table_name = '" + tableName.upper() + "'"

	cursor = conn.cursor()
	cursor.execute(primaryQuery)
	constraintNameList = []
	columnNameList = []
	primaryString = ""
	primaryColumnList = ""
	for primaryconstraint in cursor:
	#{
		constraintName = primaryconstraint[1]
		constraintNameList.append(constraintName)
		columnName = primaryconstraint[2]
		columnNameList.append(columnName)
		columnNameList.sort()
	#}
	if constraintNameList != []:
	#{	
		primaryString = "'Alter table " + tableName.upper() + "_tmp' + char(10) + \n\t\t\t\t\t\t 'ADD PRIMARY KEY ("
		primaryString += columnNameList[0]
		for loopCounter in range(1,len(constraintNameList)):
		#{
			primaryString += "," +columnNameList[loopCounter]
		#}
		primaryString += ")'"
	#}
	primaryTemplate = ""
	primaryColumnList = ','.join(columnNameList)
	primaryColumnCount = len(columnNameList)
	if primaryColumnCount != 0:
	#{
		primaryTemplate = createPrimaryTemplate(primaryString,primaryColumnList,primaryColumnCount)
	#}
	return primaryTemplate
	cursor.close()
#}

def foreignKeyCheck(srcDatabase,databaseIdentifier,tableName,conn):
#{
	foreignQuery = getQuery(srcDatabase,'foreign1') + " and uc.table_name = '" + tableName.upper() + "'" + getQuery(srcDatabase,'foreign2')

	cursor = conn.cursor()
	cursor.execute(foreignQuery)
	rows = cursor.fetchall()
	foreignTemplate = ""
	foreignColumnCount = 0
	if len(rows) != 0:
	#{
		foreignTemplate = createForeignStartTemplate(tableName)
		foreignString = ""
		for foreignconstraint in rows:
		#{
			constraintName = foreignconstraint[0]
			tgtTable = foreignconstraint[2]
			srcColumn = foreignconstraint[3]
			tgtColumn = foreignconstraint[4]
			if constraintName != []:
			#{
				foreignString = "'Alter table " + tableName.upper() + "_tmp' + char(10) +\n 'ADD (CONSTRAINT "
				foreignString += constraintName + " FOREIGN KEY (" + srcColumn + ") REFERENCES " + tgtTable+ " (" + tgtColumn + "))'"
			#}
			foreignColumnCount = srcColumn.count(",") + 1
			foreignTemplate += createForeignTemplate(foreignString,srcColumn,foreignColumnCount)
		#}
		foreignTemplate += endTemplate()
	#}
	return foreignTemplate,foreignColumnCount
	cursor.close()
#}

def uniqueKeyCheck(srcDatabase,databaseIdentifier,tableName,conn):
#{
	uniqueQuery = getQuery(srcDatabase,'unique') + " and uc.table_name = '" + tableName.upper() + "'"
	
	cursor = conn.cursor()
	cursor.execute(uniqueQuery)
	constraintNameList = []
	columnNameList = []
	uniqueString = ""
	
	for uniqueconstraint in cursor:
	#{
		constraintName = uniqueconstraint[0]
		constraintNameList.append(constraintName)
		columnName = uniqueconstraint[2]
		columnNameList.append(columnName)
		columnNameList.sort()
	#}
	if constraintNameList != []:
	#{	
		uniqueString = "'Alter table " + tableName.upper() + "_tmp' + char(10) + \n\t\t\t\t\t\t 'ADD UNIQUE("
		uniqueString += columnNameList[0]
		for loopCounter in range(1,len(constraintNameList)):
		#{
			uniqueString += "," +columnNameList[loopCounter]
		#}
		uniqueString += ")'"
	#}
	uniqueTemplate = ""
	uniqueColumnList = ','.join(columnNameList)
	uniqueColumnCount = len(columnNameList)
	if uniqueColumnCount != 0:
	#{
		uniqueTemplate = createUniqueTemplate(uniqueString,uniqueColumnList,uniqueColumnCount)
	#}
	return uniqueTemplate
	cursor.close()
#}

def indexCheck(srcDatabase,databaseIdentifier,tableName,conn):
#{
	indexQuery = getQuery(srcDatabase,'index1') + " and ui.table_name = '" + tableName.upper() + "' " + getQuery(srcDatabase,'index2')
	
	cursor = conn.cursor()
	cursor.execute(indexQuery)
	indexString = ""
	indexTemplate = ""
	
	for indexconstraint in cursor:
	#{
		indexName = indexconstraint[0]
		uniqueness = indexconstraint[1]
		indexColumnName = indexconstraint[2]
		if indexName != []:
		#{	
			indexString = "Create "
			if uniqueness == 'UNIQUE':
			#{
				indexString += "UNIQUE INDEX "
			#}
			else:
			#{
				indexString += "INDEX "
			#}
			indexString += indexName + " on " + tableName.upper() + "_tmp ("
			indexString += indexColumnName
			indexString += ")"
		#}
		indexColumnCount = indexString.count(",") + 1
		if indexColumnName != "":
		#{
			indexTemplate += createIndexTemplate(indexString,indexColumnName,indexColumnCount)
		#}
	#}
	indexTemplate += endTemplate()
	return indexTemplate
	cursor.close()
#}