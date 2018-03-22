#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rlextra.rml2pdf import rml2pdf
from odf.opendocument import OpenDocumentText
from odf.draw import Frame, Image, Page
from odf.style import Style, TextProperties, ParagraphProperties, PageLayoutProperties, PageLayout, MasterPage, GraphicProperties, TableColumnProperties
from odf.text import H, P, Span
from odf.table import Table, TableColumn, TableRow, TableCell

FULL_MONTHS = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
title = 'MINISTÉRIO DO PLANEJAMENTO, DESENVOLVIMENTO E GESTÃO'
title2= 'SECRETARIA DO PATRIMÔNIO DA UNIÃO'
subTitle = 'Memorial Descritivo xxxx/2018'
logo = 'C:/Users/09726968658/.qgis2/python/plugins/AzimuthDistanceCalculatorSPU/azimuthsAndDistances/templates/template_memorial_pdf/rep_of_brazil.png'
denominacaoArea = 'ÁREA INDUBITÁVEL DA UNIÃO NA ARQ GURUPÁ'
uf = 'PARÁ'
city = 'CACHOEIRA DO ARARI'
sistemGeodesicoRef = 'SIRGAS 2000'
sistemProjectionCartografic = 'UTM 22 SUL'
perimetroMetro = '137974.18'
areaMetroQuad = '34726602.21'
addressBrCity= 'Brasilia'
responsible = 'GUILHERME HENRIQUE'
officeResponsible = 'Analista de Sistemas'
organization = 'DIIUP/SPU/MG'

Superinte = "Superintendência do Patrimônio da União em Minas Gerais"
divisao = "Divisão de Identificação e Controle de Utilização do Patrimônio"
adresstitle="Av. Afonso Pena, 1316, 11º andar, Ala A, 30130-003, Belo Horizonte/MG"

textdoc = OpenDocumentText()

#dpstyle = Style(family="drawing-page",name="DP1")
#textdoc.automaticstyles.addElement(dpstyle)

s = textdoc.styles

pagelayout = PageLayout(name="Mpm1")
pagelayout.addElement(PageLayoutProperties(marginbottom="-1.25cm", marginright="3cm", marginleft="3cm"))
textdoc.automaticstyles.addElement(pagelayout)

masterpage = MasterPage(stylename="da", name="Default", pagelayoutname=pagelayout)
textdoc.masterstyles.addElement(masterpage)

h1style = Style(name="Heading 1", family="paragraph")
h1style.addElement(TextProperties(attributes={'fontsize':"10.5pt",'fontweight':"bold", 'fontfamily':"Times New Roman"}))
h1style.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style)

h1style2 = Style(name="Heading2 1", family="paragraph")
h1style2.addElement(TextProperties(attributes={'fontsize':"10.5pt",'fontweight':"bold", 'fontfamily':"Times New Roman"}))
h1style2.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style2)

h1style2a = Style(name="Heading2a 1", family="paragraph")
h1style2a.addElement(TextProperties(attributes={'fontsize':"10pt",'fontweight':"bold", 'fontfamily':"Times New Roman"}))
h1style2a.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style2a)

addressTitle = Style(name="addressTitle", family="paragraph")
addressTitle.addElement(TextProperties(attributes={'fontsize':"9pt", 'fontfamily':"Times New Roman"}))
addressTitle.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(addressTitle)

h1style3 = Style(name="Heading3 1", family="paragraph")
h1style3.addElement(TextProperties(attributes={'fontsize':"12pt",'fontweight':"bold", 'fontfamily':"Times New Roman", 'textunderlinewidth':"auto", 'textunderlinestyle':"solid"}))
h1style3.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style3)

h1style4 = Style(name="Heading4 1", family="paragraph")
h1style4.addElement(TextProperties(attributes={'fontsize':"12pt",'fontweight':"bold", 'fontfamily':"Times New Roman"}))
h1style4.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style4)

texttable = Style(name="texttable", family="paragraph")
texttable.addElement(TextProperties(attributes={'fontsize':"10.5pt", 'fontfamily':"Times New Roman"}))
texttable.addElement(ParagraphProperties(attributes={"textalign":"left"}))
s.addElement(texttable)

# An automatic style
bodystyle = Style(name="Body", family="paragraph")
bodystyle.addElement(TextProperties(attributes={'fontsize':"11pt", 'fontfamily':"Times New Roman"}))
bodystyle.addElement(ParagraphProperties(attributes={"textalign":"justify"}))
s.addElement(bodystyle)
textdoc.automaticstyles.addElement(bodystyle)

bodystyle2 = Style(name="Body2", family="paragraph")
bodystyle2.addElement(TextProperties(attributes={'fontsize':"11pt", 'fontfamily':"Times New Roman"}))
bodystyle2.addElement(ParagraphProperties(attributes={"textalign":"right"}))
s.addElement(bodystyle2)
textdoc.automaticstyles.addElement(bodystyle2)

