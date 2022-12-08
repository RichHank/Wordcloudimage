import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import string

# Set the URL of the website you want to skim
url = "https://www.infowars.com/"

# Open a connection to the website and store the response
with requests.get(url) as response:
    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Compile a regular expression to match words
    word_regex = re.compile(r"\b[a-zA-Z]+\b")

    # Create a set of common words to exclude
    common_words = set(["and", "the", "from"])

    # Create a translation table to exclude punctuation characters
    translation_table = str.maketrans("", "", string.punctuation)

    # Create a Counter to count the words
    word_counts = Counter()

    # Find all the heading and paragraph tags
    tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"])

    # Process the words in each tag
    for tag in tags:
        # Find all the words in the tag
        words = word_regex.findall(tag.text)
        # Convert the words to lowercase and remove punctuation characters
        words = [word.lower().translate(translation_table) for word in words]
        # Increment the count of each word in the Counter
        word_counts.update(word for word in words if word not in common_words and len(word) >= 3)

    # Get the 100 most common words
    most_common_words = word_counts.most_common(100)

    # Format the output as a string in "a, b, c" format
    output_string = ", ".join([word for word, count in most_common_words])
    print(output_string)
