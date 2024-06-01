import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import pandas as pd
import random

# Define a style dictionary
mpl_style = {
    # Figure settings
    'figure.figsize': (10, 6),
    'figure.facecolor': 'white',
    'figure.edgecolor': 'gray',
    'figure.autolayout': True,

    # Axes settings
    'axes.titlesize': 'x-large',
    'axes.titlepad': 15,
    'axes.labelsize': 'large',
    'axes.labelcolor': 'black',
    'axes.facecolor': 'white',
    'axes.edgecolor': 'lightgray',
    'axes.grid': True,
    'axes.axisbelow': True,
    'axes.linewidth': 1.2,

    # Grid settings
    'grid.color': 'gray',
    'grid.linestyle': '--',
    'grid.linewidth': 0.7,
    'grid.alpha': 0.5,

    # Font settings
    'font.size': 14,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif'],

    # Tick settings
    'xtick.color': 'black',
    'xtick.direction': 'out',
    'xtick.labelsize': 'medium',
    'ytick.color': 'black',
    'ytick.direction': 'out',
    'ytick.labelsize': 'medium',

    # Line settings
    'lines.linewidth': 2,
    'lines.markersize': 7,
    'lines.markerfacecolor': 'white',

    # Legend settings
    'legend.frameon': True,
    'legend.framealpha': 0.7,
    'legend.facecolor': 'white',
    'legend.edgecolor': 'gray',
    'legend.fancybox': True,
    'legend.shadow': True,
    'legend.fontsize': 'medium',

    # Color map
    'image.cmap': 'viridis',

    # Save settings
    'savefig.dpi': 100,
    'savefig.format': 'png',
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1
}
plt.rcParams.update(mpl_style)
plt.style.use('dark_background')


def init_database():
    return pd.DataFrame(data)

def plot_last_30_days_bar_chart(df):
    """
    Plots a bar chart of the 'value' column in the given DataFrame,
    showing data for the last 30 days.

    Args:
    df: pandas.DataFrame with 'date' and 'value' columns.
    """

    # Convert 'date' column to datetime objects if needed
    df['date'] = pd.to_datetime(df['date'])

    # Filter data for the last 30 days
    today = pd.Timestamp.now().normalize()
    thirty_days_ago = today - pd.Timedelta(days=30)
    df = df[df['date'] >= thirty_days_ago]

    # Group by day and sum the values
    daily_data = df.groupby(df['date'].dt.date)['value'].sum()

    # Plot the bar chart
    plt.figure(figsize=(8, 4.8))
    plt.bar(daily_data.index, daily_data.values, align='edge')
    plt.ylim(0, 30)
    plt.ylabel('Snesených vajec')
    plt.title('Snáška posledních 30 dnů')

    # Format x-ticks
    # formatted_dates = [date.strftime('%Y-%m-%d') for date in daily_data.index]
    # formatted_dates = [date.strftime('%m-%d') for date in daily_data.index]
    formatted_dates = [date.strftime('%d.%m.') for date in daily_data.index]
    plt.xticks(ticks=daily_data.index, labels=formatted_dates, rotation=60, ha='center')
    plt.tick_params(axis='x', which='both', length=0)  # Set length to 0 to remove ticks
    # Adjust x-axis limits to remove unwanted space
    if len(daily_data.index) > 0:
        plt.xlim([daily_data.index[0], daily_data.index[-1]+pd.DateOffset(days=1)])

    plt.tight_layout()
    # plt.show()
    plt.savefig('last_30_days_bar_chart.png')



mock_data = {'date': [date.today() - pd.DateOffset(days=i) for i in range(50)], 'value': [random.randint(0, 30) for i in range(50)]}
data = pd.DataFrame(mock_data)

print(data.head())

plot_last_30_days_bar_chart(data)




