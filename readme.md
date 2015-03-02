# Data Modeling Assignment 1

Data modeling assignemnt assigned for CSCE 378H at the University of Nebraska - Lincoln. The task is to organize the given records (contained in data.zip) into a  structured file system in order to run 4 given queries against it. Then reorganize the files into B+ trees and run the same queries to see how much processing time is saved.

## Before running

To run this project, you must first unzip data.zip intot he same directory as the program files. Next you must create `users`, `messages`, `users/tree`, and `messages/tree` directories, so that when the program reorganizes the given data it will have directories to store it in.

## Load the files

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

B+ trees are a way to speed up the searching of a file system by creating successive layers of indexes to organize the data. To create the B+ trees to query, first make sure you have the `users/tree` and `messages/tree` directories created. Then run the following command, replacing the `{x}` with the maximum number of children a node may have (we used 10 and 200 for testing in this project).

`python program.py tree {x}`

### Querying the B+ trees

Once the trees have been built, we can run the same queries against them to see the decrease in processing time due to the indexing of the files. To run a query, simply type in the following command replacing `{x}` wiht the corresponding query number seen above. Once again, teh result of the query and the time that it took will be printed out.

`python program.py tree-query {x}`
