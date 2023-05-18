from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

procressor=None
model=None

def load_model():
    global processor,model
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224').to("cuda")
    return

def object_detection(frame):
    if model is None or processor is None:
        load_model()
    inputs = processor(images=frame, return_tensors="pt").to("cuda")
    outputs = model(**inputs)
    logits = outputs.logits

    predicted_class_idx = logits.argmax(-1).item()
    class_name=model.config.id2label[predicted_class_idx]

    return (class_name,logits.max().item())