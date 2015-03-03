# Data Modeling Assignment 1

Data modeling assignment assigned for CSCE 378H at the University of Nebraska - Lincoln. The task is to organize the given records (contained in data.zip) into a  structured file system in order to run 4 given queries against it. Then reorganize the files into B+ trees and run the same queries to see how much processing time is saved. Timing results can be found below.

#### File descriptions

| file | description |
|---|---|
| program.py | contains the command line program |
| models.py | model definitions for users and messages |
| load.py | loads the records from the old files and reads and writes the new ones |
| sort.py | contains methods to sort lists of users and messages |
| query.py | contains methods to run the queries on the flat files |
| tree_user.py | contains methods to build the B+ tree of users |
| tree_message.py | contains methods to build the B+ tree of messages |
| tree_query.py | contains methods to run the queries against the B+ trees |

### Before running

To run this project, you must first unzip data.zip intot he same directory as the program files. Next you must create `users`, `messages`, `users/tree`, and `messages/tree` directories, so that when the program reorganizes the given data it will have directories to store it in.

### Load the files

Now that the data is unpacked, you can load it into the organized structure by running the following command

`python program.py load`

After this command, the program will populate the `users` and `messages` directories with the organized files. Now we are ready to run some queries against the flat file system.

### Running the queries

This program has 4 hard-coded queries to retrieve data from the files

<ol>
  <li>Find all of the users from Nebraska</li>
  <li>Find how many users sent messages between 8 and 9 am inclusively</li>
  <li>Find how many users from Nebraska sent messages between 8 and 9 am</li>
  <li>Find the user from Nebraska who sent the maximum number of messages between 8 and 9 am</li>
</ol>

To run any of these queries, run the following command, replacing `{x}` with the number of the query. The result of the query and the time that it took to run the query will be printed out

`python program.py query {x}`

### Building B+ trees

B+ trees are a way to speed up the searching of a file system by creating successive layers of indexes to organize the data. To create the B+ trees to query, first make sure you have the `users/tree` and `messages/tree` directories created. Then run the following command, replacing the `{x}` with the maximum number of children a node may have (we used 10 and 200 for testing in this project). To optimize the trees for these queries, the users are sorted by state, and the messages are organized by time (hour, mminute).

`python program.py tree {x}`

### Querying the B+ trees

Once the trees have been built, we can run the same queries against them to see the decrease in processing time due to the indexing of the files. To run a query, simply type in the following command replacing `{x}` wiht the corresponding query number seen above. Once again, the result of the query and the time that it took will be printed out.

`python program.py tree-query {x}`

# Timing Results

Below ar ethe timing results of running the queries on each type of table. The values are approximate and were gathered from and average of three tests each.

| Query | flat files | B+ tree 10 | B+ tree 200 |
|---|---|---|---|
| 1 | 0.02912 s | 0.0009241 s | 0.0011749 s |
| 2 | 1.91538 s | 0.1179518 s | 0.1112210 s |
| 3 | 2.0338 s | 0.1085591 s | 0.1006789 s |
| 4 | 4.4823 s | 0.1984589 s | 0.1847808 s |
