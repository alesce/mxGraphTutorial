#!/usr/bin/python

import xml.etree.ElementTree as xml
import random
shows = [(1, 'Mutts and Mongrels', 'June 10, 2045', 'Snootshire, Fancyplace')]
breeds = [
    (1,'Husky','http://ourworldofdogs.com/wp-content/uploads/2012/02/1290177_61857006-150x150.jpg','9:00 am'),
    (2,'Collie','http://ourworldofdogs.com/wp-content/uploads/2012/02/781676_83673737-150x150.jpg', '10:00 am'),
    (3,'Irish Wolfhound', 'http://ourworldofdogs.com/wp-content/uploads/2012/02/Irish-Wolfhound-150x150.jpg','11:00 am'),
]

dogs = [
    (1, 1, 'Floofie', 'Mark Steyn'),
    (2, 1, 'Snoofie', 'Rush Limbaugh'),
    (3, 1, 'Doofie', 'Sean Hanitty'),
    (4, 2, 'Arfie', 'Dianne Rheme'),
    (5, 2, 'Scarfie', 'Terri Gross'),
    (6, 2, 'Barfie', 'Ira Gross'),
    (7, 3, 'C-Sharp', 'Ludwig Beethoven'),
    (8, 3, 'D-minor', 'Amadeu Mozart'),
    (9, 3, 'G-minor', 'Engelbert Humperdink')
]


model = xml.Element('mxGraphModel')
root = xml.Element('root')
model.append(root)
zero = xml.Element('mxCell',id='0')
one = xml.Element('mxCell',id='1', parent='0')
root.append(zero)
root.append(one)

for show in shows:
    newCell=xml.Element('mxCell', id='show-'+str(show[0]), value= show[1]+' '
                        +show[2]+' ,'+show[3], vertex='1', parent='1',
                        style="label;verticalLabelPosition=middle;verticalAlign=top" )
    newMxGeometry=xml.Element('mxGeometry', x='0', y='0', width='600', height='1200')
    newMxGeometry.set('as','geometry')
    newCell.append(newMxGeometry)
    root.append(newCell)

for breed in breeds:   
    newCell=xml.Element('mxCell', id='breed-'+str(breed[0]), value=breed[1]+' - '+breed[3],
                        vertex='1', parent='show-1', style="icon;image="+breed[2])
    newMxGeometry=xml.Element('mxGeometry', height='150', width = '150')
    newMxGeometry.set('as','geometry')
    newCell.append(newMxGeometry)
    root.append(newCell)

for dog in dogs:
    newCell=xml.Element('mxCell', id='dog'+str(dog[0]), value="Dog's name: "+dog[2]+" -- Owner: "+dog[3],
                        vertex='1', parent='breed-'+str(dog[1]))
    newMxGeometry=xml.Element('mxGeometry', width='300', height='20')
    newMxGeometry.set('as','geometry')
    newCell.append(newMxGeometry)
    root.append(newCell)
    
    

    
file = open("example.xml", 'w')
xml.ElementTree(model).write(file)
file.close()