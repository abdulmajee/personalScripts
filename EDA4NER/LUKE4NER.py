from transformers import LukeTokenizer, LukeModel, LukeForEntityPairClassification
import xml.etree.ElementTree as ET

model = LukeModel.from_pretrained("studio-ousia/luke-base")
tokenizer = LukeTokenizer.from_pretrained("studio-ousia/luke-base")


tree = ET.parse("./xmls/221-01.xml")
root = tree.getroot()

text = root.find('TEXT').text

# Extract all character-based entity span corresponding to plain_text (start and end of entities)
entity_spans = []
for tag in root.findall('TAGS'):
    for alt_tag in tag:
        entity_spans.append((alt_tag.attrib['start'], alt_tag.attrib['end']))
inputs = tokenizer(text, entities=entities, entity_spans=entity_spans, add_prefix_space=True, return_tensors="pt")
outputs = model(**inputs)
word_last_hidden_state = outputs.last_hidden_state
entity_last_hidden_state = outputs.entity_last_hidden_state
