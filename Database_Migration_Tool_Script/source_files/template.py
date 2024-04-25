from string import Template
from textwrap import dedent

def createForeignStartTemplate(tableName):
#{
	foreignStartTemplate = Template("""BEGIN
--{
	DECLARE @lv_table_name			VARCHAR(30) = '$tableName';
	DECLARE @lv_contraint_sql		VARCHAR(max);
	DECLARE @lv_old_column_list		VARCHAR(max);
	DECLARE @lv_new_column_list		VARCHAR(max);
	DECLARE @li_old_column_count		VARCHAR(max);
	DECLARE @li_new_column_count		VARCHAR(max);
--}
--{
	---------------------------------- Create Foreign Constraint ----------------------------------
	""")
	
	tableName = tableName.upper() + "_TMP"
	foreignSubstitute=foreignStartTemplate.substitute(tableName=tableName)
	return foreignSubstitute
#}
def createForeignTemplate(foreignString,foreignColumnList,foreignColumnCount):
#{
	foreignTemplate = Template("""
	SET @lv_contraint_sql = $foreignString

	SET @lv_old_column_list = '$foreignColumnList';
	SET @lv_new_column_list = '$foreignColumnList';

	SET @li_old_column_count = $foreignColumnCount;
	SET @li_new_column_count = $foreignColumnCount;

	-- exec to create foreign constraint
	exec usp_create_foreign_constraint @lv_table_name, @lv_contraint_sql, @lv_old_column_list, @li_old_column_count, @lv_new_column_list, @li_new_column_count, 'N'

	""")
	
	foreignSubstitute=foreignTemplate.substitute(foreignString=foreignString,foreignColumnList=foreignColumnList,foreignColumnCount=foreignColumnCount)
	return foreignSubstitute
#}

def createTableTemplate(tableName,createTableString):
#{
	createTemplate = Template("""DECLARE
--{
	@lv_table_name			VARCHAR(128) = '$tableName'
	,@lv_table_sql			VARCHAR(max)
	,@li_count				INTEGER
	,@lv_contraint_sql		VARCHAR(max)
	,@lv_index_sql			VARCHAR(max)
	,@lv_old_column_list		VARCHAR(max)
	,@lv_new_column_list		VARCHAR(max)
	,@li_old_column_count		INTEGER
	,@li_new_column_count		INTEGER
--}
BEGIN
--{
	---------------------------------- Create Table ----------------------------------
	Set @lv_table_sql = $createTableString
									
	exec dbo.usp_create_table @lv_table_name, @lv_table_sql
	""")
	
	tableName = tableName.upper() + "_TMP"
	createSubstitute=createTemplate.substitute(tableName=tableName,createTableString=createTableString)
	return createSubstitute
#}

def createPrimaryTemplate(primaryString,primaryColumnList,primaryColumnCount):
#{
	primaryTemplate = Template("""
	---------------------------------- Create Primary Constraint ----------------------------------
	Set @lv_contraint_sql = $primaryString

	Set @lv_index_sql = null

	Set @lv_old_column_list = '$primaryColumnList'
	Set @lv_new_column_list = '$primaryColumnList'

	Set @li_old_column_count = $primaryColumnCount
	Set @li_new_column_count = $primaryColumnCount

	-- exec procedure to create primary constraint
	exec dbo.usp_create_primary_constraint @lv_table_name, @lv_contraint_sql, @lv_index_sql, @lv_old_column_list, @li_old_column_count, @lv_new_column_list, @li_new_column_count, 'Y'
	""")
	
	primarySubstitute=primaryTemplate.substitute(primaryString=primaryString,primaryColumnList=primaryColumnList,primaryColumnCount=primaryColumnCount)
	
	return primarySubstitute
#}

def createUniqueTemplate(uniqueString,uniqueColumnList,uniqueColumnCount):
#{
	uniqueTemplate = Template("""
	---------------------------------- Create Unique Constraint ----------------------------------
	Set @lv_contraint_sql = $uniqueString
	
	Set @lv_index_sql = null
	
	Set @lv_old_column_list = '$uniqueColumnList'
	Set @lv_new_column_list = '$uniqueColumnList'
	
	Set @li_old_column_count = $uniqueColumnCount
	Set @li_new_column_count = $uniqueColumnCount
	
	-- exec procedure to create unique constraint
	exec dbo.usp_create_primary_constraint @lv_table_name, @lv_contraint_sql, @lv_index_sql, @lv_old_column_list, @li_old_column_count, @lv_new_column_list, @li_new_column_count, 'U'
	""")
	
	uniqueSubstitute=uniqueTemplate.substitute(uniqueString=uniqueString,uniqueColumnList=uniqueColumnList,uniqueColumnCount=uniqueColumnCount)
	return uniqueSubstitute
#}

def createIndexTemplate(indexString,indexColumnList,indexColumnCount):
#{
	indexTemplate = Template ("""
	---------------------------------- Create Foreign/Other Indexes ----------------------------------
	Set @lv_index_sql = '$indexString'

	Set @lv_old_column_list = '$indexColumnList'
	Set @lv_new_column_list = '$indexColumnList'

	Set @li_old_column_count = $indexColumnCount
	Set @li_new_column_count = $indexColumnCount

	-- exec to create index
	exec dbo.usp_create_index @lv_table_name, @lv_index_sql, @lv_old_column_list, @li_old_column_count, @lv_new_column_list, @li_new_column_count, 'N'
	""")
	
	indexSubstitute = indexTemplate.substitute(indexString=indexString,indexColumnList=indexColumnList,indexColumnCount=indexColumnCount)
	return indexSubstitute
#}

def endTemplate():
#{
	finishTemplate = Template("""
--}
END

GO
""")

	finishSubstitute=finishTemplate.substitute()
	return finishSubstitute