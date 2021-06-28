import xml.etree.ElementTree as ET
import pandas as pd

# file_path = "./xmls/221-01"
tree = ET.parse("./xmls/309-01.xml")
root = tree.getroot()

plain_text = root.find('TEXT').text

id = []
start = []
end = []
text = []
TYPE = []
entity = []
start_map = {}
for elem in tree.iter():
    # print(elem.tag)
    if (not elem.tag == 'TEXT') and (not elem.tag == 'TAGS') and (not elem.tag == 'deIdi2b2'):
        # print(elem.tag)
        for alt_tag in elem.findall():
            entity.append(alt_tag)
            id.append(alt_tag.attrib['id'])
            start.append(alt_tag.attrib['start'])
            end.append(alt_tag.attrib['end'])
            text.append(alt_tag.attrib['text'])
            TYPE.append(alt_tag.attrib['TYPE'])
print(entity)
# for tag in root.findall('TAGS'):
#     for alt_tag in tag:
#         id.append(alt_tag.attrib['id'])
#         start.append(alt_tag.attrib['start'])
#         end.append(alt_tag.attrib['end'])
#         text.append(alt_tag.attrib['text'])
#         TYPE.append(alt_tag.attrib['TYPE'])
#
#         # map out all words with tags and keep their types, the word itself, and the starting and ending.
#         start_map[int(alt_tag.attrib['start'])] = {
#             "tag": tag,
#             "type": alt_tag.attrib['TYPE'],
#             "text": alt_tag.attrib['text'],
#             "end": int(alt_tag.attrib['end']),
#         }
# ner_map = {}
# conll_formatted = ""
# tagged_tokens = {}
# buffer = ""
# bio_tagged = []
# prev_tag = "O"
#
# cursor = 0
# while True:
#     # break out of loop if you come to end of the text file.
#     if cursor >= len(plain_text):
#         break
#     # Check every character if its in the label list.
#     # (if this character starts a mentioned label)
#     if cursor in start_map:
#         temp_text = plain_text[cursor: start_map[cursor]["end"]]
#         # print("****************************************")
#         if temp_text == start_map[cursor]["text"]:
#             # tagged_tokens[temp_text] += start_map
#             conll_formatted += f"{temp_text}\t{start_map[cursor]['tag']}\n"
#             # conll_formatted.append((temp_text, start_map[cursor]['type']))
#             cursor = start_map[cursor]["end"]
#     elif plain_text[cursor] == " " or plain_text[cursor] == "\n" or plain_text[cursor] == "\t":
#         if buffer:
#             # tagged_tokens[buffer] += "O"
#             conll_formatted += f"{buffer}\tO\n"
#             # conll_formatted.append((buffer, 'O'))
#             buffer = ""
#     else:
#         buffer += plain_text[cursor]
#
#     cursor += 1
#
# # print(conll_formatted)
#
# with open("conll/majeedTest-01.conll", 'w') as file:
#     file.write(conll_formatted)
#
# for token, tag in conll_formatted:
#     if tag == "O":  # O
#         bio_tagged.append((token, tag))
#         prev_tag = tag
#         continue
#     if tag != "O" and prev_tag == "O":  # Begin NE
#         bio_tagged.append((token, "B-" + tag))
#         prev_tag = tag
#     elif prev_tag != "O" and prev_tag == tag:  # Inside NE
#         bio_tagged.append((token, "I-" + tag))
#         prev_tag = tag
#     elif prev_tag != "O" and prev_tag != tag:  # Adjacent NE
#         bio_tagged.append((token, "B-" + tag))
#         prev_tag = tag
#
# print(bio_tagged)