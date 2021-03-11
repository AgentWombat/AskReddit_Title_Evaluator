import reddit_scraper
import sys
import json


if len(sys.argv) == 1:

    subreddit_name = input('What is the name of the subreddit?\n')

    section = input('Which section of the subreddit? (e.g. "new", "hot", "top")\n')

    output_path = input('What is the file location where the data will be output? (e.g. directory/directory/file_name.extention)\n')

    pages = int(input('How many pages should be scraped?\n'))

elif len(sys.argv) == 5:
    	
    subreddit_name= sys.argv[1]

    section = sys.argv[2]

    output_path = sys.argv[3]
    
    pages = int(sys.argv[4])
else:
	raise ValueError("Invalid arguments; should take form 'py data_collector.py subreddit_name section output_path pages'")

posts = reddit_scraper.get_posts(subreddit_name, section, start_page_number=0, pages = pages)

with open(output_path, 'w') as file:
    json.dump(posts, file)

print('Done')



