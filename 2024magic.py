def rotate_list(lst, n):
    for _ in range(n):
        lst.append(lst.pop(0))
    return lst
def insert_to_middle(lst, n):
    mid = len(lst) // 2
    return lst[n:mid] + lst[:n] + lst[mid:]


# 随机拿取四张牌
cards = input('请输入四个数字或字母，以空格分隔：\n').split()
print('你选择的牌是：')
print(cards)
# 将牌对折后撕开叠在一起
input('现在将牌对折后撕开，得到的列表是(按回车继续)：')
cards *= 2
print(cards)
# 将名字字数的牌依次放到底部
name_len = int(input('请输入你的名字字数：'))
print('将名字字数的牌依次放到底部：')
cards = rotate_list(cards, name_len)  # 此操作不会改变牌的顺序
print(cards)
# 最上面三张插进卡片中间
input('将最上面的三张牌插入到卡片中间(按回车继续)')
cards = insert_to_middle(cards, 3)     # 此时第一张和最后一张一定相同
print(cards)
# 将第一张拿出，藏起来
input('拿出第一张牌，藏起来(按回车继续)')
pop_card = cards.pop(0)
print('你藏起来的牌是：' + pop_card)    # 此时藏起来的是第一张，后续无论如何操作，只需控制最后一张的位置即可
# 南方人拿一张，北方人拿两张，不确定拿三张
region = int(input('请输入你的区域代号（南方人:1，北方人:2，不确定:3）：')) 
cards = insert_to_middle(cards, region)
print('将拿取数量的牌插入到中间：')
print(cards)
# 男生拿一张，女生拿两张，扔掉
gender = int(input('请输入性别代号（男生:1，女生:2）'))
if gender == 1:
    cards.pop(0)
elif gender == 2:
    cards.pop(0)
    cards.pop(0)
print('男生扔掉一张牌，女生扔掉两张牌：')
print(cards)
# "见证奇迹的时刻" 每念到一个字将第一张放到最下方
input('见证奇迹的时刻(按回车继续)')
cards = rotate_list(cards, 7)
print(cards)
# 好运留下来，烦恼丢出去
while len(cards) > 1:
    input('好运留下来，烦恼丢出去(按回车继续)')
    cards.append(cards.pop(0))
    cards.pop(0)
    print(cards)
print('你剩下的牌是：' + cards[0])
print('你藏起来的牌是：' + pop_card)
if cards[0] == pop_card:
    print('恭喜你！成功把牌都对上了！祝你新年快乐！')
