import os

import lxml.etree as ET
from acdh_tei_pyutils.tei import TeiReader
from acdh_tei_pyutils.utils import any_xpath
from acdh_wikidata_pyutils import WikiDataPlace
from tqdm import tqdm

listplace = os.path.join("data", "indices", "listplace.xml")

doc = TeiReader(listplace)

for x in tqdm(
    doc.any_xpath(
        ".//tei:body//tei:listPlace/tei:place[./tei:idno[@type='Wikidata'] and not(.//tei:geo)]"
    )[:4]
):
    try:
        coords = any_xpath(x, "./tei:location/tei:geo")[0]
    except IndexError:
        wiki_id = any_xpath(x, "./tei:idno[@type='Wikidata']")[0].text
        label = any_xpath(x, "./tei:placeName")[0].text
        item = WikiDataPlace(f"https://www.wikidata.org/wiki/{wiki_id}")
        place = item.get_apis_entity()
        location_node = ET.Element(
            "{http://www.tei-c.org/ns/1.0}location", attrib={"type": "coordinates"}
        )
        x.insert(1, location_node)
        geo = ET.SubElement(location_node, "{http://www.tei-c.org/ns/1.0}geo")
        geo.text = f"{place['lat']} {place['lng']}"
ET.indent(doc.any_xpath(".")[0], space="   ")
doc.tree_to_file(listplace)
