def plot_mood(mood_label_1, mood_label_2, number_of_days):
    sns.set()
    fig, ax = plt.subplots(figsize=(16,10))
    
    #filter dataframe to select required timespan
    filtered_by_date = df_sorted[df_sorted.index >= (df_sorted.index[0] - pd.Timedelta(days=number_of_days-1))]
    
    #set x and y axess
    x = filtered_by_date.index
    y = filtered_by_date[mood_label_1]
    y1 = filtered_by_date[mood_label_2]
    
    #format title
    title = f"{mood_label_1} and {str.lower(mood_label_2)} in the last {number_of_days} days"
    
    #set title and labels
    ax.set_title(title, fontsize=16)
    ax.set_ylabel('Levels') 
    ax.set_xlabel('Date')

    #format date labels
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()
    ax.tick_params(axis='x', rotation=45)

    ax.plot(x, y, marker='.', label=mood_label_1)
    ax.plot(x, y1, marker='x', label=mood_label_2)

    #set legend
    plt.legend()

    plt.show()
