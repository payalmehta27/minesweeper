'''
Create a funtion that takes a grid of # and -, ehre each hash(#)represents a mine and each dash(-) represents a mine- free spot.
Return a grid, where each dash is replaced by a digit, indicating the number of mines immediataley adjacent to the spot i.e. (horizontally,vertically and diagonally)
Input:                                                  Output:
[["-","-","-","#","#"],                                [["1","1","2","#","#"],
 ["-","#","-","-","-"],                                 ["1","#","3","3","2"],
 ["-","","#","-","-"],                                  ["2","4","#","2","0"],
 ["-","#","#","-","-"]                                  ["1","#","#","2","0"],
 ["-","-","-","-","-"]]                                 ["1","2","2","1","0"],
 
 

 
'''
mines_list = [
["-","-","-","#","#"],                                
["-","#","-","-","-"],                                 
["-","-","#","-","-"],                                  
["-","#","#","-","-"],                             
["-","-","-","-","-"]
]  


for xaxis in range (0,5):
    for yaxis in range(0,5):
        row = len(mines_list[0]) -1                #checks elements in row so, 5-1 = 4 (take 1 away to get highest index)
        col = len(mines_list) -1                   #checks elements in coloumn so, 5-1 = 4
        bombs = 0
        if xaxis == 0 :                            #checks if the coordinates are on the edges for the top line
            top = xaxis
        else :
            top = xaxis - 1                        #if elements are not on edge then removes 1 from the value
        if xaxis == col :                          #check if it's on the bottom line
           bottom = xaxis
        else :
           bottom = xaxis + 1                      #if it's  not on the bottom add 1
        if yaxis == 0 :                            #checks if it's first element in the list
            low = yaxis
        else :  
            low = yaxis - 1                        #if its not first element then remove 1
        if yaxis == row :                          #if row and coloumn both have same value then set it's as the highest value         
            high  = yaxis
        else :
            high = yaxis + 1                       #if it's not equal to row then add 1       
        bottom += 1                                #this adds one to the variable that the for loop goes up to one more time  and doesnt skip last value  
        high += 1                                  #this adds one to the variable that the for loop goes up to one more time  and doesnt skip last value  
        for x in range(top,bottom) :
            for y in range(low,high) :
                if mines_list[x][y] == "#" :       #Check if it's bomb . If so adds 1     
                    bombs += 1
        if mines_list[xaxis][yaxis] == "-":        #Check if '-' mine free spot then changes '-' to a count of bomb
            mines_list[xaxis][yaxis] = str(bombs)

for x in mines_list :
    print(x)