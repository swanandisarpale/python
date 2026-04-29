import pandas as pd
import matplotlib.pyplot as plt
import json

def main():
    line = "-" * 64

    # -------------------------------
    # LOADing JSON FILE
    # -------------------------------
    with open("data.json", "r") as file:
        data = json.load(file)

    # Converting JSON → DataFrame
    df = pd.DataFrame(data)

    # Converting DataFrame → CSV
    df.to_csv("output.csv", index=False)

    print(line)
    print("JSON successfully converted to CSV")
    print(line)

    
    print(line)
    print("First 5 Entries")
    print(line)
    print(df.head(5))

    
    print(line)
    print("Dataset Info")
    print(line)
    print(df.info())


    print(line)
    print("Statistics")
    print(line)
    print(df.describe(include="all", percentiles=[0.25, 0.5, 0.75]))

    # -------------------------------
    # GROUPING 
    # -------------------------------
    dist_group = df.groupby("State Name")

    states = []
    state_count = []

    for i in dist_group:
        states.append(i[0])          # state name
        state_count.append(len(i[1]))  # number of rows per state

    # -------------------------------
    # PERCENTAGE CALCULATION
    # -------------------------------
    total = len(df)   # dynamic 

    state_count_percentage = []

    for num in state_count:
        k = (num / total) * 100
        state_count_percentage.append(k)

    # -------------------------------
    # PIE CHART
    # -------------------------------
    plt.figure(figsize=(10, 10))
    plt.pie(state_count_percentage, labels=states, autopct="%0.1f%%")
    plt.title("State-wise Distribution (%)")
    plt.show()

    # -------------------------------
    # BAR GRAPH
    # -------------------------------
    plt.figure(figsize=(15, 10))
    plt.bar(states, state_count_percentage)
    plt.xticks(rotation=90)
    plt.xlabel("States")
    plt.ylabel("Percentage")
    plt.title("State-wise Percentage Distribution")
    plt.show()


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    main()