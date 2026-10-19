from pyscript import display, document

def member_adding(e):
    first_name = document.getElementById('name').value.title().strip() # first name input
    last_name = document.getElementById('surname').value.title().strip() # last name input
    full_name = first_name + ' ' + last_name 

    grade7 = {'Marianna Wheelan', 'Bobby Maler', 'Heather Taylor'}
    grade8 = {'Alice Floyd', 'Paula White', 'Luka Allstar'}
    grade9 = {'Stanley Anderson', 'Jordan Hughes', 'Amelia Gatsby'}
    grade10 = {'Robert Barrington', 'Charlie Hayes', 'Christian Brooks'}

    all_members = grade7 | grade8 | grade9 | grade10 # union
    all_members.add(full_name) # adding a new member

    display(all_members, target='results')
    display(f'Total number of students: {len(all_members)}', target='results')