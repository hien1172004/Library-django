python manage.py runserver // chạy 
---cập nhật model vào SQL---
python manage.py makemigrations
python manage.py migrate   
---- cài các thư viện trong requirements
pip install -r requirements.txt
"C:\Program Files\MySQL\MySQL Server 9.0\bin\mysqldump" -u root -p thuvien > C:\Users\Admin\Documents\pythonweb\site1\backup.sql