import check_database as c_db

if __name__ == "__main__": 
    exemplar_filename = 'exemplar.csv'  
    file_filename = 'sosi.csv'  
    c_db.Check_file(file_filename, exemplar_filename)