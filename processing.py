
#!/usr/bin/env python3
import xml.etree.ElementTree as ET
tree = ET.parse('./static/FIX42.xml')
root = tree.getroot()
#for child in root:
 # print(child.tag)
  #for subchild in child:
   # print(subchild.tag, subchild.attrib)
field_dict={}
for x in root.findall(".//fields/"):
   ## Prints message time
  # print(x.attrib)
   field_dict[x.attrib['number']] = x.attrib
sample = "8=FIX.4.2|9=51|35=0|34=703|49=ABC|52=20100130-10:53:40.830|56=XYZ|10=249"

def parse_fix(message):

  fix_dict= {}
  split_message = message.split("|")

  for pair in split_message:
     pair_list= pair.split("=")
     fix_dict[pair_list[0]]=pair_list[1]

  #print(fix_dict)
  display_dict={}
  for key, value in fix_dict.items():
    display_dict[key] = field_dict[key]
    display_dict[key]['value']=value
  return  display_dict


#print(parse_fix("8=FIX.4.2|9=51|35=0|34=703|49=ABC|52=20100130-10:53:40.830|56=XYZ|10=249"))


