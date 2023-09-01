'''
Created on Nov 10, 2022

This program parse through csv data perform math operations
then display a histogram of the user selected column
@author: naeem
'''
import pandas as pd
import matplotlib.pyplot as plt

#class menu
class MainMenu:
    '''Represents the main menu of the program'''
    #class choice dictionary
    popDict = {'a': 'Pop Apr 1', 'b': 'Pop Jul 1','c':'Change Pop', 'd':'Exit Column.'}
    houseDict = {'a':'AGE','b': 'BEDRMS','c':'BUILT','d':'ROOMS','e':'UTILITY','f':'Exit Column'}

    def __init__(self):
        '''Constructor'''
        print('Welcome to the Python Data Analysis App')

        #initialized instance variables
        self.choice, self.file, self.column = None,None,None

    def print_menu(self):
        '''First menu display'''

        #loop on file read errors
        while True:
            try:
                #menu and dictionary to match user selections
                print('\n1. Population Data')
                print('2. Housing Data')
                print('3. Exit the Program')
                menu_dict = {1: 'Population Data.',2:'Housing Data.'}

                #validate input then update class variable choice
                self.choice = self.check_choices(
                    '\nSelect the file you want to analyze: ',
                    '1','2','3'
                    )
                #exit program or
                #print selection from dictionary and attach csv file to file variable
                if self.choice == 1:
                    self.file = pd.read_csv('PopChange.csv',header=0)
                elif self.choice == 2:
                    self.file = pd.read_csv('Housing.csv',header=0)
                else:
                    print('Thanks for using the Data Analysis App')
                    break
                print('\nYou have entered', menu_dict[self.choice])
                break
            except FileNotFoundError:
                print('File not found! Please add excel files to the same directory as script!')

    def menu_pop (self):
        '''Population file menu'''
        print('a. Pop Apr 1')
        print('b. Pop Jul 1')
        print('c. Change Pop')
        print('d. Exit Column')

        self.choice = self.check_choices(
            'Select the Column you want to analyze: ',
            'a','b','c','d')

        #match choice to column name to call again later, then print user choice
        self.column = self.popDict[self.choice]
        print('\nYou have selected', self.popDict[self.choice])

    def menu_hous(self):
        '''Housing file menu'''
        print('a. AGE')
        print('b. BEDRMS')
        print('c. BUILT')
        print('d. ROOMS')
        print('e. UTILITY')
        print('f. Exit Column')

        self.choice = self.check_choices(
            'Select the Column you want to analyze: ',
            'a','b','c','d','e','f')

        #match choice to column name to call again later, then print user choice
        self.column = self.houseDict[self.choice]
        print('\nYou have selected', self.houseDict[self.choice])

    def analyze_file(self,i_file):
        '''Print column analysis'''
        #use instance file to perform operations and graph histogram
        print('The statistics for this column are:')
        print(f'Count = {i_file[self.column].count()}')
        print(f'Mean = {i_file[self.column].mean()}')
        print(f'Standard Deviation = {i_file[self.column].std()}')
        print(f'Min = {i_file[self.column].min()}')
        print(f'Max = {i_file[self.column].max()}')
        print('The Histogram of this column is now displayed.')
        i_file[self.column].plot(kind = 'hist')
        plt.show()

    def check_choices (self,message,*args):
        '''validations user input for selection menu strings

        '''
        #validates input if in user arguments
        #return valid input in lowercase if string or just return int if digit
        while True:
            selection = input(message)
            if selection.isalpha():
                selection = selection.lower()
            if selection not in (args):
                print('Input invalid!')
            else:
                if selection.isalpha():
                    return selection
                return int(selection)

#instance creation and menu loop
instance = MainMenu()
while instance.choice !=3:
    instance.print_menu()

    #flag loop to get back to same menu upon finish
    if instance.choice == 1:
        FLAG = False
        while not FLAG:
            instance.menu_pop()
            if instance.choice != 'd':
                instance.analyze_file(instance.file)
            else:
                FLAG = True
    elif instance.choice == 2:
        FLAG = False
        while not FLAG:
            instance.menu_hous()
            if instance.choice != 'f':
                instance.analyze_file(instance.file)
            else:
                FLAG = True
