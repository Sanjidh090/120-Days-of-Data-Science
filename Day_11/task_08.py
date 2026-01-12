list  = [ 1 ,2 ,3 , -4  ]
my_list = any( x < 0 for x in list )
print ( my_list )
list  = [ 1 ,2 ,3 , 4  ]
pos_check = all(x > 0 for x in list)
print (pos_check)  