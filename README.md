# topic_assigner.py

Assigns unique selections to students (or anything) based on specified prioritized choices. The method used is via a random seed to determine priority among duplicate entries of the same priority. Thus, the program first randomizes the rows in the table and then assignes choices sequentially from person to person and from highest to lowest priority, avoiding duplicates.

Input data is stored in an excel file using the following format:

Name   | First Choice   | Second Choice | ...  |
------ | -------------- | ------------- | ---- |
Joe    | Mexico         | Belgium       | ...  |
Mary   | France         | Mexico        | ...  |
Frank  | Netherlands    | France        | ...  |

Column names are irrelevent. The only convention is that the first column is the Name/Student and the following columns to the right are the choices with priority given left to right (leftmost is highest priority).

Options to the program are the number of iterations to perform (`--iterations`) and the maximum persons allowed that do not have an assignment (`--unassigned`). Because it is based on a random order some sequences do not result in a valid outcome. Additionally, since no logic is performed it will not tell you if the dataset has no solutions with the specified value of `unassigned`.

Different outcomes can be obtained by re-running the program, and with the optional `--save` parameter the results can be saved to a file (names are auto-appended with a number to avoid overwriting existing results).


## Usage

```
python topic_assigner.py [OPTIONS] FILENAME
```

```
Options:
  --iterations INTEGER  Specify how may iterations are to be run. Default is 1.
  --unassigned INTEGER  Specify the maximum number of unassigned students. Default is 0.
  --save                Flag to choose whether to save the result to a file.
```

## Example

The included `Sample Data.xlsx` contains the following:

Name     | First Choice   | Second Choice    | Third Choice   |
-------- | -------------- | ---------------- | -------------- |
Joe      | Germany        | France           |  New Zealand   |
Mary     | France         | Croatia          |  Mexico        |
Ellen    | England        | Philipines       |  Russia        |
Jeremy   | Spain          | Germany          |                |
John     | Brazil         | New Zealand      |  Germany       |
Sue      | Germany        | United States    |  South Africa  |
Jacob    | France         | Mexico           |  England       |
Jim      | Mexico         | Brazil           |                |
Penny    | Spain          | Russia           |  France        |
Audrey   | Russia         | South Africa     |  Austrailia    |


Issuing `python topic_assigner.py "Sample Data.xlsx" --iterations=10` results in the following:


```
--------------------------------------------------------------------------------
                             Student Topic Assigner
--------------------------------------------------------------------------------


  Processing file "Sample Data.xlsx"
  Trying for solutions with no unassigned students.
  Performing up to 10 iterations.



[========================------------------------------------] iteration 5

Criteria met at iteration 5

     Name      Selection  Choice
8  Audrey   South Africa       2
7   Ellen        England       1
2   Jacob         France       1
0  Jeremy          Spain       1
9     Jim         Mexico       1
1     Joe        Germany       1
6    John         Brazil       1
3    Mary        Croatia       2
5   Penny         Russia       2
4     Sue  United States       2


First choices assigned:                  6  (60%)
Second choices assigned:                 4  (40%)
Third choices assigned:                  0  (0%)
Unassigned:                              0
```

Of course, running the program again will likely yield a different result as numerous solutions exist for this dataset.
