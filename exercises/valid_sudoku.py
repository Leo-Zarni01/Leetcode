from typing import Dict, List
class Solution:
    def make_subboxes(self, board: List[List[str]]) -> Dict[str, List[str]]:
        sub_boxes = {}
        sub_boxes['A'] = [board[0][0:3]] + [board[1][0:3]] + [board[2][0:3]]
        sub_boxes['B'] = [board[0][3:6]] + [board[1][3:6]] + [board[2][3:6]]
        sub_boxes['C'] = [board[0][6:9]] + [board[1][6:9]] + [board[2][6:9]]

        sub_boxes['D'] = [board[3][0:3]] + [board[4][0:3]] + [board[5][0:3]]
        sub_boxes['E'] = [board[3][3:6]] + [board[4][3:6]] + [board[5][3:6]]
        sub_boxes['F'] = [board[3][6:9]] + [board[4][6:9]] + [board[5][6:9]]

        sub_boxes['G'] = [board[6][0:3]] + [board[7][0:3]] + [board[8][0:3]]
        sub_boxes['H'] = [board[6][3:6]] + [board[7][3:6]] + [board[8][3:6]]
        sub_boxes['I'] = [board[6][6:9]] + [board[7][6:9]] + [board[8][6:9]]
        return sub_boxes

    def print_subboxes(self, subboxes: Dict[str, List[str]]):
        for each_subboxes in subboxes.items():
            print(each_subboxes)
            print()

    def contains_duplicate(self, nums: List[str]) -> bool:
        nums.sort()
        curr_index = 0
        neighbor = 1
        while curr_index < len(nums) - 1:
            if nums[curr_index] != ".":
                if nums[curr_index] == nums[neighbor]:
                    return True
            curr_index += 1
            neighbor += 1
        return False

    def combine_lists(self, subbox: List[List[str]]) -> List[str]:
        final_list = []
        for each_list in subbox:
            final_list += each_list
        return final_list

    def check_subboxes(self, subboxes: Dict[str, List[str]]) -> bool:
        for each_subboxes in subboxes.values():
            combined_list = self.combine_lists(each_subboxes) 
            print("Combined_list: ", combined_list)
            duplicate_checker = self.contains_duplicate(combined_list)
            if duplicate_checker:
                print("Duplicate found")
                return False
            ## print(each_subboxes)
        return True
    
    def check_rows(self, subboxes: Dict[str, List[str]]) -> bool:
        first_row = subboxes['A'][0] + subboxes['B'][0] + subboxes['C'][0]
        second_row = subboxes['A'][1] + subboxes['B'][1] + subboxes['C'][1]
        third_row = subboxes['A'][2] + subboxes['B'][2] + subboxes['C'][2]

        fourth_row = subboxes['D'][0] + subboxes['E'][0] + subboxes['F'][0]
        fifth_row = subboxes['D'][1] + subboxes['E'][1] + subboxes['F'][1]
        sixth_row = subboxes['D'][2] + subboxes['E'][2] + subboxes['F'][2]

        seventh_row = subboxes['G'][0] + subboxes['H'][0] + subboxes['I'][0]
        eight_row = subboxes['G'][1] + subboxes['H'][1] + subboxes['I'][1]
        ninth_row = subboxes['G'][2] + subboxes['H'][2] + subboxes['I'][2]

        rows = [first_row, second_row, third_row, fourth_row, fifth_row, sixth_row, seventh_row, eight_row, ninth_row]
        for each_rows in rows:
            duplicate_checker = self.contains_duplicate(each_rows)
            if duplicate_checker:
                return False
        return True
    
    def make_subboxes_col(self, board: List[List[str]]) -> Dict[str, List[str]]:
        subboxes_col = {}
        subboxes_col["A"] = [[board[0][0], board[1][0], board[2][0]], [board[0][1], board[1][1], board[2][1]] , [board[0][2], board[1][2], board[2][2]]]

        subboxes_col["B"] = [[board[0][3], board[1][3], board[2][3]] , [board[0][4], board[1][4], board[2][4]], [board[0][5], board[1][5], board[2][5]]]
        subboxes_col["C"] = [[board[0][6], board[1][6], board[2][6]] , [board[0][7], board[1][7], board[2][7]] , [board[0][8], board[1][8], board[2][8]]]

        subboxes_col["D"] = [[board[3][0], board[4][0], board[5][0]] , [board[3][1], board[4][1], board[5][1]] , [board[3][2], board[4][2], board[5][2]]]
        subboxes_col["E"] = [[board[3][3], board[4][3], board[5][3]] , [board[3][4], board[4][4], board[5][4]] , [board[3][5], board[4][5], board[5][5]]]
        subboxes_col["F"] = [[board[3][6], board[4][6], board[5][6]] , [board[3][7], board[4][7], board[5][7]] , [board[3][8], board[4][8], board[5][8]]]

        subboxes_col["G"] = [[board[6][0], board[7][0], board[8][0]] , [board[6][1], board[7][1], board[8][1]] , [board[6][2], board[7][2], board[8][2]]]
        subboxes_col["H"] = [[board[6][3], board[7][3], board[8][3]] , [board[6][4], board[7][4], board[8][4]] , [board[6][5], board[7][5], board[8][5]]]
        subboxes_col["I"] = [[board[6][6], board[7][6], board[8][6]] , [board[6][7], board[7][7], board[8][7]] , [board[6][8], board[7][8], board[8][8]]]
        return subboxes_col
    
    def check_columns(self, subboxes_col: Dict[str, List[str]]) -> bool:
        first_column = subboxes_col["A"][0] + subboxes_col["D"][0] + subboxes_col["G"][0]
        second_column = subboxes_col["A"][1] + subboxes_col["D"][1] + subboxes_col["G"][1]
        third_column = subboxes_col["A"][2] + subboxes_col["D"][2] + subboxes_col["G"][2]

        fourth_column = subboxes_col["B"][0] + subboxes_col["E"][0] + subboxes_col["H"][0]
        fifth_column = subboxes_col["B"][1] + subboxes_col["E"][1] + subboxes_col["H"][1]
        sixth_column = subboxes_col["B"][2] + subboxes_col["E"][2] + subboxes_col["H"][2]
        print("sixth column is: ", sixth_column)

        seventh_column = subboxes_col["C"][0] + subboxes_col["F"][0] + subboxes_col["I"][0]
        print(f"C0: {subboxes_col['C'][0]} | F0: {subboxes_col['F'][0]} | I0: {subboxes_col['I'][0]}")
        print("seventh column is: ", seventh_column)
        eight_column = subboxes_col["C"][1] + subboxes_col["F"][1] + subboxes_col["I"][1]
        ninth_column = subboxes_col["C"][2] + subboxes_col["F"][2] + subboxes_col["I"][2]

        columns = [first_column, second_column, third_column, fourth_column, fifth_column, sixth_column, seventh_column, eight_column, ninth_column]

        for each_column in columns:
            print("current column is: ", each_column)
            duplicate_checker = self.contains_duplicate(each_column)
            if duplicate_checker:
                print("OMGGGGGG DUPLICATE")
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subboxes = self.make_subboxes(board)
        subboxes_valid = self.check_subboxes(subboxes)
        if not subboxes_valid:
            return False
        
        rows_checker = self.check_rows(subboxes)
        if not rows_checker:
            return False 

        subboxes_columns = self.make_subboxes_col(board)
        columns_checker = self.check_columns(subboxes_columns)
        if not columns_checker:
            return False 
        return True 
        
