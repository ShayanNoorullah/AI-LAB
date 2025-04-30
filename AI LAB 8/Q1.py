probEven = 3 / 6
probGt4 = 2 / 6
probLt3 = 2 / 6

count7OrMore = 0
countExact8 = 0
for i in range(1, 7):
    for j in range(1, 7):
        total = i + j
        if total >= 7:
            count7OrMore += 1
        if total == 8:
            countExact8 += 1

probSum7OrMore = count7OrMore / 36
probSum8 = countExact8 / 36

countFirstGt4 = 0
countSecondOdd = 0
for first in [5, 6]:
    for second in range(1, 7):
        countFirstGt4 += 1
        if second % 2 == 1:
            countSecondOdd += 1

probConditional = countSecondOdd / countFirstGt4

print(f"Probability of even number is {probEven}")
print(f"Probability greater than 4 is {probGt4:.4f}")
print(f"Probability less than 3 is {probLt3:.4f}")
print(f"Probability sum ≥ 7 is {probSum7OrMore:.5f}")
print(f"Probability sum = 8 is {probSum8:.5f}")
print(f"Conditional probability is {probConditional}")