#! /usr/bin/env python
# -*- coding: utf-8 -*-

from odf.opendocument import OpenDocumentText
from odf.draw import Frame, Image, Page
from odf.style import Style, TextProperties, ParagraphProperties, PageLayoutProperties, PageLayout, MasterPage
from odf.text import H, P, Span

FULL_MONTHS = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
title = 'MINISTÉRIO DO PLANEJAMENTO, DESENVOLVIMENTO E GESTÃO SECRETARIA DO PATRIMÔNIO DA UNIAO'
subTitle = 'Memorial Descritivo'
logo = 'rep_of_brazil.png'
denominacaoArea = 'ÁREA INDUBITÁVEL DA UNIÃO NA ARQ GURUPÁ'
uf = 'PARÁ'
city = 'CACHOEIRA DO ARARI'
sistemGeodesicoRef = 'SIRGAS 2000'
sistemProjectionCartografic = 'UTM 22 SUL'
perimetroMetro = '137974.18'
areaMetroQuad = '34726602.21'
addressBr= 'Brasilia'
responsible = 'ANTONIO AFONSO CORDEIRO JUNIOR'
officeResponsible = 'Geografo'
organization = 'CGIPA/SPU'

textdoc = OpenDocumentText()

dpstyle = Style(family="drawing-page",name="DP1")
textdoc.automaticstyles.addElement(dpstyle)


pagelayout = PageLayout(name="Mpm1")
pagelayout.addElement(PageLayoutProperties(margin="0cm", marginbottom="12.5cm", marginright="300pt", marginleft="30mm", margintop="125mm", pageheight="27mm", pagewidth="297mm", printorientation="portrait"))
textdoc.automaticstyles.addElement(pagelayout)


masterpage = MasterPage(stylename=dpstyle, name="Default", pagelayoutname="Mpm1")



# Styles
s = textdoc.styles
#stile do titulo.
h1style = Style(name="Heading 1", family="paragraph", )
h1style.addElement(TextProperties(attributes={'fontsize':"12pt",'fontweight':"bold"}))
h1style.addElement(ParagraphProperties(attributes={"textalign": "center"}))
s.addElement(h1style)

#"marginbottom":"12.5cm", "marginright":"30mm", "marginleft":"30mm", "margintop":"125mm"

# An automatic style
boldstyle = Style(name="Bold", family="text")
boldprop = TextProperties(fontweight="bold")
boldstyle.addElement(boldprop)
textdoc.automaticstyles.addElement(boldstyle)
# Text

textdoc.masterstyles.addElement(masterpage)

arq = open('text.txt','r')
texto = arq.read()
texto2 =texto.decode('utf-8')

# photoframe = Frame(width="200pt", height="200pt", x="56pt", y="56pt")
# href = textdoc.addPicture(logo)
# photoframe.addElement(Image(href=href))
# page.addElement(photoframe)
arq.close()
h=H(outlinelevel=1, stylename=h1style, text=title.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style, text=subTitle.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style, text='Descrição'.decode('utf-8'))
textdoc.text.addElement(h)


p = P(text=texto2)
boldpart = Span(stylename=boldstyle, text="This part is bold. ")
p.addElement(boldpart)
p.addText("This is after bold.")
textdoc.text.addElement(p)
textdoc.save("myfirstdocument.odt")
