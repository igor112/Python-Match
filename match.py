df = {}
df['String_To_Check'] = ['A', 'Random', 'B', 'Random_Two', 'C']
  
# printing original list  
print ("The original list is : " + str(df['String_To_Check'])) 
  
# initializing substring 
df['Check_Here'] = ['xxx', 'zzz', 'A', 'lll', 'B', 'QQQ', 'C']
  
# using list comprehension  
# to get string with substring  
df['Put_Values_Here'] = [i for i in df['String_To_Check'] if j for j in df['Check_Here'] in i] 
  
# printing result  
print ("All strings with given substring are : " + str(df['Put_Values_Here'])) 