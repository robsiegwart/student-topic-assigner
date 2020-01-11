# topic_assigner

Assigns unique selections to students (or anything) based on specified prioritized choices. Uses a random seed method to determine priority among duplicate entries of the same priority.

Input data is stored in an excel file using the following format:

Name   | First Choice   | Second Choice | ...  |
------ | -------------- | ------------- | ---- |
Joe    | Mexico         | Belgium       | ...  |
Mary   | France         | Mexico        | ...  |
Frank  | Netherlands    | France        | ...  |

The only header name that matters is 'Name'; all columns to the right of it are assumed as choices with priority given left to right.

Options to the program are the number of iterations to perform and the maximum persons that do not have an asignment allowed. Because it is based on a random order some sequences do not result in a valid outcome. 

Then, the program randomizes the dataset and assigns choices sequentially through the list with high to low priority of selections. Thus, it does not optimize for any criteria (e.g. everyone has at least 2nd choice) but simply returns the first result. Different outcomes can be obtained by re-running the program.

Options are:

    --iterations    int     Specify how may iterations are to be run. Default is 1.
    --unassigned    int     Specify the maximum number of unassigned students. Default is 0.
    --save          bool    Choose whether to save the result to a file Default is False.


## Example

`Sample Data.xlsx` contains the following:

Name     | First Choice   | Second Choice    | Third Choice   |
-------- | -------------- | ---------------- | -------------- |
Joe      | Germany	      | France	         |  New Zealand   |
Mary     | France	      | Croatia	         |  Mexico        |
Ellen    | England	      | Philipines	     |  Russia        |
Jeremy   | Spain	      | Germany	         |                |
John     | Brazil	      | New Zealand	     |  Germany       |
Sue      | Germany	      | United States	 |  South Africa  |
Jacob    | France	      | Mexico	         |  England       |
Jim	     | Mexico	      | Brazil	         |                |
Penny    | Spain	      | Russia	         |  France        |
Audrey	 | Russia	      | South Africa	 |  Austrailia    |


Issuing `python topic_assigner.py --iterations=10 "Sample Data.xlsx"` results in the following:


```
--------------------------------------------------------------------------------
                             Student Topic Assigner
--------------------------------------------------------------------------------


  Processing input file "Sample Data.xlsx"
  Trying for solutions with no unassigned students.
  Performing up to 10 iterations.



[======------------------------------------------------------] 10.0% ...
Criteria met at iteration 2

     Name      Selection  Choice
8  Audrey   South Africa       2
4   Ellen        England       1
1   Jacob         France       1
3  Jeremy          Spain       1
9     Jim         Mexico       1
2     Joe        Germany       1
0    John         Brazil       1
7    Mary        Croatia       2
5   Penny         Russia       2
6     Sue  United States       2


Number of first choices assigned:        6
Number of second choices assigned:       4
Number of third choices assigned:        0
Number of unassigned:                    0
```

Of course, running the program again will likely yield a different result as numerous solutions exist for this dataset.