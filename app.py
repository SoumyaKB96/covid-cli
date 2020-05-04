import sys
import actions


if(sys.argv[1]=="-t"):
    print(actions.cases())
    
if(sys.argv[1]=="-s"):
    print(actions.state_case(sys.argv[-1]))

if(sys.argv[1]=="-i"):
    if(sys.argv[-1]=="-i"):
     print(actions.case2())
    else :
        print(actions.cont_case(sys.argv[-1])) 

