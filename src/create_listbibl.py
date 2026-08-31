# import os
# import lxml.etree as ET
# from acdh_tei_pyutils.tei import TeiReader
# from acdh_tei_pyutils.utils import normalize_string

# data_dir = os.path.join("data", "indices")
# input_file = os.path.join(data_dir, "listbibl.xml")
# listorg_out = os.path.join(data_dir, "listorg.xml")

# template = """
# <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
# <?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
# 	schematypens="http://purl.oclc.org/dsdl/schematron"?>
# <TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="listorg.xml">
#     <teiHeader>
#         <fileDesc>
#             <titleStmt>
#                 <title level="a">Ortsverzeichnis</title>
#                 <title level="s">Eine Karl Kraus Bibliographie, basierend auf S.P. Scheichls "Kommentierte Auswahlbibliographie" (KAB)</title>
#                 <editor ref="https://d-nb.info/gnd/1036708799">Bernhard Oberreither</editor>
#             </titleStmt>
#             <publicationStmt>
#                 <p>Publication Information</p>
#             </publicationStmt>
#             <sourceDesc>
#                 <p>Information about the source</p>
#             </sourceDesc>
#         </fileDesc>
#     </teiHeader>
#     <text>
#         <body>
#             <listOrg></listOrg>
#         </body>
#     </text>
# </TEI>
# """

# items = set()
# doc = TeiReader(input_file)
# for x in doc.any_xpath(".//tei:bibl[@xml:id]/tei:publisher"):
#     items.add(normalize_string(x.text))

# orgs = {}
# for i, x in enumerate(sorted(list(items)), start=1):
#     orgs[x] = f"kab-org-{i:0>5}"


# for x in doc.any_xpath(".//tei:bibl[@xml:id]/tei:publisher"):
#     item = normalize_string(x.text)
#     item_id = orgs[item]
#     x.attrib["key"] = f"#{item_id}"

# doc.tree_to_file(input_file)
# doc = TeiReader(template)
# listorg_node = doc.any_xpath(".//tei:listOrg")[0]

# for key, value in orgs.items():
#     node = ET.SubElement(listorg_node, "{http://www.tei-c.org/ns/1.0}org")
#     node.attrib["{http://www.w3.org/XML/1998/namespace}id"] = value
#     orgname = ET.SubElement(node, "{http://www.tei-c.org/ns/1.0}orgName")
#     orgname.text = key

# doc.tree_to_file(listorg_out)
