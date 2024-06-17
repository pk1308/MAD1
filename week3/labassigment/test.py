import sys 

def run_script():
    c_index = sys.argv.index('-c') if '-c' in sys.argv else -1
    s_index = sys.argv.index('-s') if '-s' in sys.argv else -1
    # check order 
    if s_index==1 and c_index== -1: 
        student_id = sys.argv[s_index+1]
        print(student_id)
    elif c_index ==1 and s_index== -1:
        course_id= sys.argv[c_index+1]
        print("course_id", course_id)  
    else:
        print("null")  

if __name__ == "__main__":
    run_script()