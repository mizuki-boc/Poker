'''
カードの定義
- スート
    - ハート = "H"
    - ダイヤ = "D"
    - クローバ = "C"
    - スペード = "S"
- 番号
    - 1~9 = 1~9
    - 10 = T
    - J, Q, K = J, Q, K
- 例
    - HA = ハートのエース
    - DQ = ダイヤのクイーン
    - C3 = クローバーの３
- hand: ["C3", "HA"] みたいに扱いたい．
'''
# ハンドの仮想スコア定義．ハイカードはハイカードの番号を仮想スコアとする．
score = {
    "ROYAL_STRAIGHT_FLUSH"  : 100,
    "STRAIGHT_FLUSH"        : 90,
    "FOUR_OF_A_KIND"        : 80,
    "FULL_HOUSE"            : 70,
    "FLUSH"                 : 60,
    "STRAIGHT"              : 50,
    "THREE_OF_A_KIND"       : 40,
    "TWO_PAIR"              : 30,
    "PAIR"                  : 20,
}
# 仮想ナンバースコア
num = {
    "A": 140,
    "K": 130,
    "Q": 120,
    "J": 110,
    "T": 100,
    "9": 90,
    "8": 80,
    "7": 70,
    "6": 60,
    "5": 50,
    "4": 40,
    "3": 30,
    "2": 20,
}
# 仮想スートスコア　S > H > D > C
suit = {
    "S": 4,
    "H": 3,
    "D": 2,
    "C": 1,
}

def calc_winrate(p1_hand, p2_hand, field_card):
    '''
    2プレーヤーのハンドと，場のカード(枚数問わない)で，どちらが勝者か判定する関数
    '''
    pass

def set_besthand(hand, field_card):
    '''
    ハンドと場のカード(４枚以上)から，最適な組み合わせを計算する関数
    与えられたカードから，最適な組み合わせを計算するより，
    フロップの段階(５枚確定された段階)から取捨選択する方法の方がよくね？
    '''
    all_card = hand + field_card
    # フロップはリターン
    if len(all_card) == 5:
        return all_card

    # フラッシュかどうか
    suit_of_card = [x[0] for x in all_card]
    spade_num = suit_of_card.count("S")
    heart_num = suit_of_card.count("H")
    diamond_num = suit_of_card.count("D")
    club_num = suit_of_card.count("C")
    # ストレートかどうか
    # ペアがあるかどうか
        

def calc_handrank(hand):
    '''
    ハンドの役(rank)を計算する関数
    '''
    pass

def noname():# todo 名前決める
    '''
    hand(５枚) に対して，カード(１枚)を加えた方が良いかどうか判断
    最適なハンドをリターンする
    '''
    pass

def sort_card(cards):
    '''
    カードをソート(昇順)する関数
    S > H > D > C
    '''
    sorted_card = []
    ans = []
    for i in range(len(cards)):
        sorted_card.append(suit[cards[i][0]] + num[cards[i][1]])
    sorted_card.sort()
    # 仮想番号から，スートと番号の記号に変換する
    for c in sorted_card:
        # スート検索
        s = inverse_lookup(suit, c % 10)
        # 番号検索
        n = inverse_lookup(num, c // 10 * 10)
        ans.append(s + n)
    return ans

def inverse_lookup(d, x):
    '''
    辞書逆引き関数
    '''
    for k,v in d.items():
        if x == v:
            return k

if __name__ == "__main__":
    a = ["HA", "C2", "D9", "ST", "H9", "H8"]
    print(sort_card(a))