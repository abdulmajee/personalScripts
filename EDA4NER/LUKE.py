
from transformers import LukeTokenizer, LukeForEntityPairClassification
model = LukeForEntityPairClassification.from_pretrained("studio-ousia/luke-large-finetuned-tacred")
tokenizer = LukeTokenizer.from_pretrained("studio-ousia/luke-large-finetuned-tacred")
# text = "Beyoncé lives in Los Angeles."
text = "Majeed is a from Ghana but works at Sentez Güvenlik."
entity_spans = [(0, 6), (36, 50)]  # character-based entity spans corresponding to "Beyoncé" and "Los Angeles"
inputs = tokenizer(text, entity_spans=entity_spans, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
predicted_class_idx = int(logits[0].argmax())
print("Predicted class:", model.config.id2label[predicted_class_idx])

