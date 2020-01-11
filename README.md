# topic_assigner

Assigns unique selections to students (or anything) based on specified prioritized choices. Uses a random seed method to determine priority among duplicate entries of the same priority.

Input data is stored in an excel file using the following format:

Name   | First Choice   | Second Choice | .... |
------ | -------------- | ------------- | ---- |
Joe    | Mexico         | Belgium       | ...  |
Mary   | France         | Mexico        | ...  |
Frank  | Netherlands    | France        | ...  |

The only header name that matters is 'Name'; all columns to the right of it are assumed as choices with priority given left to right.

Then, the program randomizes the dataset and assigns choices sequentially through the list with high to low priority of selections. Thus, it does not optimize for any criteria and simply returns the first result. Different outcomes can be obtained by re-running the program.

Options are:

    --iterations    int     Specify how may iterations are to be run. Default is 1.
    --unassigned    int     Specify the maximum number of unassigned students. Default is 0.
    --save          bool    Choose whether to save the result to a file Default is False.