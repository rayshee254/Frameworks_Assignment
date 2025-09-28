import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
use_cols = ['title', 'abstract', 'publish_time', 'authors', 'journal', 'source_x']
df = pd.read_csv('metadata.csv', usecols=use_cols, low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df.dropna(subset=['publish_time', 'title'], inplace=True)
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata interactively")

# Year range filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered_df = df[df['year'].between(year_range[0], year_range[1])]

# Sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'publish_time']].head(10))

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title('Publications by Year')
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_title('Top Journals')
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
titles = filtered_df['title'].dropna().str.lower().str.cat(sep=' ')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)