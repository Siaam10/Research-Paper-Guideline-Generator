import requests
from bs4 import BeautifulSoup
#code produced with help of chatgpt

# replace "url" with the actual URL of the webpage you want to scrape
url = "https://theaisummer.com/vision-transformer/"

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# get the text content of the page
text = soup.get_text()

# create an HTML file and write the text content to it
with open("aisummer.html", "w", encoding="utf-8") as file:
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<title>" + url + "</title>\n</head>\n<body>\n")
    file.write("<pre>" + text + "</pre>\n")
    file.write("</body>\n</html>")
    
print("Output saved")

#https://viso.ai/deep-learning/vision-transformer-vit/
#https://theaisummer.com/vision-transformer/
#https://www.v7labs.com/blog/vision-transformer-guide
'''
https://towardsdatascience.com/what-are-vision-transformers-and-how-are-they-important-for-general-purpose-learning-edd008545e9e

https://machinelearningmastery.com/the-vision-transformer-model/

https://www.pinecone.io/learn/vision-transformers/

https://analyticsindiamag.com/hands-on-guide-to-using-vision-transformer-for-image-classification/

https://arxiv.org/abs/2202.06709

https://medium.com/analytics-vidhya/understanding-the-vision-transformer-and-counting-its-parameters-988a4ea2b8f3

https://www.educative.io/answers/what-is-vision-transformer

https://blog.paperspace.com/vision-transformers/
'''
