# -*- coding: utf-8 -*-
import requests


#source: https://www.ruv.is/frett/2020/10/30/domstolar-nyta-ekki-fjarfundarbunad-sem-skyldi
article = """Saloth Sar, betur þekktur sem Pol Pot, var fæddur 19. maí 1925 og dó 15. apríl 1998.  Hann var leiðtogi Rauðu khmeranna í Kambódíu frá 1963 til 1979 og er þekktastur fyrir dauða  óhemjumargs fólks í stjórnartíð sinni, sem var  frá 1975 til 1979. Rauðu khmerarnir reyndu að   framfylgja sýn sinni um samyrkjuvæðingu, en meðal þess sem hún átti að fela í sér var að borgarbúar flyttu út í sveitir og ynnu þar við landbúnað eða í betrunarvinnu. Þeir töldu sig geta byrjað siðmenninguna upp á nýtt og tóku því upp tímatal sem átti að hefjast með valdatíð þeirra.  Sú valdatíð var ekki löng, en því mannskæðari. Þrælkunarvinna, vannæring, hrun í heilbrigðiskerfinu og beinar aftökur kostuðu á bilinu 750.000 - 1.700.000 manns lífið (sumir segja á bilinu 300.000 til 3.000.000) -- í landi sem hafði 14 milljónir íbúa árið 2006. Meðal þeirra sem voru ofsóttir voru menntamenn og aðrir „borgaralegir óvinir“, sem taldir voru hættulegir"""

r = requests.post("http://0.0.0.0:8080/hyphenator", params={'text':article})
exp = 'Ákærendafélag Íslands segir að dómstólar séu of illa búnir til að geta nýtt sér bráðabirgðaheimild til málsmeðferða í gegnum fjarfundarbúnað. Umsýsla dómstóla segir að tæknilausnir séu til staðar en að unnið sé að úrbótum. Í vor var sett í lög bráðabirgðaákvæði þess efnis að heimilt sé að skýrslutaka og önnur málsmeðferð fari fram í gegnum fjarfundarbúnað. Í umsögn Ákærendafélags Íslands kemur fram að dómstólar hafi ekki nýtt sér þessa heimild eins og kostur er bestur í ljósi þess tækjabúnaður sé ekki fullnægjandi.'
print(r.text)
assert exp == r.text
