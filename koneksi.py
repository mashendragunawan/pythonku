import mysql.connector
from mysql.connector import Error

def connector_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hendra"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"✅ Berhasil terhubung ke MySQL Server versi {db_info}")
            return connection
            
    except Error as e:
        print(f"❌ Gagal terhubung ke MySQL: {e}")
        return None

def create_table():
    # Mendapatkan koneksi database
    conn = connector_to_mysql()
    
    if conn is None:
        print("Tidak dapat membuat tabel karena koneksi gagal")
        return
    
    # Daftar query untuk membuat tabel
    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            stock INT DEFAULT 0
        )
        """
    ]
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Eksekusi setiap query pembuatan tabel
        for query in create_table_queries:
            cursor.execute(query)
            print("✔️ Tabel berhasil dibuat")
        
        # Commit perubahan
        conn.commit()
        
    except Error as e:
        print(f"❌ Gagal membuat tabel: {e}")
        if conn:
            conn.rollback()
            
    finally:
        # Pastikan cursor dan koneksi ditutup
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            print("🔌 Koneksi database ditutup")

# Jalankan fungsi create_table saat script di-run
if __name__ == "__main__":
    create_table()