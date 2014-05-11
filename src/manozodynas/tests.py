# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting
from lxml.cssselect import CSSSelector
from manozodynas.models import *
from django.test import Client


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)

class WordInsertTest(StatefulTesting):
    def test_word_insert(self):
        self.open(reverse('word'))
        self.assertStatusCode(200)
        qs = Word.objects.all()
        self.assertFalse(qs.filter(word='test', category='n').exists())
        self.selectForm('#word_form')
        self.submitForm({
             'word': 'test',
             'category': 'n',
        })
        self.assertStatusCode(302)
        self.assertTrue(qs.filter(word='test', category='n').exists())

class TranslationInsertTest(StatefulTesting):
    def test_translation_insert(self):
        c = Client()
        response = c.post('/word', {
             'word': 'test_word',
             'category': 'adj',
        })
        self.assertEqual(response.status_code, 302)
        qs = Word.objects.all()
        self.assertTrue(qs.filter(word='test_word').exists())
        word = qs.get(word='test_word')
        self.assertEqual(word.word, 'test_word')
        id = str(word.id)
	response = c.post('/word/'+id+'/translate/', {
             'translation': 'test_translation',
             'description': 'test_description',
        })
        self.assertEqual(response.status_code, 302)
        qs = Translation.objects.all()
        self.assertTrue(qs.filter(translation='test_translation', 
                                  description='test_description',
                                  srcWord=word).exists())

class WordDeleteTest(StatefulTesting):
    def test_word_delete(self):
        c = Client()
        response = c.post('/word', {
             'word': 'test_word',
             'category': 'adj',
        })
        self.assertEqual(response.status_code, 302)
        qs = Word.objects.all()
        self.assertTrue(qs.filter(word='test_word').exists())
        word = qs.get(word='test_word')
        id = str(word.id)
	response = c.post('/word/'+id+'/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(qs.filter(word='test_word').exists())
