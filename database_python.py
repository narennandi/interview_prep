import sqlite3

db = sqlite3.connect(':memory:')  # Using an in-memory database
cur = db.cursor()


#Create tables
cur.execute("""CREATE TABLE IF NOT EXISTS Customer 
			(
			id integer PRIMARY KEY,
			firstname varchar(255),
			lastname varchar(255)
			)
			""")

cur.execute("""
			CREATE TABLE IF NOT EXISTS Item 
			(
			id integer PRIMARY KEY,
			title varchar(255),
			price decimal
			)
			""")

cur.execute("""
			CREATE TABLE IF NOT EXISTS BoughtItem 
			(
			ordernumber integer PRIMARY KEY,
			customerid integer,
			itemid integer,
			price decimal,
			CONSTRAINT customerid
				FOREIGN KEY(customerid) REFERENCES Customer(id),
			CONSTRAINT itemid
				FOREIGN KEY(itemid) REFERENCES Item(id)
			)
			""")

#Inserting Data
cur.execute("""
			INSERT INTO Customer (firstname, lastname)
			VALUES 	('Bob', 'Adams'),
					('Amy', 'Smith'),
					('Rob', 'Bennet')
			""")


cur.execute("""
			INSERT INTO Item (title, price)
			VALUES 	('USB', 10.2),
					('Mouse', 12.33),
					('Monitor', 199.99)
			""")


cur.execute("""
			INSERT INTO BoughtItem (customerid, itemid, price)
			VALUES 	(1, 1, 10.2),
                    (1, 2, 12.23),
                    (1, 3, 199.99),
                    (2, 3, 180.00),
                    (3, 2, 11.23)
			""")


#Aggregation functions
cur.execute("""
			SELECT itemid, AVG(price) 
			from BoughtItem 
			GROUP BY itemid
			""")

print(cur.fetchall())


cur.execute("""
			SELECT 
				i.title, AVG(b.price) 
			from 
				BoughtItem b
			INNER JOIN 
				Item i
				on b.itemid = i.id
			GROUP BY 
				b.itemid
			""")

cur.execute("""
			SELECT 
				c.firstname, SUM(b.price) as total
			from 
				BoughtItem b
			INNER JOIN
				Customer c
				on b.customerid = c.id
			group by
				c.firstname
			""")

print(cur.fetchall())
