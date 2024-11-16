import random


def get_robot_choice():
    return random.choice(["石头", "剪刀", "布"])


def determine_winner(player_choice, robot_choice):
    if player_choice == robot_choice:
        return "平局"
    elif (player_choice == "石头" and robot_choice == "剪刀") or \
            (player_choice == "剪刀" and robot_choice == "布") or \
            (player_choice == "布" and robot_choice == "石头"):
        return "用户赢"
    else:
        return "机器人赢"


def main():
    player_score = 0
    robot_score = 0

    while player_score < 2 and robot_score < 2:
        player_choice = input("请输入您的选择（石头/剪刀/布）：")
        robot_choice = get_robot_choice()
        print(f"机器人选择了：{robot_choice}")

        result = determine_winner(player_choice, robot_choice)
        if result == "用户赢":
            player_score += 1
            print("你赢了这一局！")
        elif result == "机器人赢":
            robot_score += 1
            print("机器人赢了这一局！")
        else:
            print("这一局平局！")

        print(f"当前比分 - 用户: {player_score}, 机器人: {robot_score}")

    if player_score == 2:
        print("恭喜你，获得胜利！")
    else:
        print("很遗憾，机器人获胜！")


if __name__ == "__main__":
    main()
