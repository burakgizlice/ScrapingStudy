from parsel import Selector

def get_opponents(html):
    selector = Selector(text=html)

    matches = selector.xpath('//table[@class="wikitable"]')[0]
    trs = matches.xpath(".//tr")

    opponents = []
    for tr in trs[1:]:
        opponent = {
            'name': None,
            'URL': None
        }

        opponent_node = tr.xpath("./td[3]")
        a = opponent_node.xpath('a')

        outcome = tr.xpath("./td[1]/text()").get()
        opponent["outcome"] = outcome.strip('\n')

        if len(a) == 1:
            link = opponent_node.xpath("a/@href").get()
            opponent["URL"] = f"https://en.wikipedia.org{link}"
            opponent_name = a.xpath('text()').get()
            opponent["name"] = opponent_name.strip("\n")
        else:
            opponent_name = opponent_node.xpath("text()").get()
            opponent["name"] = opponent_name.strip("\n")
        opponents.append(opponent)
    return opponents