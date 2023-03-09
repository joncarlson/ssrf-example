from xml.dom import pulldom


def parse_location(xml):
    doc = pulldom.parse(xml)

    isLocation = False
    locations = []

    for event, node in doc:
        if event == pulldom.END_ELEMENT and node.tagName == 'location':
            isLocation = False

        if event == pulldom.START_ELEMENT and node.tagName == 'location':
            isLocation = True

        if event == pulldom.CHARACTERS and isLocation:
            locations.append(node.nodeValue)

    return locations
