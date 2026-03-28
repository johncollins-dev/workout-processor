# workout-processor.py
if __name__ == "__main__":
    import sys
    import pandas as pd
    data = pd.read_excel(sys.argv[1], index_col=0)
    print(data)
