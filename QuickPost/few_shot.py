import pandas as pd
import json
import os


class FewShotPosts:
    def __init__(self, file_path=None):
        self.df = None
        self.unique_tags = None
        if file_path is None:
            
            file_path = os.path.join(os.path.dirname(__file__), "data", "processed_posts.json")
        self.load_posts(file_path)

    def load_posts(self, file_path):
        try:
            with open(file_path, encoding="utf-8") as f:
                posts = json.load(f)
                self.df = pd.json_normalize(posts)
                self.df['length'] = self.df['line_count'].apply(self.categorize_length)
               
                all_tags = self.df['tags'].apply(lambda x: x).sum()
                self.unique_tags = list(set(all_tags))
        except FileNotFoundError:
            
            raw_file_path = os.path.join(os.path.dirname(__file__), "data", "raw_posts.json")
            from preprocessor import process_raw_posts
            posts = process_raw_posts(raw_file_path)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length) 
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  
            (self.df['language'] == language) & 
            (self.df['length'] == length)  
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    
    posts = fs.get_filtered_posts("Medium", "English", "Job Search")
    print(posts)
