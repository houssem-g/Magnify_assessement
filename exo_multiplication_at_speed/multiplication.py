import pandas as pd


class fileMultiplication():
    def __init__ (self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
        
    def extract_and_multiplie(self):
        df1 = pd.read_csv(
            'exo_multiplication_at_speed/file_A.txt', sep=" ",header=None, names=['col_file_A'])
        df2 = pd.read_csv(
            'exo_multiplication_at_speed/file_B.txt', sep=" ",header=None, names=['col_file_B'])
        df = pd.concat([df1, df2], axis=1)
        df["res"] = df['col_file_A'] * df['col_file_B']
        return df["res"].to_csv(self.file3, header=None, index=None, sep='\t', mode='a')

file1 = 'exo_multiplication_at_speed/file_A.txt'
file2 = 'exo_multiplication_at_speed/file_B.txt'
file3 = 'exo_multiplication_at_speed/file_C.txt'
obj = fileMultiplication(file1, file2, file3)
obj.extract_and_multiplie()