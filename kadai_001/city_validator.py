class CityValidator:
    def __init__(self, grid_data):
        """
        コンストラクタ
        :param grid_data: 5x5の高さデータ（リストのリスト）
        """
        self.grid = grid_data
        self.rows = len(grid_data)
        self.cols = len(grid_data[0])

    def check_sunlight(self):
        """
        要件A：日照権チェック
        南側の建物(r+1)が、自分(r)以上の高さの場合、日当たりが悪いと判定。
        :return: 該当する区画の座標リスト [(r, c), ...]
        """
        violations = []

        for r in range(self.rows - 1):  # 最南端はチェック不要
            for c in range(self.cols):
                current = self.grid[r][c]
                south = self.grid[r + 1][c]

                if south >= current:
                    violations.append((r, c))

        return violations

    def find_crowded_zones(self, threshold):
        """
        要件B：過密エリア特定
        自身＋東西南北の高さ合計がthresholdを超える区画を探す。
        :param threshold: 過密判定の基準値（整数）
        :return: 辞書 {(r, c): total_height, ...}
        """
        crowded_spots = {}

        for r in range(self.rows):
            for c in range(self.cols):
                total = self.grid[r][c]

                # 北
                if r - 1 >= 0:
                    total += self.grid[r - 1][c]
                # 南
                if r + 1 < self.rows:
                    total += self.grid[r + 1][c]
                # 西
                if c - 1 >= 0:
                    total += self.grid[r][c - 1]
                # 東
                if c + 1 < self.cols:
                    total += self.grid[r][c + 1]

                if total > threshold:
                    crowded_spots[(r, c)] = total

        return crowded_spots
