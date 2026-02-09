CityValidator (AI City Development Mission)
Overview

This program validates city blocks based on building height data represented as a 2D array.
It checks urban areas from two perspectives:

Requirement A: Sunlight Rights Validation

Requirement B: Crowded Area Detection

This project was implemented as a school assignment to practice 2D array handling, boundary checking, and the use of tuples and dictionaries in Python.

Technologies & Concepts

Python 3.x

2D arrays (list of lists)

for-loops

Conditional statements (if)

Tuples (row, col)

Dictionaries (dict)

Data Structure

City data is represented as a 5×5 two-dimensional list:

test_area = [
    [0, 10, 5, 0, 8],
    [0, 12, 6, 0, 8],
    [5, 15, 0, 0, 10],
    [5, 5,  0, 0, 5],
    [0, 0,  0, 0, 0]
]


Rows represent north to south

Columns represent west to east

Values indicate building height (0 means an empty lot)

Elements are accessed using grid[row][col].

Class Design
CityValidator Class
Constructor
CityValidator(grid_data)


grid_data: 2D list containing building height data

Stores the number of rows and columns internally

Requirement A: Sunlight Rights Check
Description

For each block, the program checks whether the southern neighbor (row + 1) has a height greater than or equal to the current block.
If so, the block is considered to have a sunlight issue.

Method
check_sunlight()

Return Value
[(row, col), ...]


A list of coordinates where sunlight rights are violated

Implementation Notes

The southernmost row is excluded because it has no southern neighbor

Boundary-safe logic is used to avoid IndexError

Requirement B: Crowded Area Detection
Description

For each block, the program calculates the total height of:

The current block

North

South

East

West neighbors

If the total exceeds the specified threshold, the block is marked as a crowded area.

Method
find_crowded_zones(threshold)

Parameters

threshold: Integer value used as the crowded-area criterion

Return Value
{ (row, col): total_height, ... }


Key: Block coordinates as a tuple

Value: Total building height

Implementation Notes

Each neighboring block is checked individually to ensure it exists

Tuples are used as dictionary keys to represent coordinates clearly

How to Run
python city_validator.py


The program outputs:

A list of blocks with sunlight violations

A dictionary of crowded areas and their total heights

What I Learned / Challenges

A 2D array requires row-first, column-second access

Boundary handling is critical when checking neighboring cells

Tuples are immutable and suitable as dictionary keys

Writing clear conditional logic helps prevent runtime errors

Handling edge cases (especially at the borders of the grid) was the most challenging part, but breaking the logic into small steps made it manageable.

Conclusion

Through this assignment, I gained a solid understanding of 2D array operations and safe boundary-aware logic in Python.
This experience also reinforced the importance of writing readable and maintainable code.

-------------------------Japanese-------------------------------

CityValidator（AI都市開発ミッション）
概要

本プログラムは、2次元配列で表現された都市の建物高さデータをもとに、
以下の2つの観点から都市区画をチェックするための検証ツールです。

要件A：日照権チェック

要件B：過密エリアの検出

スクール課題として、2次元配列の操作・境界条件の扱い・辞書とタプルの理解を目的に実装しました。

使用技術・前提知識

Python 3.x

2次元配列（リストのリスト）

for ループ

条件分岐（if 文）

タプル (row, col)

辞書（dict）

データ構造について

都市データは、次のような 5×5 の2次元配列で表現されます。

test_area = [
    [0, 10, 5, 0, 8],
    [0, 12, 6, 0, 8],
    [5, 15, 0, 0, 10],
    [5, 5,  0, 0, 5],
    [0, 0,  0, 0, 0]
]


行（row）：北 → 南

列（col）：西 → 東

値：建物の高さ（0 は空き地）

grid[row][col] の形式でアクセスします。

クラス構成
CityValidator クラス
コンストラクタ
CityValidator(grid_data)


grid_data：都市の高さデータ（2次元配列）

行数・列数を内部で保持します

要件A：日照権チェック
概要

各区画について、南側の区画（row + 1）が自分以上の高さの場合、
日照権侵害と判定します。

メソッド
check_sunlight()

戻り値
[(row, col), ...]


日照権侵害が発生している区画の座標リスト

実装上の工夫

最南端の行は南側が存在しないため、チェック対象外

配列の範囲外参照（IndexError）を防ぐ設計

要件B：過密エリア検出
概要

各区画について、以下の合計値を計算します。

自身

北

南

東

西

合計が threshold を超える場合、過密エリアと判定します。

メソッド
find_crowded_zones(threshold)

引数

threshold：過密と判定する基準値（整数）

戻り値
{ (row, col): total_height, ... }


キー：区画の座標（タプル）

値：高さの合計

実装上の工夫

上下左右が存在するかを個別に判定

タプルを辞書のキーとして利用し、座標管理を簡潔に表現

実行方法
python city_validator.py


実行すると、以下が表示されます。

日照権侵害のある区画一覧

過密エリアとその高さ合計

学んだこと・難しかった点

2次元配列では 「行 → 列」 の順でアクセスする必要があること

上下左右の判定では、配列の端の処理が最重要であること

タプルは変更不可なため、辞書のキーとして安全に使えること

処理をシンプルに書くことで、IndexError を未然に防げること

特に境界条件の扱いが難しく感じましたが、
一つずつ条件を分けて考えることで、正しく実装することができました。

まとめ

本課題を通して、
2次元配列の基礎操作と、安全なロジック設計の重要性を理解できました。
今後は処理の共通化や拡張にも挑戦していきたいです。
