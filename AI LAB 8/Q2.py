totalCards = 52
redCards = 26
hearts = 13
faceCards = 12
diamondFaceCards = 3
spadeFaceCards = 3
queens = 4

probRed = redCards / totalCards
probHeartGivenRed = hearts / redCards
probDiamondGivenFace = diamondFaceCards / faceCards
probSpadeOrQueenGivenFace = (spadeFaceCards + queens - 1) / faceCards

print(f"Probability of red card is {probRed:.4f}")
print(f"Probability of heart given red is {probHeartGivenRed:.4f}")
print(f"Probability of diamond given face is {probDiamondGivenFace:.4f}")
print(f"Probability of spade or queen given face is {probSpadeOrQueenGivenFace:.4f}")