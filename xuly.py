import pandas as pd
import re
from underthesea import word_tokenize


input_file = "comments.csv"
output_file = "data_processed.csv"

df = pd.read_csv(input_file)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)    
    text = re.sub(r"@\w+", "", text)             
    text = re.sub(r"[^a-zA-Z0-9áàảãạâấầẩẫậăắằẳẵặéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()     
    return text

df['clean_text'] = df['comment'].apply(clean_text)


df['tokens'] = df['clean_text'].apply(word_tokenize)


positive_words = ["tốt", "tuyệt vời", "hài lòng", "đáng tiền", "thích"]
negative_words = ["tệ", "thất vọng", "không đáng", "xấu", "sai"]

def auto_label(text):
    for w in positive_words:
        if w in text:
            return 1  
    for w in negative_words:
        if w in text:
            return 0  
    return 2    

df['label'] = df['clean_text'].apply(auto_label)


df.to_csv(output_file, index=False, encoding='utf-8')
print(f"File đã xử lý xong! Lưu tại: {output_file}")
