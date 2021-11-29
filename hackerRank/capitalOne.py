string = "reuonnoinfe"

lookup = [["zero", "z", "0"],
          ["two", "w", "2"],
          ["four", "u", "4"],
          ["six", "x", "6"],
          ["eight", "g", "8"],
          ["one", "o", "1"],
          ["three", "t", "3"],
          ["five", "f", "5"],
          ["seven", "s", "7"],
          ["nine", "i", "9"]
          ]

ans = ""
i = 0
while i < len(lookup):
    if lookup[i][1] in string:
        ans += lookup[i][2]
        for char in lookup[i][0]:
            string = string.replace(char, "")
    else:
        i += 1
print(int(ans.sorted))
