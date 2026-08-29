n = int(input("Enter the number of houses: "))

money = []

for i in range(n):
    amount = int(input(f"Enter amount in house {i + 1}: "))
    money.append(amount)

if n == 0:
    print("Maximum amount:", 0)
elif n == 1:
    print("Maximum amount:", money[0])
else:
    dp = [0] * n

    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    print("Maximum amount:", dp[n - 1])
