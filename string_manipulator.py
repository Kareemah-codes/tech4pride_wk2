 
#Input Validation

sentence = input('Enter your sentence')

if not sentence or len(sentence)<20:
    print('Error: string must not be empty and minimum of 20 characters')

#Input Transformation
else:
    print('_____WELCOME TO STRING FORMATTER_____ \n' \
    'Enter any of the following commands to apply transformations to your sentence\n' \
    'Command	Action \n' \
    'U	Convert the string to uppercase \n' \
    'L	Convert the string to lowercase \n' \
    'R	Reverse the string \n' \
    'Z	Undo the last change (only one level of undo) \n' \
    'C ch1 ch2	Replace all occurrences of command ch1 with command ch2 \n' \
    'X	Terminate — stop accepting commands and display the final string \n \n')

    command = input("Enter command")
    sentence_versions = []
    sentence_version_index = -2
    while (command == "U" or "L" or "R" or"Z" or "C" or "X"):
        if command == "U":
           sentence = sentence.upper()
           sentence_versions.append(sentence)
           command = input("Enter command")

        if command == "L":
           sentence = sentence.lower()
           sentence_versions.append(sentence)
           command = input("Enter command")

        if command == "R":
            sentence = sentence[::-1]
            sentence_versions.append(sentence)
            command = input("Enter command")    

        if command == "Z":
            sentence = sentence_versions[sentence_version_index]
            sentence_version_index -=1
            command = input("Enter command")
        
        if command == "C":
            ch1 = input('What character do you want to replace?')
            ch2 = input('What character will replace ' + ch1 +" ?")
            sentence = sentence.replace(ch1,ch2)
            sentence_versions.append(sentence)
            command = input("Enter command")

        
        if command == "X":
            print(sentence)
            break
            


    

     
     
    
    
     
    