def process_data(df):
    overdue = df[df["status"] == "pending"].sort_values(by="amount", ascending=False)

    return {
        "total": df["amount"].sum(),
        "paid": df[df["status"] == "paid"]["amount"].sum(),
        "pending": df[df["status"] == "pending"]["amount"].sum(),
        "top_defaulters": overdue.head(5)
    }