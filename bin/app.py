import web
import sqlite3 as lite
import sys

con = None
dbFile = '..\installbase.db'

##############################################################
#This just gives you the version of sqlite
##############################################################
def getSQLiteVersion():
	try:
		con = lite.connect(dbFile)
	
		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')
	
		data = cur.fetchone()
	
		return "SQLite version: " + data
	
	except lite.Error, e:

		return "Error " + ":" + e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()
			
##############################################################			
#this will give you a list of customers from your install base
##############################################################
def getInstallBaseCust():
	try:
		con = lite.connect(dbFile)
	
		cur = con.cursor()
		cur.execute('select distinct CS_CUSTOMER_NAME from tbl_installbase')
	
		rows = cur.fetchall()
	
		print "Here are all of your customers:"
		for row in rows:
			print row[0]
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()
			
##############################################################
#this will give you the install base for a particular customer
##############################################################
def getInstallBaseVNX():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select CS_CUSTOMER_NAME, PRODUCT_GROUP, ITEM_SERIAL_NUMBER from tbl_installbase where PRODUCT_GROUP like \'VNX%\'')
	
		rows = cur.fetchall()
	
		print "Here are all of your customers:"
		for row in rows:
			print row[0]
			print row[1]
			print row[2]
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()
##############################################################			
################### END OF FUNCTION DEFS #####################
##############################################################
			
urls = (
  '/hello', 'Index'
)


app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        
        if form.name == "version":
        	greeting = getSQLiteVersion()
        else:
        	greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()



