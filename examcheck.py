# import examCalculator as exC
from examCalculator import *

x = int(input('첫번째 과목 점수: '))
y = int(input('두번째 과목 점수: '))
z = int(input('세번째 과목 점수: '))
# tot = examCalculator.totalScore(x,y,z)


print(f'총점: {totalScore(x,y,z)}')
print(f'평균 점수: {avgScore(x,y,z)}')
print(f'합격 여부: {p_f(x,y,z)}')