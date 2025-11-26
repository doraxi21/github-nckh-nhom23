emotion_words = {
    "vui": ["vui", "hạnh phúc", "phấn khởi", "vui vẻ"],
    "buồn": ["buồn", "chán", "chán nản", "thất vọng"],
    "tức giận": ["tức", "giận", "cau có", "nổi điên"],
    "sợ hãi": ["sợ", "hoảng", "hoảng loạn"],
    "ghê tởm": ["ghê", "kinh", "ghê tởm"],
    "ngạc nhiên": ["ngạc nhiên", "bất ngờ"],
    "tin tưởng": ["tin tưởng", "yên tâm"],
    "kỳ vọng": ["mong đợi", "hi vọng", "kỳ vọng"]
}
negators = ["nhưng", "tuy nhiên", "mặc dù", "dù vậy"]
time_words = {
    "quá_khứ": ["hôm qua", "lúc trước", "khi đó"],
    "hiện_tại": ["bây giờ", "hiện tại", "giờ thì"]
}


def detect_emotion_rule(sentence: str):
    s= sentence.lower()
    
    for neg in negators:
        s= s[s.find(neg)+len(neg):]
        break
    
    for emotion, word_list in emotion_words.items():    
        for w in word_list:
            if(w in s):                
                return emotion
                break 
    
    return "Không xác định"        