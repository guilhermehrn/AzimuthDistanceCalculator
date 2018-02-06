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
stdlib_dir = os.path.dirname(os.__file__)
print stdlib_dir
real_distutils_path = sys.path

__path__.append('C:\Users\09726968658\.qgis2\python\plugins\AzimuthDistanceCalculator\ENV\Lib\site-packages')
#execfile(os.path.join(real_distutils_path, '__init__.py'))
print __path__
def classFactory(iface):
    # load AzimuthDistanceCalculator class from file AzimuthDistanceCalculator
    from azimuthdistancecalculator import AzimuthDistanceCalculator
    return AzimuthDistanceCalculator(iface)
