import mysql.connector
class student:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Priyan@07",
            database="task1"
        )
        print("connection successful")
    def post(self,**kwargs):
        try:
            self.cursor=self.con.cursor()
            query="insert into student(name,place,course) values(%s,%s,%s)"
            values=[i for i in kwargs.values()]

            self.cursor.execute(query,values)
            self.con.commit()
            print("added")
        except Exception as e:
            print(e)

obj=student()
obj.post(name="riya",place="calicut",course="python")
obj.post(name="amal",place="kakkanad",course="data_analytics")
obj.post(name="sam",place="kochi",course="digital_marketing")
obj.post(name="manu",place="calicut",course="python")