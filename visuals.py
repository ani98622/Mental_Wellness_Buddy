from datetime import datetime, timedelta
from matplotlib.ticker import MaxNLocator
from matplotlib.figure import Figure
import seaborn as sns

def generate_bar_chart(result, title="Issue Statistics"):
    columns = list(result.keys())
    critical_counts = [result[col][0] for col in columns]
    moderate_counts = [result[col][1] for col in columns]

    sns.set(style="whitegrid")
    
    fig = Figure(figsize=(12, 7))  
    ax = fig.subplots()
    
    width = 0.4  
    bar_positions = range(len(columns))
    
    ax.bar(bar_positions, critical_counts, label="Critical", color=sns.color_palette("Reds", 5)[3], width=width)
    ax.bar(bar_positions, moderate_counts, label="Moderate", 
           bottom=critical_counts, color=sns.color_palette("Blues", 5)[3], width=width)

    ax.set_ylabel('Number of Cases', fontsize=14)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(columns, rotation=45, ha="right", fontsize=12)

    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(True, which='major', axis='y', linestyle='--', alpha=0.7)

    for i, (crit, mod) in enumerate(zip(critical_counts, moderate_counts)):
        ax.text(i, crit / 2, f'{crit}', ha='center', va='center', color='white', fontweight='bold')
        ax.text(i, crit + (mod / 2), f'{mod}', ha='center', va='center', color='white', fontweight='bold')

    ax.legend(loc="upper right", fontsize=12, title="Severity Level", title_fontsize=13)
    fig.tight_layout()

    return fig

def get_date_range(option):
    today = datetime.today()
    if option == "Last 7 Days":
        from_date = today - timedelta(days=7)
    elif option == "Last 30 Days":
        from_date = today - timedelta(days=30)
    elif option == "This Month":
        from_date = today.replace(day=1)
    elif option == "Last Month":
        first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        from_date = first_day_last_month
        today = first_day_last_month.replace(day=28) + timedelta(days=4)  # Get last day of the month
        today = today - timedelta(days=today.day - 1)
    else:
        from_date = today - timedelta(days=30)  # Default to last 30 days

    return from_date.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')




