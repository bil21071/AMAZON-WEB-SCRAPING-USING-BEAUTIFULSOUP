from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape1_amazon_reviews(url):
    # Send a GET request to the URL and store the response
    response1 = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    # Parse the HTML content of the page
    soup = BeautifulSoup(response1.content, 'html.parser')
    
    # Find all review sections
    reviews = soup.find_all('div', class_='a-section review aok-relative')
    
    # Initialize lists to store review data
    review_data = []
    
    # Iterate over each review
    for review in reviews:
        # Initialize a dictionary to store review details
        review_dict = {}
        
        # Find reviewer name
        reviewer_name = review.find('span', class_='a-profile-name').get_text(strip=True)
        review_dict['Reviewer Name'] = reviewer_name
        
        # Find review date
        review_date = review.find('span', class_='a-size-base a-color-secondary review-date').get_text(strip=True)
        review_dict['Date'] = review_date
        
        # Find review body
        review_body = review.find('span', class_='a-size-base review-text review-text-content').get_text(strip=True)
        review_dict['Comment'] = review_body
        
        # Find review rating
        review_rating = review.find('i', class_='a-icon-star').get_text(strip=True).split(' ')[0]
        review_dict['Rating'] = review_rating
        
        # Append review details to the list
        review_data.append(review_dict)
    
    # Create a DataFrame from the list of dictionaries
    df_reviews = pd.DataFrame(review_data)
    
    return df_reviews

# URL of the Amazon product reviews page
URL = "https://www.amazon.co.jp/-/en/Ferrero-Rocher-T-30-Chocolate-ea/product-reviews/B00600QFA8/ref=cm_cr_arp_d_viewopt_sr?filterByStar=five_star&pageNumber=1"

# Scrape reviews from the provided URL
df_reviews = scrape1_amazon_reviews(URL)

# Display the DataFrame
print(df_reviews)

# Save the DataFrame to an Excel file
df_reviews.to_excel('amazon_reviews120.xlsx', index=False)
