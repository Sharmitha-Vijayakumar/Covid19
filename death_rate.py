plt.figure(figsize=(10, 6))
plt.errorbar(
    predicted_data['Month'],
    predicted_data['Predicted_Death_Rate_Model_1'],
    yerr=[
        predicted_data['Predicted_Death_Rate_Model_1'] - predicted_data['LCL_Death_Rate_Model_1'],
        predicted_data['UCL_Death_Rate_Model_1'] - predicted_data['Predicted_Death_Rate_Model_1']
    ],
    fmt='o',
    capsize=5,
    label='Predicted Death Rate with Confidence Intervals'
)
plt.title('Predicted Death Rates with Confidence Intervals')
plt.xlabel('Month')
plt.ylabel('Death Rate')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()