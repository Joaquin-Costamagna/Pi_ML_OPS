import pandas as pd


df_steam_games = pd.read_parquet('Data/steam_games.parquet')

df_user_reviews = pd.read_parquet('Data/user_reviews.parquet')

df_user_items= pd.read_parquet('Data/user_items.parquet')

df_user_items = pd.DataFrame(df_user_items)

df_steam_games = pd.DataFrame(df_steam_games)

df_user_reviews = pd.DataFrame(df_user_reviews)


df_reviews_games2 = df_user_reviews.merge(df_steam_games[['item_id', 'price']])


df_games_reviews4 = pd.merge(df_steam_games, df_user_reviews, how="inner", left_on="item_id", right_on="item_id")
df_games_reviews4 = df_games_reviews4.drop(['price', 'item_id', 'release_year', 'user_id', 'item_id', 'sentiment_analysis'], axis=1)


df_games_reviews5 = pd.merge(df_steam_games, df_user_reviews, how="inner", left_on="item_id", right_on="item_id")


def developer(developer):
    df_developer = df_steam_games[df_steam_games["developer"] == developer]
    items_per_year = df_developer.groupby("release_year")["item_id"].count()

    # Filter the developer's DataFrame for free games (price zero):
    df_dev_free = df_developer[df_developer["price"] == 0]

    # Get the number of free items per year
    free_items = df_dev_free.groupby("release_year")["price"].count()  # Number of free items per year

    # Calculate the percentage of free content per year
    free_proportion = round((free_items / items_per_year) * 100, 2)

    # Rename the series to merge them into a DataFrame:
    items_per_year.name = "Number of Items"
    free_proportion.name = "Free Content"

    df1 = pd.merge(items_per_year, free_proportion, on="release_year").reset_index()
    df1 = df1.fillna(0)

    df1 = df1.rename(columns={"release_year": "Year"})

    # Format the Free Content column:
    df1["Free Content"] = df1["Free Content"].apply(lambda x: f"{x}%")

    # Convert the DataFrame to a dictionary
    dictionary = df1.to_dict(orient="records")
    del df_developer, items_per_year, df_dev_free, free_items, free_proportion, df1
    return dictionary




def userdata(user_id):
    # Filter the data for the specified user
    user_data = df_reviews_games2[df_reviews_games2['user_id'] == user_id]

    # Calculate the amount of money spent by the user
    spent_money = user_data['price'].sum()

    # Calculate the recommendation percentage based on reviews.recommend
    recommendations = (user_data['recommend'] == True).sum()
    recommendation_percentage = recommendations / len(user_data) * 100

    # Calculate the number of items
    number_of_items = user_data['item_id'].nunique()

    # Create a dictionary with the results
    results = {
        'Amount of money spent': round(spent_money, 2),
        'Recommendation Percentage': recommendation_percentage,
        'Number of items': number_of_items
    }
    return results


'''
def UserForGenre(genre):
    
    # Filter games by the specified genre
    games_filtered = df_steam_games[df_steam_games['genres'].str.contains(genre, case=False, na=False)]

    # Merge df_user_items and df_games based on item_id and id
    merged_df = pd.merge(df_user_items, games_filtered, left_on='item_id', right_on='item_id', how='inner')

    # Group by year and user, calculate the playtime by user per year
    grouped = merged_df.groupby(['release_year', 'user_id'])['playtime_forever'].sum().reset_index()

    if len(grouped) > 0:
        # Find the user with the most playtime for the given genre
        max_user = grouped[grouped['playtime_forever'] == grouped.groupby('release_year')['playtime_forever'].transform('max')]['user_id'].values[0]
    else:
        return {"error": "No data available for the specified genre"}

    # Filter the data for the user with the most playtime
    user_data = grouped[grouped['user_id'] == max_user]

    # Remove years with 0 playtime
    user_data = user_data[user_data['playtime_forever'] > 0]

    # Sort years in descending order
    user_data = user_data.sort_values(by='release_year', ascending=False)

    # Convert playtime to integers
    user_data['playtime_forever'] = user_data['playtime_forever'].astype(int)

    # Create a list of accumulated playtime by year
    hours_by_year = [{'Year': int(year), 'Hours': int(hours)} for year, hours in zip(user_data['release_year'], user_data['playtime_forever'])]

    result = {
        "User with the Most Playtime for Genre " + genre: max_user,
        "Playtime": hours_by_year
    }

    return result

'''


def best_developer_year(year):
    df = df_games_reviews4
    
    # Convert columns to the appropriate data types
    df["recommend"] = df["recommend"].astype(int)
    df["year"] = df["year"].astype(int)
    
    # Perform groupby and apply an aggregation function
    df = df.groupby(['developer', 'year'])['recommend'].sum().reset_index()

    # Rename the resulting column
    df = df.rename(columns={'recommend': 'total_true'})
    
    # Filter the data for the specified year
    filtered_df = df[df['year'] == year]
    if filtered_df.empty:
        return "No data found for that year"

    # Group by developer and sum recommended games
    developer_grouped = filtered_df.groupby('developer')['total_true'].sum().reset_index()

    # Sort in descending order
    developer_grouped = developer_grouped.sort_values(by='total_true', ascending=False)

    # Add the position rank
    developer_grouped['Position'] = range(1, len(developer_grouped) + 1)

    # Select the top 3 developers
    top_developers = developer_grouped.head(3)

    # Create the result in the desired format
    result = [{"Position {}: {}".format(row['Position'], row['developer']): row['total_true']} for i, row in top_developers.iterrows()]

    return result




def developer_reviews_analysis(developer):
    df = df_games_reviews5
    df = df.drop(['item_id', 'release_year', 'price'], axis= 1)
    # Filtramos las reseñas del desarrollador especificado
    df = df[df["developer"] == developer]

    # Contamos el número de reseñas positivas y negativas
    count_positive = df[df["sentiment_analysis"] == 2].shape[0]
    count_negative = df[df["sentiment_analysis"] == 0].shape[0]

    # Devolvemos el resultado
    return {
        "developer": developer,
        "negative": count_negative,
        "positive": count_positive,
    }
























