import random
#idea = lost in jungle: have to make certain decisions to get out
allchoices = [[1, "Climb up a tree"], 
           [2, "Eat one (1) berry"], 
           [3, "Drink the sussy river water"], 
           [4, "Follow animal in front"], 
           [5, "Follow the river"]]


def escaperoute():
    result = []
    #if difficulty == "ez":
    for i in range(3):
        idx = random.randint(0,4)
        result.append(allchoices[idx])
    return result

def displaychoices(start, options):
    
    result = start + '\n'
    i = 0
    while i < 3:
        result += str(i+1) + ': ' + options[i][1] + '\n'
        i += 1
    print(result)

def main():
   
    answer = escaperoute()
    allmoves = ''
    #print(answer)
    alive = False
    idx = 0
    
    prevmove = ''

    while not(alive):
        correct = answer[0]
        if correct in allchoices:
            text = '''\nYou wake up in the middle of a jungle and have to get out by nighttime! what do you choose to do next'''
            allchoices.remove(correct)
            random.shuffle(allchoices)
            #print(allchoices)
            options = [correct, allchoices[0], allchoices[1]]
            random.shuffle(options)

        displaychoices(prevmove + text, options)
        

        action = int(input("what are u gna do: (type the number) "))
        
        prevmove = '\n' + options[action-1][1] + '\n'
        allmoves += 'You ' + options[action-1][1] + ' and '
        
        #print(options[action-1][1], correct[1])
        if options[action-1][1] == correct[1]:
            answer.pop(0)
            if answer == []:
                alive = True
                print(allmoves[0].upper() + allmoves[1:] + 'made it out! congrats')
                break
            
            allchoices.append(correct)
            
            #print(answer)
        else:
            random.shuffle(allchoices)
            options = [correct, allchoices[0], allchoices[1]]
            random.shuffle(options)

        
            
main()