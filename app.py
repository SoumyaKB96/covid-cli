import sys
import actions





if(sys.argv[1]=="-t"):
    print(actions.cases())
    
if(sys.argv[1]=="-s"):
    print(actions.state_case(sys.argv[-1]))



