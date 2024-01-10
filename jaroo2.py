rooms = int(input("خانه شما چند اتاق دارد؟ "))

# ایجاد اتاق ها و پر کردن از خانه های کثیف یا تمیز
room_sizes = []
for i in range(rooms):
    length = int(input(f"عرض اتاق {i+1} چند متر است؟ "))
    width = int(input(f"طول اتاق {i+1} چند متر است؟ "))
    room = []
    for j in range(length):
        row = []
        for k in range(width):
            user_input = input(f"آیا محل ({j+1}, {k+1}) در اتاق {i+1} کثیف است؟ (y/n) ")
            if user_input.lower() == "n":
                row.append("c")
            else:
                row.append("d")
        room.append(row)

    room_sizes.append(room)


# چاپ ارایه قبل از تمیز کردن
print("خانه قبل از تمیز کردن:")
for i in range(rooms):
    print(f"اتاق {i+1}:")
    for j in range(len(room_sizes[i])):
        for k in range(len(room_sizes[i][j])):
            print(room_sizes[i][j][k], end=" ")
        print()
    print()

# تمیز کردن اتاق ها
for i in range(rooms):
    print(f"اتاق {i+1}:")
    for j in range(len(room_sizes[i])):
        for k in range(len(room_sizes[i][j])):
            room_sizes[i][j][k] = "c"
            print(f"({j+1}, {k+1}): تمیز شد")
    print()

# چاپ ارایه پس از تمیز کردن
print("خانه تر و تمیز خدمت شما:")
for i in range(rooms):
    print(f"اتاق {i+1}:")
    for j in range(len(room_sizes[i])):
        for k in range(len(room_sizes[i][j])):
            print(room_sizes[i][j][k], end=" ")
        print()
    print()