import psycopg2
import xlrd

book = xlrd.open_workbook("pytest.xlsx")
sheet = book.sheet_by_name("Source")

database = psycopg2.connect (database = "RunP", user="postgres", password="", host="localhost", port="5432")

cursor = database.cursor()

query = """INSERT INTO orders (Daily_Date, Days, First, Second, Leader) VALUES (%s, %s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    Daily_Date = sheet.cell(r,0).value
    Days = sheet.cell(r,1).value
    First = sheet.cell(r,2).value
    Second = sheet.cell(r,3).value
    Leader = sheet.cell(r,4).value

    values = (Daily_Date, Days, First, Second, Leader)

    cursor.execute(query, values)

cursor.close()

database.commit()

database.close()

print ""
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "I just imported Excel into postgreSQL"