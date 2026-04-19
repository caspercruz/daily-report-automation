import pandas as pd

def load_data():
    try:
        data = {
            "name": ["A", "B", "C"],
            "value": [10, 20, 30]
        }
        df = pd.DataFrame(data)
        return df

    except Exception as e:
        print("Data loading failed:", e)
        raise