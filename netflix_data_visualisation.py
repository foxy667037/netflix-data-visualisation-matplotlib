# Project Goal (Netflix Data Visualisation)
# 1. What type of content netflix has.
# 2. Which produce more content.
# 3. Understand content rating categories (PG, R, TV-MA, TV14, etc)
# 4. Duration of movies.


# ====================================================================================================================================


# Step 1: import all required libraries
import pandas as pd
import matplotlib.pyplot as plt


# Step 2: csv file path
data_file_path = "./netflix_titles.csv"


# Step 3: load data
data_frame = pd.read_csv(data_file_path)


# Step 4: clean data (remove missing values or duplicate rows)
data_frame = data_frame.dropna(
    subset=[
        "type",
        "title",
        "director",
        "cast",
        "country",
        "date_added",
        "release_year",
        "rating",
        "duration",
        "listed_in",
        "description",
    ]
)
data_frame = data_frame.drop_duplicates(subset=["show_id"])


# Step 5: Create a bar chart that define types of shows
type_counts = data_frame["type"].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color=["skyblue", "orange"])
plt.title("Number of Movies vs Tv Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig(
    "./result_images/Movies_Vs_TV_Shows_Bar_Chart.png", dpi=300, bbox_inches="tight"
)

plt.tight_layout()
plt.show()


# Step 6: Create a pie chart that show rating
rating_counts = data_frame["rating"].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Percentage Of Content Rating")
plt.savefig("./result_images/Movies_Rating_Pie_Chart.png", dpi=300, bbox_inches="tight")

plt.tight_layout()
plt.show()


# Step 7: Create a histogram that define content duration
movie_data_frame = data_frame[
    data_frame["type"] == "Movie"
].copy()  # copy data that has type == movie
movie_data_frame["duration_int"] = (
    movie_data_frame["duration"].str.replace(" min", "").astype(int)
)  # convert duration into int and remove (space min).

plt.figure(figsize=(8, 6))
plt.hist(movie_data_frame["duration_int"], bins=30, color="purple", edgecolor="black")
plt.title("Distribution of Movie Duration")
plt.xlabel("Duration in minutes")
plt.ylabel("Number Of Movies")
plt.savefig(
    "./result_images/Distribution_Of_Movies_Duration_Histogram.png",
    dpi=300,
    bbox_inches="tight",
)

plt.tight_layout()
plt.show()


# Step 8: Create a scatter plot that define release year vs number of shows
release_counts = data_frame["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.scatter(release_counts.index, release_counts.values, color="red", marker="o")
plt.title("Release Years Vs Number of Shows")
plt.xlabel("Release Years")
plt.ylabel("Number of Shows")
plt.grid(True)
plt.savefig(
    "./result_images/Release_Years_Vs_Number_Of_Shows_Scatter_Plot.png",
    dpi=300,
    bbox_inches="tight",
)

plt.tight_layout()
plt.show()


# Step 9: Create a horizantal bar chart that define top 10 country that release number of shows
country_counts = data_frame["country"].value_counts().head(10).sort_values()

plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color="skyblue")
plt.title("Top 10 Countries By Number of Shows")
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.grid(True)
plt.savefig(
    "./result_images/Top_10_Countries_By_Num_Of_Shows_Bar_Chart.png",
    dpi=300,
    bbox_inches="tight",
)

plt.tight_layout()
plt.show()


# Step 10: Create a subplot that define Movies vs TV Shows by year
content_by_year = (
    data_frame.groupby(["release_year", "type"]).size().unstack().fillna(0)
)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# first subplot: movies
ax[0].plot(content_by_year.index, content_by_year["Movie"], color="blue")
ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number Of Movies")

# second subplot: tv shows
ax[1].plot(content_by_year.index, content_by_year["TV Show"], color="orange")
ax[1].set_title("TV Shows Released Per Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number Of Movies")

fig.suptitle("Comparison Of Movies and TV Shows Released Over Year")

plt.tight_layout()
plt.savefig(
    "./result_images/Comparison_Of_Movies_and_TV_Shows_Released_Over_Year.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()