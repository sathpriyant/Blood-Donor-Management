import mysql.connector

class BloodDonorManager:
    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Priyan@07",
            database = "blood_db"
        )
        print("connection successful")

    def get_obj(self,id=None):
        try:
            self.cursor=self.con.cursor()
            query="select * from donor where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            result=self.cursor.fetchone()
            return result
        except Exception as e:
            return None

    def post(self,**kwargs):
       try:
           self.cursor = self.con.cursor()
           query = "insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
           values = [v for v in kwargs.values()]
           self.cursor.execute(query, values)
           self.con.commit()
           print("donor added")
       except Exception as e:
           print(e)

    def get(self):
        try:
            self.cursor=self.con.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            result=self.cursor.fetchall()
            for i in result:
                print(i)
        except Exception as e:
            print(e)

    def retrive(self,id=None):
        try:
            result = self.get_obj(id)
            if result != None:
                print(result)
            else:
                print("donor not found")
        except Exception as e:
            print(e)

    def dele(self,id=None):
        try:
            result = self.get_obj(id)

            if result != None:
                self.cursor = self.con.cursor()
                query = "delete from donor where id=%s"
                values = (id,)
                self.cursor.execute(query, values)
                self.con.commit()
                print("donor deleted")
            else:
                print("donor not found")

        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_obj(id=id) #to fetch the donor details of given id
            if record != None: #if data found - update operation
                self.cursor = self.con.cursor() #to execute query
                placeholder="" #empty string for using in update query to construct the set part
                for k in kwargs.keys(): #to loop through the kwargs we use when we call
                    placeholder+= k + "=%s, " # eg placeholder = name=%s, city=%s
                    placeholder = placeholder.rstrip(", ") # removes the last , so no error in query
                    query=f"update donor set {placeholder} where id= %s" #update donor set name=%s, city=%s where id=%s
                    values=[v for v in kwargs.values()] #get values from the call
                    values.append(id)#append id to values
                    self.cursor.execute(query,values)
                    self.con.commit()
                    print(" updated successfully")

            else: #if no data found
                print("donor not found")
        except Exception as e:
            print(e)

donor_instance = BloodDonorManager()   #CREATE AN OBJECT

#donor_instance.put(id=1,name="lolan") #update

#donor_instance.dele(id=3) #delete

#donor_instance.retrive(id=1) #single data

donor_instance.get() #full data

# donor_instance.post(name="sanju",blood_group="AB+",phone="9875699083",city="calicut",last_donation=datetime.datetime.now())
#insertion

# #post ,get,put,delete