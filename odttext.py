#! /usr/bin/env python
# -*- coding: utf-8 -*-

from odf.opendocument import OpenDocumentText
from odf.draw import Frame, Image, Page
from odf.style import Style, TextProperties, ParagraphProperties, PageLayoutProperties, PageLayout, MasterPage, GraphicProperties, TableColumnProperties
from odf.text import H, P, Span
from odf.table import Table, TableColumn, TableRow, TableCell

FULL_MONTHS = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro', 'outubro','novembro','dezembro']
title = 'MINISTÉRIO DO PLANEJAMENTO, DESENVOLVIMENTO E GESTÃO SECRETARIA DO PATRIMÔNIO DA UNIÃO'
subTitle = 'Memorial Descritivo'
logo = 'C:/Users/09726968658/.qgis2/python/plugins/AzimuthDistanceCalculator/azimuthsAndDistances/templates/template_memorial_pdf/rep_of_brazil.png'
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
h1style.addElement(ParagraphProperties(attributes={"textalign":"center"}))
s.addElement(h1style)

#"marginbottom":"12.5cm", "marginright":"30mm", "marginleft":"30mm", "margintop":"125mm"

# An automatic style
boldstyle = Style(name="Bold", family="paragraph")

boldstyle.addElement(TextProperties(attributes={'fontsize':"12pt"}))
boldstyle.addElement(ParagraphProperties(attributes={"textalign":"justify"}))
s.addElement(boldstyle)
textdoc.automaticstyles.addElement(boldstyle)


#imgStile
imgstyle = Style(name="Mfr1", family="graphic")
imgprop = GraphicProperties(horizontalrel="paragraph",horizontalpos="center", verticalrel="paragraph-content",verticalpos="top",)
imgstyle.addElement(imgprop)
textdoc.automaticstyles.addElement(imgstyle)
# Text

textdoc.masterstyles.addElement(masterpage)

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

h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)
h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)
h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)
h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)
h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style, text=title.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=h1style, text=subTitle.decode('utf-8'))
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
cell = TableCell(valuetype="text", currency="AUD", value="-125")
cell.addElement(P(text=u"Imóvel: " + denominacaoArea.decode('utf-8'))) # The current displayed value
tr.addElement(cell)

tr = TableRow()
table.addElement(tr)

# Create a column (same as <col> in HTML) Make all cells in column default to currency
table.addElement(TableColumn(numbercolumnsrepeated=0, stylename=widewidth, defaultcellstylename="co1"))
table.addElement(TableColumn(numbercolumnsrepeated=1, stylename=widewidth, defaultcellstylename="co1"))
# Create a row (same as <tr> in HTML)
tr = TableRow()
table.addElement(tr)
# Create a cell with a negative value. It should show as red.
cell = TableCell(valuetype="text", currency="AUD", value="-125")
cell.addElement(P(text=u"$-125.00")) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="text", currency="AUD", value="-125")
cell.addElement(P(text=u"$-125.00")) # The current displayed value
tr.addElement(cell)

# Create a row (same as <tr> in HTML)
tr = TableRow()
table.addElement(tr)
# Create another cell but with a positive value. It should show in black
cell = TableCell(valuetype="currency", currency="AUD", value="123")
cell.addElement(P(text=u"$123.00")) # The current displayed value
tr.addElement(cell)

cell = TableCell(valuetype="currency", currency="AUD", value="123")
cell.addElement(P(text=u"$123.00")) # The current displayed value
tr.addElement(cell)


textdoc.text.addElement(table)









h=H(outlinelevel=1, stylename=h1style, text='Descrição'.decode('utf-8'))
textdoc.text.addElement(h)

h=H(outlinelevel=1, stylename=boldstyle, text='\n')
textdoc.text.addElement(h)


p = P(text=texto2, stylename=boldstyle)
#boldpart = Span(stylename=boldstyle, text="This part is bold. ")
#p.addElement(boldpart)
#p.addText("This is after bold.")
textdoc.text.addElement(p)
textdoc.save("myfirstdocument.odt")
