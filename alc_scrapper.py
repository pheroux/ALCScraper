from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Function to scrape the winning numbers
def scrape_winning_numbers(url, webdriver_path):
    # Set up Selenium with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

    # Fetch the webpage
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    winning_numbers = []

    # Find the winning numbers container
    container = soup.find('ol', class_='draw__full__mainDraw__winning-number-container__winning-numbers winning-numbers')

    if not container:
        print("Winning numbers container not found. Inspect the webpage's HTML structure.")  # Debugging statement
    else:
        print("Winning numbers container content:", container.prettify())  # Debugging statement

        # Find all the winning number elements within the container using a less restrictive class name
        numbers = container.find_all('li', class_='draw--full__winning-number')

        if not numbers:
            print("No winning number elements found. Inspect the webpage's HTML structure.")  # Debugging statement
        else:
            print(f"Found {len(numbers)} winning number elements.")  # Debugging statement

        for number in numbers:
            winning_numbers.append(number.text)

    driver.quit()
    return winning_numbers

# Main function
def main():
    url = "https://www.alc.ca/content/alc/en/our-games/lotto/lotto-6-49.html?date=2023-03-04"
    # Replace with the path to your Chrome WebDriver executable 
    webdriver_path = "C:/chromedriver/chromedriver.exe"
    winning_numbers = scrape_winning_numbers(url, webdriver_path)

    if winning_numbers:
        print("Winning numbers:", ', '.join(winning_numbers))
    else:
        print("No winning numbers found.")

if __name__ == "__main__":
    main()
