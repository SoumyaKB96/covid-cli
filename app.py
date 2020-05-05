import sys
import actions


class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()
if(sys.argv[1]=="-t"):
    print(actions.cases())
    
elif(sys.argv[1]=="-s"):
        print(actions.state_case(sys.argv[-1]))

elif(sys.argv[1]=="-i"):
        if(sys.argv[-1]=="-i"):
            print(actions.case2())
        else :
            print(actions.cont_case(sys.argv[-1])) 

else : 
    actions.help()

