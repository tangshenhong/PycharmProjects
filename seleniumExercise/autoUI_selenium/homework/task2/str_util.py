'''
from github to get unicode char width:
https://github.com/urwid/urwid/blob/master/urwid/old_str_util.py
'''


widths = [
    (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
    (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
    (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
    (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
    (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
    (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
    (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
    (120831, 1), (262141, 2), (1114109, 1),
]

def get_width( o ):
    """Return the screen column width for unicode ordinal o."""
    global widths
    if o == 0xe or o == 0xf:
        return 0
    for num, wid in widths:
        if o <= num:
            return wid
    return 1

'''
自定义
'''
def get_str_width(s):
    '''

    :param s: 接收一个字符串
    :return: 返回这个字符串的显示长度
    '''
    try:
        return sum([get_width(ord(c)) for c in s])
    except:
        print(type(s))
        return 20

if __name__ == '__main__':
    print(get_str_width('光明大道2019（电影《燃点》主题..'))
