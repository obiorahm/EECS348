import common
import student_code
import time

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def run_experiment(board, next, win, gmme, gabe):
	b=[0 for x in range(9)];
	common.set_board(b,board)
	common.print_board(b)
	common.variables.explored = 0
	wmm = student_code.minmax_tictactoe(b,next)
	mme=common.variables.explored
	common.variables.explored = 0
	wabp = student_code.abprun_tictactoe(b,next)
	abpe=common.variables.explored
	
	print (common.legend(next) + " moves Result :")
	res1 = "- MIN-MAX: "+ common.legend(wmm) + " wins "
	if (wmm!=win):
		res1 += "(" +bcolors.RED + "Fail" + bcolors.NORMAL + ")"
	else:
		res1 += "(" +bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

	res1 += " boards explored " + str(mme)
	
	if (mme>gmme):
		res1 += "(" +bcolors.RED + "Fail" + bcolors.NORMAL + ")"
	else:
		res1 += "(" +bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"
	
	print (res1)
	
	res1= "- ALPHA-BETA: "+common.legend(wabp)+" wins "
	if (wabp!=win):
		res1 += "(" +bcolors.RED + "Fail" + bcolors.NORMAL + ")"
	else:
		res1 += "(" +bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"

	res1 += " boards explored " + str(abpe)

	if (abpe>gabe):
		res1 += "(" +bcolors.RED + "Fail" + bcolors.NORMAL + ")"
	else:
		res1 += "(" +bcolors.GREEN + "Pass" + bcolors.NORMAL + ")"
	
	print (res1)
	print("")
	print("")
	return wmm==win and mme<=gmme and wabp==win and abpe<=gabe	


board1 = (
"X O"
"OOX"
"XO ")
next1=common.constants.O
win1=common.constants.O
mme1=4
abe1=2

board2 = (
" XO"
"   "
"   ")
next2=common.constants.O
win2=common.constants.O
mme2=8232
abe2=1250

board3 = (
"XOO"
"XX "
"   ")
next3=common.constants.O
win3=common.constants.X
mme3=27
abe3=9

board4 = (
"X  "
" O "
"   ")
next4=common.constants.O
win4=common.constants.NONE
mme4=6812
abe4=1535

board5 = (
"OOX"
"XOO"
"XOX")
next5=common.constants.O
win5=common.constants.O
mme5=1
abe5=1

board6 = (
"XOO"
"OX "
"0XX")
next6=common.constants.O
win6=common.constants.X
mme6=1
abe6=1


board7 = (
"   "
"   "
"   ")
next7=common.constants.O
win7=common.constants.NONE
mme7=549946
abe7=94978
all_passed = True
all_passed = all_passed 


print ("Board 1")
start_time = time.time()
exp1 = run_experiment(board1,next1,win1,mme1,abe1)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 2")
start_time = time.time()
exp2 = run_experiment(board2,next2,win2,mme2,abe2)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 3")
start_time = time.time()
exp3 = run_experiment(board3,next3,win3,mme3,abe3)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 4")
start_time = time.time()
exp4 = run_experiment(board4,next4,win4,mme4,abe4)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 5")
start_time = time.time()
exp5 = run_experiment(board5,next5,win5,mme5,abe5)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 6")
start_time = time.time()
exp6 = run_experiment(board6,next6,win6,mme6,abe6)
print("--- %s seconds ---" % (time.time() - start_time))
print ("Board 7")
start_time = time.time()
exp7 = run_experiment(board7,next7,win7,mme7,abe7)
print("--- %s seconds ---" % (time.time() - start_time))

all_passed = exp1 and exp2 and exp3 and exp4 and exp5 and exp6 and exp7


if all_passed:
	exit(0)
else:
	exit(1)
