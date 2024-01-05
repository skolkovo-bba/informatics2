#!/usr/bin/python3

name = "wiki_small.txt"

import os
import sys
import math

import array

import statistics

from collections import deque, Counter

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            n, _nlinks = map(int, f.readline().split())
            
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            count = 0

            for i in range(n):
                self._titles.append(f.readline().rstrip())
                self._sizes[i], self._redirect[i], how = map(int, f.readline().split())

                for _ in range(how):
                    self._links[count] = int(f.readline())
                    count += 1
                
                self._offset[i + 1] = count

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return sum(self._sizes)

    def is_redirect(self, _id):
        return bool(self._redirect[_id])

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]
    
    def bfs(self, title_from, title_to):
        s = self.get_id(title_from)
        e = self.get_id(title_to)

        n = len(self._titles)
        INF = n + 1
        q = deque()
        q.append(s)
        used = [False] * n
        d = [INF] * n
        p = [-2] * n 
        used[s] = True;
        p[s] = -1
        while q:
            v = q.popleft()
            for to in self.get_links_from(v):
                if not used[to]:
                    used[to] = True
                    q.append(to)
                    d[to] = d[v] + 1
                    p[to] = v
        
        if not used[e]:
            raise Exception("no path")
        else:
            path = [e]
            while path[-1] != s:
                path.append(p[path[-1]])
            return path[::-1]
    
    def __len__(self):
        return len(self._titles)


if __name__ == '__main__':

    

    if os.path.isfile(name):
        wg = WikiGraph()
        wg.load_from_file(name)

        print("Запускаем поиск в ширину")
        path = wg.bfs("Python", "Список_файловых_систем")
        print("Поиск закончен. Найден путь:")
        for p in path:
            print(wg.get_title(p))
        
        how = len([id for id in range(len(wg)) if wg.is_redirect(id)])
        print(f"Количество статей с перенаправлением: {how} ({how / len(wg) * 100} %)")

        red = [wg.get_number_of_links_from(id) for id in range(len(wg))]
        print(f"Минимальное количество ссылок из статьи: {min(red)}")
        print(f"Количество статей с минимальным количеством ссылок: {red.count(min(red))}")
        print(f"Максимальное количество ссылок из статьи: {max(red)}")
        print(f"Количество статей с максимальным количеством ссылок: {red.count(max(red))}")
        print(f"Статья с наибольшим количеством ссылок: {wg.get_title(red.index(max(red)))}")
        print(f"Среднее количество ссылок в статье: {statistics.mean(red)} (ср. откл. {statistics.stdev(red)})")

        links_on = array.array('L', [0] * len(wg))
        for i in range(len(wg)):
            for out in wg.get_links_from(i):
                links_on[out] += 1
        
        print(f"Минимальное количество ссылок на статью: {min(links_on)}")
        print(f"Количество статей с минимальным количеством внешних ссылок: {links_on.count(min(links_on))}")
        print(f"Максимальное количество ссылок на статью: {max(links_on)}")
        print(f"Количество статей с максимальным количеством внешних ссылок: {links_on.count(max(links_on))}")
        print(f"Статья с наибольшим количеством внешних ссылок: {wg.get_title(links_on.index(max(links_on)))}")
        print(f"Среднее количество внешних ссылок на статью: {statistics.mean(links_on)} (ср. откл. {statistics.stdev(links_on)})")

        send = array.array('L', [0] * len(wg))
        for i in range(len(wg)):
            if wg.is_redirect(i):
                for out in wg.get_links_from(i):
                    send[out] += 1
        print(f"Минимальное количество перенаправлений на статью: {min(send)}")
        print(f"Количество статей с минимальным количеством внешних перенаправлений: {send.count(min(send))}")
        print(f"Максимальное количество ссылок на статью: {max(send)}")
        print(f"Количество статей с максимальным количеством внешних ссылок: {send.count(max(send))}")
        print(f"Статья с наибольшим количеством внешних ссылок: {wg.get_title(send.index(max(send)))}")
        print(f"Среднее количество внешних ссылок на статью: {statistics.mean(send)} (ср. откл. {statistics.stdev(send)})")

    else:
        print('Файл с графом не найден')
        sys.exit(-1)
