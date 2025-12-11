import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    1name TEXT NOT NULL,
    department TEXT NOT NULL,
    grade INTEGER NOT NULL
)''')# 清空舊資料（避免重複執行時資料重複）
cursor.execute('DELETE FROM students')
# 連接資料庫
cursor.execute('DELETE FROM students')
# 插入範例資料
sample_data = [
('A001', '王小明', '資訊工程系', 1),
('A002', '李小華', '資訊工程系', 2),
('B001', '林小芳', '電機工程系', 3),
('B002', '黃小龍', '電機工程系', 4),
('C001', '鄭小文', '企業管理系', 1),
('C002', '劉小玲', '企業管理系', 2),
('D001', '許小偉', '財務金融系', 3),
('D002', '楊小慧', '財務金融系', 4)]
cursor.executemany('''
    INSERT INTO students (student_id, name, department, grade)
    VALUES (?, ?, ?, ?)''', sample_data)
conn.commit() # 提交變更
conn.close() #關閉連接
print("資料庫建立成功！")
print(f"已插入{len(sample_data)} 筆學生資料")