# News30 - AI-Powered 30-Second News Video Generator

## 🚀 Overview
**News30** is an AI-driven tool that automates the creation of concise 30-second news videos. It scrapes the latest news, generates engaging scripts, and converts them into short, visually appealing videos—ideal for quick news consumption.

## 🎯 Features
- **Automated News Scraping**: Fetches the latest news from reliable sources.
- **AI-Powered Script Generation**: Creates concise and engaging news summaries.
- **Dynamic Video Creation**: Generates high-quality short videos with visuals and narration.
- **Fast & Efficient**: Produces news videos in seconds.

## 🛠 Installation
Ensure you have **Python 3.8+** installed. Then, follow these steps:

```sh
  # Clone the repository
  git clone https://github.com/siddhesh-desai/News30.git
  cd News30

  #Update the .env file
  
  # Install dependencies
  pip install -r requirements.txt
```

## ▶️ How to Run
Run the main application using:

```sh
  python app.py
```

This will initiate the news scraping, script generation, and video creation pipeline. The generated news videos will be available in the **output_videos.txt** file.

## 📁 Project Structure
- **news_scraper.py** - Scrapes news from sources.
- **script_writer.py** - Generates a script from the scraped news.
- **news_byte_creator.py** - Processes and structures the news.
- **video_maker.py** - Creates the final video from the script and assets.
- **templates/** - Contains web templates for the interface.

## 🏆 Contributing
We welcome contributions! Feel free to submit issues, feature requests, or pull requests.

## 📜 License
This project is licensed under the **MIT License**.

---
🎥 *Stay informed in just 30 seconds with News30!*

