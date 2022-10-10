def snail(snail_map):
    snail_list=[]
    map_with_mark_y=[] 
    map_with_mark_x=[] 
    x=0
    y=0
    for i in range(int(len(snail_map)/2)+1):
        while y<len(snail_map[x]):
            if y in map_with_mark_y or y<0 or y>=len(snail_map[x]):
                break
            snail_list.append(snail_map[x][y])
            y+=1
        map_with_mark_x.append(x)
        x+=1
        y-=1

        while x<len(snail_map):
            if x in map_with_mark_x or x<0 or x>=len(snail_map):
                break
            snail_list.append(snail_map[x][y])
            x+=1
        
        map_with_mark_y.append(y)
        x-=1
        y-=1

        while y>=0:
            if x in map_with_mark_x or x<0 or x>=len(snail_map):
                break
            snail_list.append(snail_map[x][y])
            y-=1
        map_with_mark_x.append(x)
        x-=1
        y+=1

        while x>=0:
            if y in map_with_mark_y or y<0 or y>=len(snail_map[x]):
                break
            snail_list.append(snail_map[x][y])
            y-=1
        y+=1
        map_with_mark_y.append(y)
        y+=1

    return snail_list









array = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(snail(array))