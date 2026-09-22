import pandas as pd

# Load application history
data = pd.read_csv("applications.csv")

if len(data) == 0:
    print("⚠️ No applications found in applications.csv. Please add some data first.")
else:
    # Success rate
    success_rate = (data['Reply'].value_counts().get('Positive', 0) / len(data)) * 100
    print("Success Rate:", round(success_rate, 2), "%")

    # Companies with most positive replies
    print("\nCompanies with most positive replies:")
    print(data[data['Reply'] == 'Positive']['Company'].value_counts())

    # Resume versions with most positive replies
    print("\nResume versions with most positive replies:")
    print(data[data['Reply'] == 'Positive']['Resume Version'].value_counts())
