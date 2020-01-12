'''
    Title:          Student Topic Asssigner
    Author:         Rob Siegwart
    Date:           1/9/2019
    Description:    Assigns unique selections of topics to students based on
                    their selected preferences.
                    
                    Uses random seeding to determine
                    priority and does not enforce logical rules.
                    
                    The program may be run several times to obtain different outcomes.

                    Because it uses random seeding some sequencing does not produce
                    a valid solution.


                    The saved file name is [filename]_assigned.xlsx and is put in the same directory as 
                    the input file. It also appends a digit to avoid overwriting existing results
                    so the program may be rerun to obtain additional solutions while keeping
                    existing solutions.

                    Input data is an excel file (.xlsx) with the student name followed by choices:

                    Name   | 1st Choice   | 2nd Choice | ...
                    ------ | ------------ | ---------- |
                    Joe    | Mexico       | Austrailia | ...
                    Mary   | Portugal     | Iceland    | ...

                    The only column name that is expected is 'Name'. The columns to the right of it
                    are assumed to be the choice entries in decreasing priority from left to right.

                    As many or as little choices may be added for each student and do not have to be
                    the same number.
'''

import os
import sys
import pandas as pd
import click


def print_header(w=80):
    print('\n')
    print('-'*w)
    print('Student Topic Assigner'.center(w))
    print('-'*w)
    print('\n')


@click.command()
@click.argument('filename')
@click.option('--iterations', default=1, help='Specify how may iterations are to be run. Default is 1.')
@click.option('--unassigned', default=0, help='Specify the maximum number of unassigned students. Default is 0.')
@click.option('--save', default=False, is_flag=True, help='Choose whether to save the result to a file. Default is False.')
def run(filename, iterations, unassigned, save):
    '''
    Assign topics to students based on priority until the number of unassigned
    students is equal to or less than the value 'unassigned' (defaults to 0). 
    '''
    data = pd.read_excel(filename,index_col='Name')
    choice_cols = data.columns

    def assign():
        '''
        Assign choices sequentially with a random seed to determine priority.
        '''
        # Randomize
        data_rand = data.sample(frac=1)

        # Drop rows with all empyty entries
        data_rand.dropna(how='all', subset=choice_cols, inplace=True)

        # Initialize variables
        assigned = dict()
        topics_used = set()
        rank_vector = [0]*len(choice_cols)

        # Assign topics
        for index,row in data_rand.iterrows():
            row_ = row.dropna()

            for index_,choice in enumerate(row_):
                if choice in topics_used:
                    continue
                else:
                    assigned[row.name] = [choice,index_+1]
                    topics_used.add(choice)
                    rank_vector[index_] += 1
                    break
            
            if not assigned.get(row.name):
                assigned[row.name] = ['<< None >>','-']
            

        # Organize data for output dataframe
        selections = list(map(lambda x: x[0], assigned.values()))
        choice = list(map(lambda x: x[1], assigned.values()))

        # Create an output dataframe
        pd_data = { 'Name': list(assigned.keys()), 'Selection': selections, 'Choice': choice }
        df = pd.DataFrame(pd_data)
        num_unassigned = len(df[df.Selection == '<< None >>'])

        return df,rank_vector,num_unassigned

    # Print information to console
    print_header()
    print('  Processing input file "{}"'.format(filename))
    if unassigned == 0:
        print('  Trying for solutions with no unassigned students.')
    else:
        print('  Trying for solutions with {} or less unassigned students.'.format(unassigned))
    print('  Performing up to {} iterations.'.format(iterations))
    if save:
        print('  Result if found will be saved to a file.')
    print('\n\n')


    for i in range(iterations):
        if iterations > 1:
            progress(i,iterations)
        df,rv,um = assign()

        if um <= unassigned:
            # Sort the results by name
            df.sort_values(by='Name',inplace=True)

            print('\nCriteria met at iteration {}\n'.format(i+1))
            print(df)
            print('\n')
            print('Number of first choices assigned: '.ljust(40),rv[0],' ({}%)'.format(round(100*rv[0]/sum(rv)),1))
            print('Number of second choices assigned: '.ljust(40),rv[1],' ({}%)'.format(round(100*rv[1]/sum(rv)),1))
            print('Number of third choices assigned: '.ljust(40),rv[2],' ({}%)'.format(round(100*rv[2]/sum(rv)),1))
            print('Number of unassigned: '.ljust(40),um)
            print('\n')
            
            if save:
                files = list(map(lambda x: os.path.splitext(x)[0], os.listdir()))
                out_fn = '{} - Assigned'.format(os.path.splitext(filename)[0])
                j = 1
                while out_fn + ' ' + str(j) in files:
                    j+=1
                out_fn += ' ' + str(j) + '.xlsx'
                
                df.to_excel(out_fn)
                print('Result saved to file "{}"\n\n\n'.format(out_fn))

                print(' End '.center(80,'-'))
                print('\n\n\n')
            
            return
    
    print('\n\nCriteria not met after {} iterations.\n'.format(iterations))
    print(' End '.center(80,'-'))
    print('\n\n\n')


def progress(count, total, status=''):
    '''
    Display a progress bar.
    
    Credit: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    '''
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


if __name__ == '__main__':
    run()