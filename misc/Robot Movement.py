def robot_movement(s):
    # L, R, F
    x = 0
    y = 0
    direction = 0
    for command in s:
        if command == "F":
            if direction == 0:
                y += 1
            elif direction == 90:
                x += 1
            elif direction == 180:
                y -= 1
            elif direction == 270:
                x -= 1
        elif command == "R":
            direction += 90
            if direction == 360:
                direction = 0

        elif command == "L":
            direction -= 90
            if direction == -90:
                direction = 270
    back = abs(x) + abs(y)
    if x >= 0 and y >= 0 and direction in [270, 180]:
        back += 2
    elif x <= 0 and y >= 0 and direction in [90, 180]:
        back += 2
    elif x < 0 and y < 0 and direction in [0, 90]:
        back += 2
    elif x > 0 and y < 0 and direction in [0, 270]:
        back += 2
    return back


print(robot_movement("RF"))
