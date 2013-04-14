# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import pylab
import networkx as nx


#############################################
## ここからリンク関係

# リンク情報のみを反映させたグラフを作成
# int型を指定しないとノード名（ラベル）を単純な数値にしてくれない
G = nx.read_edgelist("edge.txt", nodetype=int)


#############################################
## ここから座標関係

# 座標情報をndarray型として読み込む
pos_array=numpy.loadtxt("coord.txt", dtype=int)

# 座標情報は辞書型で表す
pos = {}

# ndarrayの情報を「(x,y)」という値に変換する
for i in range(len(pos_array)):
	pos[i] = (pos_array[i][0], pos_array[i][1])


#############################################
## ここから描画関係

# 描画
nx.draw(G, pos)

# 保存
plt.savefig("test_fig.png")

plt.show()

