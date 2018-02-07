# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AzimuthDistanceCalculator
                                 A QGIS plugin
 Calculates azimuths and distances
                             -------------------
        begin                : 2014-09-24
        copyright            : (C) 2014 by Luiz Andrade
        email                : luiz.claudio@dsg.eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import os
import sys
import imp

name_lib_dir = os.path.expanduser("~")
name_lib_dir  = name_lib_dir + '\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\site-packages'
sys.path.append(name_lib_dir)

name_lib_dir = os.path.expanduser("~")
name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\distutils'
sys.path.append(name_lib_dir)

name_lib_dir = os.path.expanduser("~")
name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib'
sys.path.append(name_lib_dir)

name_lib_dir = os.path.expanduser("~")
name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\distutils'
sys.path.append(name_lib_dir)
def classFactory(iface):
    # load AzimuthDistanceCalculator class from file AzimuthDistanceCalculator
    #from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
    # from reportlab.lib.pagesizes import letter
    # from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    # from reportlab.lib.units import inch
    # from datetime import date
    # from reportlab.lib.units import mm
    from azimuthdistancecalculator import AzimuthDistanceCalculator
    return AzimuthDistanceCalculator(iface)
