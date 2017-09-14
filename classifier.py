#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nltk
from nltk.corpus import stopwords
from textblob.classifiers import NaiveBayesClassifier


class Classifier:

    def __init__(self):
        self.train = [
            ('no quiero estudiar', 'triste'),
            ('no me gusta la universidad', 'triste'),
            ('me gusta ir a clases', 'felicidad'),
            ('este ramo es genial', 'felicidad'),
            ('me fue mal en la prueba', 'enojo'),
            ('estaba dificil la prueba', 'triste'),
            ('me fue como el hoyo en la prueba', 'triste'),
            ('me cae mal esa persona!', 'enojo'),
            ('odio los lunes', 'enojo'),
            ('al fin es viernes!', 'felicidad'),
            ('me fue bien en la prueba!', 'felicidad'),
            ('hoy fue un gran dia', 'felicidad'),
            ('no me siento bien', 'triste'),
            ('me duele el estomago', 'triste'),
            ('no me siento bien de la cabeza', 'triste'),
            ('me fue bien en la prueba', 'felicidad'),
            ('estaba facil la prueba', 'felicidad'),
            ('me gusta beber cerveza', 'felicidad'),
            ('la chela es rica', 'felicidad'),
        ]
        self.cl = NaiveBayesClassifier(self.train)
    
    def get_sentiment(self, text):
        sentiment = self.cl.classify(text)
        return sentiment
