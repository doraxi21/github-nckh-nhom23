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
negation_words = ["không", "chẳng", "chưa"]  # từ phủ định
time_words = {
    "quá_khứ": ["hôm qua", "lúc trước", "khi đó"],
    "hiện_tại": ["giờ","bây giờ", "hiện tại", "giờ thì","hiện giờ"]
}

# Mapping đảo cảm xúc khi gặp phủ định
inverse_emotion = {
    "vui": "buồn",
    "buồn": "vui",
    "tức giận": "không tức giận",
    "sợ hãi": "can đảm",
    "ghê tởm": "thích",
    "ngạc nhiên": "bình thường",
    "tin tưởng": "hoài nghi",
    "kỳ vọng": "thất vọng"
}
def detect_emotion_advanced(sentence: str):
    s = sentence.lower().strip()
    
    # Chia câu theo các từ nối
    parts = [s]
    for neg in negators:
        new_parts = []
        for part in parts:
            new_parts.extend(part.split(neg))
        parts = new_parts

    emotions_found = []
    
    # Lọc phần hiện tại, bỏ quá khứ
    current_parts = []
    for part in parts:
        if any(tp in part for tp in time_words["quá_khứ"]):
            continue
        if any(tp in part for tp in time_words["hiện_tại"]):
            current_parts.append(part)
    if not current_parts:
        current_parts = [s]
    
    # Phân tích từng phần
    for part in current_parts:
        words = part.split()
        best_emotion = None
        best_length = 0
        negated = False
        
        for emotion, word_list in emotion_words.items():
            for w in word_list:
                if w in part and len(w) > best_length:
                    best_length = len(w)
                    best_emotion = emotion
                    # Kiểm tra phủ định theo khoảng cách từ
                    for i, token in enumerate(words):
                        if token in negation_words:
                            try:
                                emo_index = words.index(w)
                                if 0 <= emo_index - i <= 2:  # phủ định trong vòng 2 từ
                                    negated = True
                                    break
                            except ValueError:
                                pass
        
        if best_emotion:
            if negated and best_emotion in inverse_emotion:
                best_emotion = inverse_emotion[best_emotion]
            emotions_found.append(best_emotion)
    
    # Trả về cảm xúc chính
    if emotions_found:
        return emotions_found[-1]  # ưu tiên cảm xúc cuối cùng
    return "Không xác định"