rowA=["A"]
rowB=["B"]*9
rowC=["C"]*9
rowD=["D"]*9
rowE=["E"]*9
rowF=["F"]*9
rowG=["G"]*9
rowH=["H"]*9
rowI=["I"]*9
col1=["1"]*9
col2=["2"]*9
col3=["3"]*9
col4=["4"]*9
col5=["5"]*9
col6=["6"]*9
col7=["7"]*9
col8=["8"]*9
col9=["9"]*9

rows = ['A','B','C','D','E','F','G','H','I']
digits='123456789'
columns = ['1','2','3','4','5','6','7','8','9']

#first goal, print squares.
#dataframes and pandas? pandas is an extension, but look up what it is.

#import the pandas library and aliasing as pd
pip install pandas
import pandas as pd
df = pd.DataFrame()
print (df)


#this prints it straight
print (rows)

#the code below prints out each elemnt in a new row
for row in rows: print(row)

#loc gets rows(or colunms) with particular labels from the index
#iloc gets rows (or columns0 at particular positions in the index - so it only takes integers


