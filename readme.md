# Data Modeling Assignment 1

Unzip data.zip to run this. Then in the command line run

`python program.py load` - Loads the assignment files and restructures them into individual files

`python program.py users {field}` - Shows all of the users, sorted by the field (id, first, last, city, state)

`python program.py query {x}` - Runs one of the queries x = (1-4)


## B+ tree implementation

B+ tree file system. The root filw will be in row 0 and have an id of 0. Teh third paramter in the file name is the number of children the file has. Those children will be in the root row + 1. They will each have an id, and a number of children as well.

{row}_{id}_{num_children}.dat

0_0_5.dat

1_0_5.dat, 1_1_5.dat, 1_2_5.dat, 1_3_5.dat, 1_4_5.dat, 1_5_5.dat
