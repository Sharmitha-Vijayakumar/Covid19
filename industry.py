sectors = ['Agriculture', 'Aviation', 'Education', 'Retail', 'Tourism']
impact_scores = [10, 20, 15, 12, 25]  # Example scores

plt.figure(figsize=(8, 8))
plt.pie(impact_scores, labels=sectors, autopct='%1.1f%%', startangle=90)
plt.title('Economic Impact of COVID-19 by Sector')
plt.tight_layout()
plt.show()