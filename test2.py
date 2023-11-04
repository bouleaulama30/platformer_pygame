def delete_line_file_map(filename):
    x,y= 1172,460
    f=open(filename,'r')
    lines=f.readlines()
    f=open(filename,'w')
    print(lines)
    for line in lines:
        i= index_second_coma(line)
        if (f'{x},{y}')!=line[:i]:
            f.write(line)
            print(f'{x},{y}',line[:i])
			
def index_second_coma(string):
    i=0
    count=0
    for elm in string:
        if elm==",":
            count+=1
        if count==2:
            return i
        i+=1
    return -1
    
delete_line_file_map("test2.txt")


