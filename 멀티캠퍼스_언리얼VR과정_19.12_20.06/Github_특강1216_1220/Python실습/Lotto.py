#로또 번호를 랜덤으로 뽑아주는 프로그램

import random

numbers = range(1,46)

result = random.sample(numbers, 6)

result.sort()
#result = sorted(result)

print(result)
