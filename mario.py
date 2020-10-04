#define get_int
def get_int(text):
    try:
        num = input(text)
        num = int(num)
        return num
    except:
        return get_int(text)

#define print mario
def printmario(level, width):

    if level <= width:
        print(" "*(width-level),"#"*level," ","#"*level,sep="" )
        printmario(level+1,width)


#get input from user to create int
height = get_int("Height: ")

while height > 8 or height < 1:
    height = get_int("Height: ")

printmario(1,height)