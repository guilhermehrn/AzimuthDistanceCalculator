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
from __future__ import absolute_import

import os
import sys
import imp


currentDirectoryPath = os.path.dirname(__file__)
#print currentDirectoryPath

libraryDirectoryPath = os.path.join(currentDirectoryPath, 'ENV/Lib/site-packages')
#print libraryDirectoryPath
sys.path.append(libraryDirectoryPath)

libraryDirectoryPath = os.path.join(currentDirectoryPath, 'ENV/Lib/distutils')
#print libraryDirectoryPath
#name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\distutils'
sys.path.append(libraryDirectoryPath)

libraryDirectoryPath = os.path.join(currentDirectoryPath, 'ENV/Lib')
#print libraryDirectoryPath
#name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib'
sys.path.append(libraryDirectoryPath)

libraryDirectoryPath = os.path.join(currentDirectoryPath, 'ENV/Lib/distutils')
#print libraryDirectoryPath
#name_lib_dir  = name_lib_dir +'\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\distutils'


sys.path.append(libraryDirectoryPath)
def classFactory(iface):
    # load AzimuthDistanceCalculator class from file AzimuthDistanceCalculator
    from .azimuthdistancecalculator import AzimuthDistanceCalculator
    return AzimuthDistanceCalculator(iface)
