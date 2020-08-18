from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass
    def __init__(self, capacity:int) -> None:
        self.no = 0  # 現在のデータ数
        self.front = 0  # 先頭要素カーソル
        self.rear = 0   # 末尾要素カーソル
        self.capacity = capacity  # キューの容量
        self.que = [None]*capacity   # キューの本体

    def __len__(self) -> int:
        """キューに押し込まれているデータ数を返す"""
        return self.no

    def is_empty(self) -> bool:
        """キューは空であるか"""
        return self.no <= 0

    def is_full(self)-> bool:
        """キューは満杯か"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """データxをエンキュー"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """データをデキュー"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front +=  1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self)-> Any:
        """データをピーク（先頭データを覗く）"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value:Any)-> Any:
        """キューからvalueを探して添字（見つからなければ-1）を返す"""
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any)-> Any:
        """キューに含まれるvalueの個数を返す"""
        c = 0
        for i in range(self.no):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        """キューを空にする"""
        self.no = self.front = self.rear = 0

    def dump(self)-> None:
        if self.is_empty:
            print("Nothing is inside")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
                print()

from enum import Enum
Menu = Enum('Menu', ['エンキュー', 'デキュー', 'ピーク', '探索', 'ダンプ',
                     '1終了'])
def select_menu()->Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'現在のデータ数：{len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.エンキュー:
        x = int(input('データ:'))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print("キューが満杯です。")
    elif menu == Menu.デキュー:  # デキュー
        try:
            x = q.deque()
            print(f'デキューしたデータは{x}です。')
        except FixedQueue.Empty:
            print('キューが空です。')

    elif menu == Menu.ピーク:  # ピーク
        try:
            x = q.peek()
            print(f'ピークしたデータは{x}です。')
        except FixedQueue.Empty:
            print('キューが空です。')

    elif menu == Menu.探索:  # 探索
        x = int(input('値：'))
        if x in q:
            print(f'{q.count(x)}個含まれ先頭の位置は{q.find(x)}です。')
        else:
            print('その値は含まれません。')

    elif menu == Menu.ダンプ:  # ダンプ
        q.dump()

    else:
        break
