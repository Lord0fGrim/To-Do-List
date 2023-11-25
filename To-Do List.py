# To-Do List App:
# Build a basic to-do list application where users can add, remove, and mark tasks as completed.

to_do = ['do to bed','go to bed','buy clothes','go take a shit']
marked = ['revived the death']


print('To-Do list: ' + "\n"+ str(to_do))
print('Mark Task: '+ "\n"+ str(marked))

user = input('Enter "A" for add, "R" for remove, or "M" for marked task: ')


def add():
    if user == 'A' or user == 'a':
        add_list = input('Enter new list: ')
        print('\n')
        to_do.append(add_list)
        print('To-Do list: ' + "\n"+ str(to_do))
        print('Mark Task: '+ "\n"+ str(marked))
        print('\n')
add()    

def remove():
    if user == 'R' or user == 'r':
        choose = input('To-Do list or Mark Task:')
        if choose == 'To-Do list' or choose == 'to do list':
            remove_list = input('Enter the No. of Item you wish to remove: ')
            print('\n')
            to_do.pop(int(remove_list) -1)
            print('To-Do list: ' + "\n"+ str(to_do))
            print('Mark Task: '+ "\n"+ str(marked))
            print('\n')
        elif choose == 'Mark Task' or choose == 'mark task':
            remove_list = input('Enter the No. of Item you wish to remove: ')
            print('\n')
            marked.pop(int(remove_list) -1)
            print('To-Do list: ' + "\n"+ str(to_do))
            print('Mark Task: '+ "\n"+ str(marked))
            print('\n')
remove()

def mark():
    if user == 'M' or user == 'm':
        add_list = input('Enter new list: ')
        for i in range(len(to_do)-1):
            if add_list == to_do[i]:
                to_do.pop(i)
        print('\n')
        marked.append(add_list)
        print('To-Do list: ' + "\n"+ str(to_do))
        print('Mark Task: '+ "\n"+ str(marked))
        print('\n')

mark()




