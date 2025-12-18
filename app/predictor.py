import joblib
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

class EmotionPredictor:
    def __init__(self):
        # Load mô hình phân loại đã train
        self.model = joblib.load("models/emotion_model.pkl")

        # Load PhoBERT
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
        self.phobert = AutoModel.from_pretrained("vinai/phobert-base")

        # Chạy CPU
        self.device = torch.device("cpu")
        self.phobert.to(self.device)

    def encode_text(self, text: str):
        """
        Chuyển văn bản thành embedding 768 chiều bằng PhoBERT
        """
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            max_length=128,
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():
            outputs = self.phobert(**inputs)

        # Lấy cls embedding (pooler_output)
        # Nếu pooler_output không có -> dùng mean pooling
        if hasattr(outputs, "pooler_output"):
            vector = outputs.pooler_output
        else:
            vector = outputs.last_hidden_state.mean(dim=1)

        return vector.cpu().numpy()

    def predict(self, text: str):
        """
        Dự đoán cảm xúc từ văn bản
        """
        # Vector hóa bằng PhoBERT
        vec = self.encode_text(text)

        # Mô hình .pkl dự đoán
        proba = self.model.predict_proba(vec)[0]  # xác suất mỗi lớp

        # Cảm xúc dự đoán
        emotion = self.model.classes_[np.argmax(proba)]

        # Độ tin cậy
        confidence = float(np.max(proba))

        return emotion, confidence
