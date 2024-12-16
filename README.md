# Scratch Username Scraper 🧑‍💻

A Python script that scrapes usernames of Scratch users starting from a given seed username. It gathers usernames from followers and saves them to a file. This tool is perfect for gathering a list of Scratch users for research, analysis, or other purposes. 

## Features ✨
- Interactive menu to start the scraper or exit 🚪
- Displays ASCII art with animation 🎨
- Progress bar to track scraping status 📊
- Saves scraped usernames to `scratch_usernames.txt` 📝
- Fully customizable with a starting username and a maximum number of usernames to scrape 🎯

## Requirements 📋
To run this script, you need the following Python libraries:
- `requests` — to make HTTP requests
- `time` — to manage delays between requests
- `os` and `shutil` — for file and terminal management
- `colorama` — for colorful console output

You can install the required libraries by running the following command:
```bash
pip install requests colorama
```

## How to Use 🚀
1. Clone or download the repository.
2. Run the script with Python:
   ```bash
   python main.py
   ```
3. You will be prompted to enter a starting username and a maximum number of usernames to scrape.
4. The script will fetch the usernames and save them in `scratch_usernames.txt`.

### Interactive Menu 🎮
- **[1] Start Scraper**: Begin scraping Scratch usernames.
- **[2] Exit**: Close the script.

### Output 📂
- Scraped usernames will be saved in `scratch_usernames.txt`.

## Example Usage 👇

```bash
$ python main.py
Enter the starting username: scratchteam
Enter the maximum number of usernames to scrape: 500
Scraping complete! 500 usernames saved in 'scratch_usernames.txt'.
```

## ASCII Art 🎨
The script displays a fun ASCII art animation when it starts:

```
                                                                   
 _____                               _____                         
|  |  |___ ___ ___ ___ ___ _____ ___|   __|___ ___ ___ ___ ___ ___ 
|  |  |_ -| -_|  _|   | .'|     | -_|__   |  _|  _| .'| . | -_|  _|
|_____|___|___|_| |_|_|__,|_|_|_|___|_____|___|_| |__,|  _|___|_|  
                                                      |_|

```

---

## Credits 🙌

This tool was created by **Kyra** 🦸‍♂️.  
If you have any questions or suggestions, feel free to reach out! 😄

---

## License 📝

This tool is open-source under the MIT License. You can freely modify and distribute it as per your needs.
