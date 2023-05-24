
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

procressor=None
model=None

def load_model():
    global processor,model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
    model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large").to("cuda")
    return

def object_decision(object_name:str):
    white_list=["graph"]
    if object_name in white_list:
        return True
    return False
def get_answer(frame,question:str):
    if model is None or processor is None:
        load_model()
    inputs = processor(frame, question, return_tensors="pt").to("cuda")
    out = model.generate(**inputs)
    answer=processor.decode(out[0], skip_special_tokens=True)
    print(f"{question}: {answer}")
    return str(answer)
