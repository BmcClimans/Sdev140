"""
Figure 3-21 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. 
Use the flowchart to create a program that leads a person through the steps of fixing a bad Wi-Fi connection. 
Here is an example of the program’s output: 
"""
#Wifi troubleshooting program, get answer for if loop
answer: str = input('Reboot the computer and try to connect. Did that fix the problem? (yes or no): ')

# if/elif/else loop to troubleshoot wifi connection
if answer == 'yes':
    print('Internet connection is working.')
elif answer == 'no':
    answer = input('Reboot the router and try to connect. Did that fix the problem? (yes or no): ')
    if answer == 'yes':
        print('Internet connection is working.')
    elif answer == 'no':
        answer = input('Make sure the cables between the router & modem are plugged in firmly. Did that fix the problem? (yes or no): ')
        if answer == 'yes':
            print('Internet connection is working.')
        elif answer == 'no':
            answer = input('Move the router to a new location and try to connect. Did that fix the problem? (yes or no): ')
            if answer == 'yes':
                print('Internet connection is working.')
            elif answer == 'no':
                print('Get a new router.')