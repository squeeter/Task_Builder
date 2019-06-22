'''

2019_06_18_PH_pk_v0_1.py:  Built to generate weekly reports of projects I'm

    working on, and generate todo lists for each day.  Storyboard below:

   

Main Screen:

================================================================================

Welcome - choose an option:

1.  Add Project

2.  Remove Project

3.  Write Daily Tasklist

4.  Generate Weekly Report

Q.  Quit

 

Add Project:

================================================================================

Adds a new line to a file called projects.txt

 

Remove Project:

================================================================================

Removes a project from projects.txt

 

3.  Write Daily Tasklist

================================================================================

Goes to sub-screen:

 

Select a project from the options below:

1.  New, Unrelated Task

2.  [Project A]

...

X.  [Project N]

B.  Go back

 

If 1 is selected, it's treated as a new, one-off task.

If a project is selected, it expands into a sub-menu:

 

Select a task for [Project A]:

1.  New task for [Project A]

2.  [Task A]

...

X.  [Task N]

B.  Go back

 

Once a task is selected, this subscreen appears:

 

Choose an option:

1.  Add to tasklist

0.  Remove from tasklist

 

0 removes it from tasklist, but 1 opens a new window:
'''

from colors import BodyColors as bc

class menus():

    def helpmenu(self):
        try:
            os.system("clear")
            # Logo().banner()
            print("\t[INFORMATION]::")
            print("""
This application is designed to build tasklists via terminal prompts.  I wanted
a series of prompts to help ensure that the tasks were tractable and trackable.
""")
        except:
            print("Welp... something went wrong.")

    def intro_menu(self):
        # Logo().banner()
        print(" [{}!{}] {}Lookup menu:{}".format(bc.CYLW,bc.CEND,bc.CBLU, bc.CEND))
        print('\t[{}1{}] {}Add Project{} - {}Search targets by email address{}'.format(bc.CBLU,bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
        print('\t[{}2{}] {}Remove Project{} - {}Search targets by email address{}'.format(bc.CBLU,bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
        print('\t[{}3{}] {}Build Tasklis{} - {}Search targets by email address{}'.format(bc.CBLU,bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
        print('\t[{}4{}] {}Generate Weekly Report{} - {}Search targets by email address{}'.format(bc.CBLU,bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))
        print('\t[{}Q{}] {}Quit{} - {}Search targets by email address{}'.format(bc.CBLU,bc.CEND,bc.CRED,bc.CEND,bc.CYLW,bc.CEND))

ui = menus()
ui.intro_menu()
