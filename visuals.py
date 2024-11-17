from datetime import datetime, timedelta
from matplotlib.ticker import MaxNLocator
from matplotlib.figure import Figure
import seaborn as sns

def generate_bar_chart(result, title="Office Issue Statistics"):
    columns = list(result.keys())
    critical_counts = [result[col][0] for col in columns]
    moderate_counts = [result[col][1] for col in columns]

    total_counts = [crit + mod for crit, mod in zip(critical_counts, moderate_counts)]

    sns.set(style="whitegrid")

    fig = Figure(figsize=(14, 8))  
    ax = fig.subplots()
    
    width = 0.5  
    bar_positions = range(len(columns))
  
    ax.bar(bar_positions, critical_counts, label="Critical", 
           color=sns.color_palette("Reds", 5)[3], width=width, edgecolor="black")
    ax.bar(bar_positions, moderate_counts, label="Moderate", 
           bottom=critical_counts, color=sns.color_palette("Blues", 5)[3], width=width, edgecolor="black")

    ax.set_ylabel('Number of Cases', fontsize=14, fontweight='bold')
    ax.set_title(title, fontsize=18, fontweight='bold', color="darkblue")
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(columns, rotation=45, ha="right", fontsize=12, color="darkblue")

    max_y = max(total_counts)
    ax.set_ylim(0, max_y + (0.2 * max_y))  

    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    for i, (crit, mod) in enumerate(zip(critical_counts, moderate_counts)):
        ax.text(i, crit / 2, f'{crit}', ha='center', va='center', color='white', fontweight='bold', fontsize=10)
        if mod > 0:
            ax.text(i, crit + (mod / 2), f'{mod}', ha='center', va='center', color='white', fontweight='bold', fontsize=10)

    ax.legend(loc="upper right", fontsize=12, title="Severity Level", title_fontsize=13, edgecolor="black")
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
        today = first_day_last_month.replace(day=28) + timedelta(days=4)  
        today = today - timedelta(days=today.day - 1)
    else:
        from_date = today - timedelta(days=30) 

    return from_date.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')