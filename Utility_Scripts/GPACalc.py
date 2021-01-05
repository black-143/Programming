def calcGPA(finishedSem,targetGPA,targetSEM):
	finishedSemGPA = []
	for i in range(finishedSem):
		finishedSemGPA.append(float(input('Enter SEM%d GPA :: ' %(i+1))))

	finishedSemGPASum = round(sum(finishedSemGPA),2)
	totalfinishedSemGPASum = targetGPA * targetSEM
	remainingSemGPASum = totalfinishedSemGPASum - finishedSemGPASum
	avgPerSem = round((remainingSemGPASum / (targetSEM - finishedSem)),2)
	
	if avgPerSem > 10.0:
		print('Leave it,out of the range.\nGPA :: %.2f' %avgPerSem)
	else:
		print('Try Hard,you can do it.\nGPA :: %.2f' %avgPerSem)

def main():
	finishedSem = int(input('Total no.of semesters finished :: '))
	targetGPA = float(input('Target GPA :: '))
	targetSEM = int(input('Target Semester :: '))
	calcGPA(finishedSem,targetGPA,targetSEM)


if __name__ == '__main__':
	main()

'''
$ py3 GPACalc.py
Total no.of semesters finished :: 4
Target GPA :: 9.5
Target Semester :: 6
Enter SEM1 GPA :: 8.7
Enter SEM2 GPA :: 8.9
Enter SEM3 GPA :: 7.3
Enter SEM4 GPA :: 6.4
Leave it,out of the range.
GPA :: 12.85
'''
