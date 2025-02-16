import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class COVIDDataVisualizer:
    def __init__(self, data_file='Moving AVERAGE.xlsx', predicted_file='Project1.csv'):
        """Initialize the visualizer with data files."""
        self.data = pd.read_excel(data_file)
        self.predicted_data = pd.read_csv(predicted_file)
        # Set style for all plots
        plt.style.use('seaborn')
        sns.set_palette("husl")
    
    def create_death_rate_plot(self):
        """1. Create death rate over time visualization."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Month'], self.data['Death Rate'], 
                marker='o', linestyle='-', color='blue')
        plt.title('COVID-19 Death Rate Over Time', pad=20)
        plt.xlabel('Month')
        plt.ylabel('Death Rate')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/death_rate_over_time.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_moving_average_plot(self):
        """2. Create 3-month moving average visualization."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['Month'][2:], self.data['3 Month Moving Average'][2:],
                marker='o', linestyle='-', color='green')
        plt.title('3-Month Moving Average of COVID-19 Death Rates', pad=20)
        plt.xlabel('Month')
        plt.ylabel('3-Month Moving Average')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/moving_average.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_predicted_vs_actual_plot(self):
        """3. Create predicted vs actual death rates visualization."""
        merged_data = pd.merge(
            self.data[['Month', 'Death Rate']], 
            self.predicted_data[['Month', 'Predicted_Death_Rate_Model_1']], 
            on='Month', how='left'
        )
        
        plt.figure(figsize=(10, 6))
        plt.plot(merged_data['Month'], merged_data['Death Rate'],
                label='Actual Death Rate', marker='o', linestyle='-', color='blue')
        plt.plot(merged_data['Month'], merged_data['Predicted_Death_Rate_Model_1'],
                label='Predicted Death Rate', marker='x', linestyle='--', color='red')
        plt.title('Comparison of Actual vs. Predicted Death Rates', pad=20)
        plt.xlabel('Month')
        plt.ylabel('Death Rate')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/predicted_vs_actual.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_cumulative_plot(self):
        """4. Create cumulative death rates visualization."""
        plt.figure(figsize=(10, 6))
        plt.bar(self.predicted_data['Month'], 
               self.predicted_data['CumulativeFrequency'],
               color='purple', alpha=0.7)
        plt.title('Cumulative Death Rates Over Time', pad=20)
        plt.xlabel('Month')
        plt.ylabel('Cumulative Death Rate')
        plt.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/cumulative_death_rates.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_confidence_intervals_plot(self):
        """5. Create confidence intervals visualization."""
        plt.figure(figsize=(10, 6))
        plt.errorbar(
            self.predicted_data['Month'],
            self.predicted_data['Predicted_Death_Rate_Model_1'],
            yerr=[
                self.predicted_data['Predicted_Death_Rate_Model_1'] - 
                self.predicted_data['LCL_Death_Rate_Model_1'],
                self.predicted_data['UCL_Death_Rate_Model_1'] - 
                self.predicted_data['Predicted_Death_Rate_Model_1']
            ],
            fmt='o', capsize=5,
            label='Predicted Death Rate with Confidence Intervals'
        )
        plt.title('Predicted Death Rates with Confidence Intervals', pad=20)
        plt.xlabel('Month')
        plt.ylabel('Death Rate')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/confidence_intervals.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_sector_impact_plot(self):
        """6. Create economic impact by sector visualization."""
        sectors = ['Agriculture', 'Aviation', 'Education', 'Retail', 'Tourism']
        impact_scores = [10, 20, 15, 12, 25]

        plt.figure(figsize=(10, 10))
        plt.pie(impact_scores, labels=sectors, autopct='%1.1f%%', 
                startangle=90, colors=sns.color_palette("husl", len(sectors)))
        plt.title('Economic Impact of COVID-19 by Sector', pad=20)
        plt.tight_layout()
        plt.savefig('visualizations/economic_impact_by_sector.png', dpi=300, bbox_inches='tight')
        plt.close()

    def create_all_visualizations(self):
        """Create all visualizations at once."""
        # Create visualizations directory if it doesn't exist
        import os
        os.makedirs('visualizations', exist_ok=True)
        
        # Generate all visualizations
        self.create_death_rate_plot()
        self.create_moving_average_plot()
        self.create_predicted_vs_actual_plot()
        self.create_cumulative_plot()
        self.create_confidence_intervals_plot()
        self.create_sector_impact_plot()
        
        print("All visualizations have been created in the 'visualizations' directory.")

if __name__ == "__main__":
    # Initialize visualizer
    visualizer = COVIDDataVisualizer()
    # Create all visualizations
    visualizer.create_all_visualizations()