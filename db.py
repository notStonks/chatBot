import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

# --- Достать код ---   
    def get_codA(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codA FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codB(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codB FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codC(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codC FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codD(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codD FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codE(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codE FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codF(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codF FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

    def get_codG(self, serial_num):
        with self.connection:
            result = self.cursor.execute("SELECT codG FROM kodes WHERE id = ?", (serial_num,)).fetchmany(1)
            return (result[0][0])

# --- Достать номер кода ---
    def countA(self):
        with self.connection:
            result = self.cursor.execute("SELECT nA FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countB(self):
        with self.connection:
            result = self.cursor.execute("SELECT nB FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countC(self):
        with self.connection:
            result = self.cursor.execute("SELECT nC FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countD(self):
        with self.connection:
            result = self.cursor.execute("SELECT nD FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countE(self):
        with self.connection:
            result = self.cursor.execute("SELECT nE FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countF(self):
        with self.connection:
            result = self.cursor.execute("SELECT nF FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

    def countG(self):
        with self.connection:
            result = self.cursor.execute("SELECT nG FROM counter WHERE id = ?", (1,)).fetchmany(1)
            return (result[0][0])

# --- Обновить номер кода ---
    def up_nA(self,nA):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nA = ? WHERE id = ?", (nA,1,))

    def up_nB(self,nB):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nB = ? WHERE id = ?", (nB,1,))

    def up_nC(self,nC):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nC = ? WHERE id = ?", (nC,1,))

    def up_nD(self,nD):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nD = ? WHERE id = ?", (nD,1,))

    def up_nE(self,nE):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nE = ? WHERE id = ?", (nE,1,))

    def up_nF(self,nF):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nF = ? WHERE id = ?", (nF,1,))

    def up_nG(self,nG):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nG = ? WHERE id = ?", (nG,1,))

# --- Достать ID кода ---
    def get_IDA(self):
        with self.connection:
            result = self.cursor.execute("SELECT nA FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDB(self):
        with self.connection:
            result = self.cursor.execute("SELECT nB FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDC(self):
        with self.connection:
            result = self.cursor.execute("SELECT nC FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDD(self):
        with self.connection:
            result = self.cursor.execute("SELECT nD FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDE(self):
        with self.connection:
            result = self.cursor.execute("SELECT nE FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDF(self):
        with self.connection:
            result = self.cursor.execute("SELECT nF FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

    def get_IDG(self):
        with self.connection:
            result = self.cursor.execute("SELECT nG FROM counter WHERE id = ?", (2,)).fetchmany(1)
            return (result[0][0])

# --- Поменяит месный ID кода ---
    def up_IDA(self,nA):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nA = ? WHERE id = ?", (nA,2,))

    def up_IDB(self,nB):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nB = ? WHERE id = ?", (nB,2,))

    def up_IDC(self,nC):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nC = ? WHERE id = ?", (nC,2,))

    def up_IDD(self,nD):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nD = ? WHERE id = ?", (nD,2,))

    def up_IDE(self,nE):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nE = ? WHERE id = ?", (nE,2,))

    def up_IDF(self,nF):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nF = ? WHERE id = ?", (nF,2,))

    def up_IDG(self,nG):
        with self.connection:
            return self.cursor.execute("UPDATE counter SET nG = ? WHERE id = ?", (nG,2,))

# --- Пополнение кодов ---
    def up_codA(self,codA,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codA = ? WHERE id = ?", (codA,id,))
    
    def up_codB(self,codB,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codB = ? WHERE id = ?", (codB,id,))

    def up_codC(self,codC,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codC = ? WHERE id = ?", (codC,id,))

    def up_codD(self,codD,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codD = ? WHERE id = ?", (codD,id,))
            
    def up_codE(self,codE,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codE = ? WHERE id = ?", (codE,id,))

    def up_codF(self,codF,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codF = ? WHERE id = ?", (codF,id,))

    def up_codG(self,codG,id):
        with self.connection:
            return self.cursor.execute("UPDATE kodes SET codG = ? WHERE id = ?", (codG,id,))

# --- Внести пользователя ---
    def add_user_idA(self, user_id, payment_id, order_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users ('user_id','order_id', 'payment_id') VALUES (?, ?, ?)", (user_id, order_id, payment_id))

# --- Проверить пользователя ---
    def check_userA(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

# --- Получить пользователя по order_id ---
    def get_user_from_order_idA(self, order_id):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users WHERE order_id = ?", (order_id,)).fetchone()
            return result[0]

# --- Получить пользователя по payment_id ---
    def get_user_from_payment_idA(self, payment_id: int):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users WHERE payment_id = ?", (payment_id,)).fetchmany(1)
            return result[0]

# --- Удалить пользователя ---
    def delete_userA(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
