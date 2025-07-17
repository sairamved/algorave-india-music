import pandas as pd
from templates import track_template, index_template, index_block

df = pd.read_csv("data.csv")
df.columns = ["track", "track_artist", "zine_artist", "zine_link", "process",
                     "track_artist_link", "zine_artist_link", "track_artist_bio", "zine_artist_bio",
                     "track_artist_photo", "zine_artist_photo", "number", "slug"]
track_info = df[:10]

blocks = []

for i in range(10):
	# Write track page
    with open(f"../{track_info.loc[i].slug}.html", "w") as f:
        row = track_info.loc[i]
        f.write(track_template(
            row.slug,
            row.track,
            row.number,
            row.track_artist,
            row.zine_artist, 
            row.process,
            row.zine_link))
    # Append track info to index blocks
    blocks.append(index_block(row.slug, row.track))

# Write index page
with open(f"../index.html", "w") as f:
    f.write(index_template("\n".join(blocks)))