sudoku_1 = Solution()
board = [[".",".","5",".",".",".",".",".","6"],[".",".",".",".","1","4",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","9","2",".","."],["5",".",".",".",".","2",".",".","."],[".",".",".",".",".",".",".","3","."],[".",".",".","5","4",".",".",".","."],["3",".",".",".",".",".","4","2","."],[".",".",".","2","7",".","6",".","."]]


subboxes = sudoku_1.make_subboxes(board)
# sudoku_1.check_subboxes(subboxes)
sudoku_1.print_subboxes(subboxes)
sudoku_1.check_rows(subboxes)
columns = sudoku_1.make_subboxes_col(board)
print(sudoku_1.check_columns(columns))

# sudoku_2 = Solution()
# board_2 = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# subboxes_2 = sudoku_2.make_subboxes(board_2)
# sudoku_2.check_subboxes(subboxes_2)
# sudoku_2.print_subboxes(subboxes_2)

# sudoku_3 = Solution()
# board_3 = [["4","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

# subboxes_3 = sudoku_3.make_subboxes(board_3)
# # sudoku_1.check_subboxes(subboxes)
# sudoku_3.print_subboxes(subboxes_3)
# sudoku_3.check_rows(subboxes_3)
# columns_3 = sudoku_3.make_subboxes_col(board_3)
# sudoku_3.check_columns(columns_3)