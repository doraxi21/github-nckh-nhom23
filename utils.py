emotion_words = {
    "vui": ["vui", "hạnh phúc", "phấn khởi", "vui vẻ"],
    "buồn": ["buồn","buồn bã","chán", "chán nản", "thất vọng"],
    "tức giận": ["tức", "giận", "cau có", "nổi điên"],
    "sợ hãi": ["sợ", "hoảng", "hoảng loạn"],
    "ghê tởm": ["ghê", "kinh", "ghê tởm"],
    "ngạc nhiên": ["ngạc nhiên", "bất ngờ"],
    "tin tưởng": ["tin tưởng", "yên tâm"],
    "kỳ vọng": ["mong đợi", "hi vọng", "kỳ vọng"]
}
negators = ["nhưng","nhưng mà","tuy nhiên", "mặc dù", "dù vậy"]
time_words = {
    "quá_khứ": ["hôm qua", "lúc trước", "khi đó"],
    "hiện_tại": ["giờ","bây giờ", "hiện tại", "giờ thì"]
}


def detect_emotion_rule(sentence: str):
    s= sentence.lower()
    pos=0
    for neg in negators:
        if neg in s:
          pos=s.find(neg)
          s= s[pos+len(neg):]
          break
    s=s.strip()
    best_emotion= None
    best_length= 0
    for emotion, word_list in emotion_words.items():    
        for w in word_list:
            if(w in s):
                if(len(w)>best_length):
                 best_length=len(w)
                 best_emotion=emotion    
                   
        
    if best_emotion is None:
      return "Không xác định"        
    else: 
       return best_emotion