bodystyle3 = Style(name="Body3", family="paragraph")
bodystyle3.addElement(TextProperties(attributes={'fontsize':"11pt", 'fontweight':"bold", 'fontfamily':"Times New Roman"}))
bodystyle3.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(bodystyle3)
textdoc.automaticstyles.addElement(bodystyle3)

bodystyle4 = Style(name="Body4", family="paragraph")
bodystyle4.addElement(TextProperties(attributes={'fontsize':"11pt", 'fontfamily':"Times New Roman"}))
bodystyle4.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(bodystyle4)
textdoc.automaticstyles.addElement(bodystyle4)

#imgStile
imgstyle = Style(name="Mfr1", family="graphic")
imgprop = GraphicProperties(horizontalrel="paragraph", horizontalpos="center", verticalrel="paragraph-content", verticalpos="top")
imgstyle.addElement(imgprop)
textdoc.automaticstyles.addElement(imgstyle)
# Text
#textdoc.masterstyles.addElement(masterpage)

arq = open('text.txt','r')
texto = arq.read()
texto2 =texto.decode('utf-8')

#insert image
p=P()
textdoc.text.addElement(p)
href = textdoc.addPicture(logo)
imgframe = Frame(name="fig1", anchortype="paragraph", width="2.24cm", height="2.22cm", zindex="0", stylename=imgstyle)
p.addElement(imgframe)
img = Image(href=href, type="simple", show="embed", actuate="onLoad")

imgframe.addElement(img)

arq.close()

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style, text=title.decode('utf-8'))
textdoc.text.addElement(h)
h=H(outlinelevel=1, stylename=h1style, text=title2.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style2, text=Superinte.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style2a, text=divisao.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=addressTitle, text=adresstitle.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style3, text=subTitle.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

# Create automatic styles for the column widths.
widewidth = Style(name="co1", family="table-column")
widewidth.addElement(TableColumnProperties(columnwidth="8cm"))
textdoc.automaticstyles.addElement(widewidth)

# Start the table, and describe the columns
table = Table(name="Currency colours")

table.addElement(TableColumn(stylename=widewidth, defaultcellstylename="co1"))
tr = TableRow()
table.addElement(tr)

# Create a cell with a negative value. It should show as red.
cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"Imóvel: " + denominacaoArea.decode('utf-8'), stylename=texttable)) # The current displayed value
tr.addElement(cell)

tr = TableRow()
table.addElement(tr)

cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"Proprietário:", stylename=texttable)) # The current displayed value
tr.addElement(cell)

tr = TableRow()
table.addElement(tr)

cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"Endereço: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

# Create a column (same as <col> in HTML) Make all cells in column default to currency
table.addElement(TableColumn(numbercolumnsrepeated=0, stylename=widewidth, defaultcellstylename="co1"))
table.addElement(TableColumn(numbercolumnsrepeated=1, stylename=widewidth, defaultcellstylename="co1"))
# Create a row (same as <tr> in HTML)
tr = TableRow()
table.addElement(tr)
# Create a cell with a negative value. It should show as red.
cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"Município/UF: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"NBP: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

# Create a row (same as <tr> in HTML)
tr = TableRow()
table.addElement(tr)
# Create another cell but with a positive value. It should show in black

cell = TableCell(valuetype="text", currency="AUD", value="123")
cell.addElement(P(text=u"Área (m²): ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="text", currency="AUD", value="123")
cell.addElement(P(text=u"Código SNCR: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

tr = TableRow()
table.addElement(tr)

cell = TableCell(valuetype="text", currency="AUD", value="123")
cell.addElement(P(text=u"Perímetro (m): ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="text", currency="AUD", value="123")
cell.addElement(P(text="RIP: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

tr = TableRow()
table.addElement(tr)

cell = TableCell(valuetype="text", currency="AUD", value="123")
cell.addElement(P(text=u"Comarca: ", stylename=texttable)) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="text", currency="AUD")
cell.addElement(P(text=u"Matrícula: -- ", stylename=texttable)) # The current displayed value
tr.addElement(cell)



textdoc.text.addElement(table)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style4, text='DESCRIÇÃO'.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

p = P(text=texto2, stylename=bodystyle)
textdoc.text.addElement(p)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

p = P(text="Belo Horizonte, 10 de Outubro de 2016", stylename=bodystyle2)
textdoc.text.addElement(p)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=bodystyle, text='\n')
textdoc.text.addElement(h)

p = P(text=responsible, stylename=bodystyle3)
textdoc.text.addElement(p)

p = P(text=officeResponsible, stylename=bodystyle4)
textdoc.text.addElement(p)

p = P(text=organization, stylename=bodystyle4)
textdoc.text.addElement(p)

temp = textdoc.xml()

output = 'docpdf.pdf'
rml2pdf.go(temp, outputFileName=output)
argw = open("xmldoc.xml", "w")
argw.write(temp)
argw.close()
textdoc.save("myfirstdocument.odt")
