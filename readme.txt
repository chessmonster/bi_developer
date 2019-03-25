pre-requisites
1. windows OS
2. python 3

deployment steps
1. pull or download from repo
2. cd to bi_dev > exam
3. run: pip install django django-chartjs
4. run: python manage.py runserver
5. commnad line should show. Starting development server at http://127.0.0.1:8000/

notes
1. for simplicity, I used the built-in database of django which is sqlite
2. for part 1, questions 2 and 3, I created a script to perform to populate the fields as descried in the document. 
   the script is at bi_dev/exam/update_fields.py
3. I utilized django and chart js to create the dashboards requested from part 1 (#5, #6, #7)
4. For the answers on part 2, the queries are located at bi_dev/exam/queries.py with a comment header PART 2 QUERIES.

