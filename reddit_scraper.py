from bs4 import BeautifulSoup as bs
import requests
import time


def get_posts(subreddit: str, section: str, start_page_number = 0, pages = 1, time_frame = 'all', store_link = False):
    '''
    Returns an array in which each entry is a dictionary containing information about a post on the spesified reddit page. It grabs every post on each page and skips advertisements.
    :param subreddit: The subreddit to be scrapped.
    :param section: 'top', 'new', 'hot'. The section of the subreddit.
    :param start_page_number: 0 is the first page. The starting page index of the posts.
    :param pages: The number of pages scraped.
    :param time_frame: 'hour', 'day', 'week', 'month', 'year', 'all'. Only does anything when sectoon is set to 'top'. Sets the time over which top posts will be scraped.
    :return: The posts array. Each post is represented by a dictionary with 'title', 'link', 'karma', and 'comment_count' keys.
    '''

    # To access page n, the get request must contain the id of the last post on page n-1.
    # 'last_id' is neccisary because it stores the id of the last post on a page.
    # This is then used to access the page successive to the current page.


    # Circumvent reddit bot detection by adding headers to get request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

    posts = []

    last_id = ''
    for page in range(0, start_page_number + pages):

        MAX_ATTEMPTS = 10
        i = 0

        # get response from reddit
        response = ''
        while True:
            if page == 0:
                response = requests.get('https://old.reddit.com/r/'+subreddit+'/'+section+'/?t='+time_frame, headers = headers)
            else:
                response = requests.get('https://old.reddit.com/r/'+subreddit+'/'+section+'/?t='+time_frame+'&after='+last_id, headers = headers)


            if response:
                break
            else:
                i += 1
                if i > MAX_ATTEMPTS:
                    raise ValueError("Failed to connect after " + MAX_ATTEMPTS + " attempts")

                time.sleep(2)

        soup = bs(response.text, 'html.parser')

        # If not yet at the first page to scrape, move on to the next page
        if page < start_page_number:
            last_id = soup.find_all('div', class_='thing')[-1].attrs['id'][6:]

        # Add to posts
        else:
            for div in soup.find_all('div', class_='thing'):
                post = {}
                
                # Skip advertisements
                if 'promoted' in div.attrs['class']:
                    continue
                
                post['title'] = div.find(class_='title').a.text
                
                if store_link:
                    post['link'] = div.attrs['data-url']

                post['karma'] = div.attrs['data-score']

                post['comment_count'] = div.attrs['data-comments-count']

                posts.append(post)

                # Save the id of the last post on the page
                last_id = div.attrs['id'][6:]

    return posts
