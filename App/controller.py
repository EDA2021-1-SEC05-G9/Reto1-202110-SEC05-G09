﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv

# Inicialización del Catálogo de videos
def initCatalog(listType):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(listType)
    return catalog

def loadData(catalog):
    
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Funciones para la carga de datos


def loadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for category in input_file:
        model.addCategory(catalog, category)


# Funciones de consulta sobre el catálogo

# Funciones de ordenamiento

def sortVideos(catalog, size, method):
    'Sort videos by views'
    return model.sortVideos(catalog, size, method)

def videosCountry(catalog, country):
    return model.videosCountry(catalog, country)

def videosCountryTrendingResumed(lst):
    return model.videosCountryTrendingResumed(lst)

def videosLikesCountryTags(catalog, pais,tag):
    return model.videosLikesCountryTags(catalog, pais,tag)

def videosCountryCategory(catalog, pais, categoria):
    return model.videosCountryCategory(catalog, pais, categoria)

def videosCategoryTrendingResumed(catalog, category):
    return model.videosCategoryTrendingResumed(catalog, category)