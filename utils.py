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
negators = ["nhưng","nhưng mà","tuy nhiên", "mặc dù", "dù vậy","bởi vì"]
time_words = {
    "quá_khứ": ["hôm qua", "lúc trước", "khi đó"],
    "hiện_tại": ["giờ","bây giờ", "hiện tại", "giờ thì","hiện giờ"]
}


def detect_emotion_rule(sentence: str):
    s= sentence.lower().strip()
    pos=0 
    for word_present in time_words["hiện_tại"]:
       if(word_present in s):
          pos=s.find(word_present)
          s=s[pos+len(word_present):]
          break
          
    before, after=s,""   # -> before = s, after =""
    #tách 2 nửa nếu có từ nối
    for neg in negators:
       if neg in s:
          idx= s.find(neg)
          before = s[:idx]
          after = s[idx+len(neg):]
          break
    # kiểm tra 2 nửa -> có từ quá khứ không
    for past_word in time_words["quá_khứ"]:
       if past_word in after:
          return detect_emotion_rule(before)
       if past_word in before:
          return detect_emotion_rule(after)
    # sau khi kiểm tra qk -> kiểm tra 2 nửa có từ hiện tại không
    for present_word in time_words["hiện_tại"]:
       if present_word in before:
          return detect_emotion_rule(before)
       if present_word in after:
          return detect_emotion_rule(after)
    # tìm từ cảm xúc gần đúng nhất
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