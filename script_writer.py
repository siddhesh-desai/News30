import os
from dotenv import load_dotenv
import google.generativeai as genai


class ScriptWriter:
    def __init__(self, news):
        self.news = news
        self.script = ""
        self.headlines = []

    def _get_response(self, prompt):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)

        return response.text

    def write_script(self):
        prompt = (f"News Article: {self.news}", f"Given the above news article, your task is to generate an engaging narration script of less than 60 words. The script should comprehensively cover the main points of the news within the 30-second time frame.",
                  f"Avoid using hashtags, external links, or any irrelevant words.")
        response = self._get_response(prompt)
        self.script = response
        return response

    def write_headlines(self):
        self.script = self.write_script()
        prompt = (f"News script: {self.script}", f"Given the script of video, your task is to generate four short headlines that comprehensively cover the main points of the news. The headlines should be impactful, concise, and engaging with an emoji. Separate the healines by a new line. Don't include any bullets.")
        response = self._get_response(prompt)
        headlines_arr = response.split("\n")
        return headlines_arr


# if __name__ == "__main__":
#     news = '''Rafael Nadal's return to the French Open - and possible farewell - ended at the first hurdle as the 14-time winner lost to Alexander Zverev.

# The 22-time Grand Slam champion was beaten 6-3 7-6 (7-5) 6-3 by the in-form German fourth seed.

# Nadal has become synonymous with Roland Garros but, in front of a partisan crowd, he could not replicate the level which has made him almost unbeatable on the Paris clay.

# The 37-year-old indicated when he missed last year's French Open that the 2024 season could be his final one on tour.

# He has also said he does not know if this will be his final time at the clay-court major - but it remains a "big chance" it will be.

# Nadal arrived on Court Philippe Chatrier - the scene of many of the finest moments of his career - to a thunderous reception from a packed stadium.

# While nowhere near his scintillating best, the former world number one showed flashes of the brilliance that has made him so loved, but not enough to stringently test Zverev.

# It was only Nadal's fourth defeat in 116 singles matches at Roland Garros and Zverev became the third man - after Robin Soderling in 2009 and Novak Djokovic in 2015 and 2021 - to beat him there.

# "I don't know if it'll be the last time I'm going to be here in front of you. If it is I have enjoyed it," Nadal said in an on-court speech.

# "The crowd have been amazing the whole week. For me it's so special to feel the love of the people the way I have felt."

# With some fans crying in the stands, Nadal departed to another standing ovation as the crowd showed their appreciation for the tournament's finest champion.

# Too early to call me 'Queen of Clay' - Swiatek after emphatic win
# Published
# 2 hours ago
# Sinner makes light work of Eubanks in Paris opener
# Published
# 6 hours ago
# No 'perfect ending' but Murray proud of French Open legacy
# Published
# 19 hours ago
# Nadal falls short after tough draw
# Anticipation for Nadal's return had been frenzied all day, with fans of the iconic champion – easily identified by Spanish red and yellow flags and 'Gracias Rafa' T-shirts – milling around the arena as soon as the gates opened.

# After a dismal defeat by Hubert Hurkacz in Rome last month, Nadal had not even been sure if he would be ready to compete here.

# In a bullish pre-tournament news conference, he said he quickly found the motivation to return and felt his practice session showed he could "play against anyone".

# Practice is very different to a match, of course. Nadal knew that and knew he faced a monumental task against Zverev.

# With the 275th-ranked Nadal unseeded at Roland Garros for the first time, having barely played because of injury in the past 18 months, it left him vulnerable to facing a leading player when the draw was made.

# Zverev is considered one of the finest players not to have won a major title and, being a strong clay-court athlete, stands a good chance of finally joining the pantheon of Grand Slam winners over the next fortnight.

# He reached the 2022 French Open semi-finals, retiring against Nadal after a nasty fall which led to a serious ankle injury, and tuned up this year by winning the Rome title earlier this month.

# The way in which the 27-year-old played against Nadal reiterated why he is among the favourites.

# Zverev's performances at Roland Garros will play out alongside a trial over domestic violence allegations. Zverev has denied the charges, with a hearing set to begin on Friday in Germany.'''
#     writer = ScriptWriter(news)
#     headlines = writer.write_headlines()
#     print(headlines)
