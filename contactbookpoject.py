#dictionary has been stored in contacts
contacts = {'Jesulayomi': '09022183739', 'Tofunmi': '08144174291', 'Sunmbo': '08035667878'}

#enter name only if it is true
while True:
    print('Enter a name:(blank to quit)')
    name = input()
    if name == '':
        break

#check to see if the key entered is in the dictionary
    if name in contacts:
        print(contacts + 'is the number of' + contacts[name])
        else:
            print('I do not have contact information for' + name)
            print('What is their contact?')
            cnts = input()
            contacts[name] = cnts
            print('Contact List Updated.')
