import random

cards = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

random.shuffle(cards)
sum1 =0
sum2 =0
queue1=[]
queue2=[]
for i in range(3):
  print("round ",i)
  p1 = int(input("Player 1: "))
  sum1 += cards[p1]
  queue1.append(cards[p1])
  p2 = int(input("Player 2: "))
  sum2 += cards[p2]
  queue2.append(cards[p2])

print(queue1);
print(queue2)

print("Card picked by Player 1: " , sum1)
print("Card picked by Player 2: " , sum2)

if sum1 > sum2:
  print("Player 1 is the winner!")
elif sum1 < sum2:
  print("Player 2 is the winner!")
else:
  print("It's a tie!")