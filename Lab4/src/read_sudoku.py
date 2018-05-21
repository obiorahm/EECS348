f=open("sudoku.txt", "r")
sudoku = ()
row = ""
if f.mode == 'r':
	f1 = f.readlines()
	for line in f1:
		start = -1
		for char in line:
			start += 1
			if char == ".":
				row +="0"
			else:
				row += char
		new_sudoku = common.init_sudoku();
		common.set_sudoku( new_sudoku, row);
		run_experiment(row, 6000, 800, 650)	
		row = ""		
#common.print_sudoku(new_sudoku)
