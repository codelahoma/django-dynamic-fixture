# -*- coding: utf-8 -*-
import pytest

from django.test import TestCase

from ddf import *


class SampleAppTestCase(TestCase):
    def test_category(self):
        o = G('django_dynamic_fixture.Category')
        assert o.name is not None
        assert o.parent is None
        o = G('django_dynamic_fixture.Category', self_fk_depth=1)
        assert o.parent is not None
        assert o.parent.parent is None

    # def test_author(self):
    #     o = G('django_dynamic_fixture.Author')
    #     assert o.name is not None
    #     assert o.description is None
    #     o = G('django_dynamic_fixture.Author', fill_nullable_fields=True)
    #     assert o.description is not None

    # def test_publisher(self):
    #     o = G('django_dynamic_fixture.Publisher')
    #     assert o.name is not None

    # def test_book(self):
    #     o = G('django_dynamic_fixture.Book')
    #     assert o.main_author is not None
    #     assert o.main_author.name is not None
    #     assert o.authors.all().count() == 0
    #     assert o.categories.all().count() == 0
    #     o = G('django_dynamic_fixture.Book', authors=2, categories=5)
    #     assert o.authors.all().count() == 2
    #     assert o.categories.all().count() == 5

    # def test_book_edition(self):
    #     o = G('django_dynamic_fixture.BookEdition')
    #     assert o.book is not None
    #     assert o.year is not None
    #     assert o.publishers.all().count() == 0
    #     o = G('django_dynamic_fixture.BookEdition', publishers=2)
    #     assert o.publishers.all().count() == 2
    #     # assert o.publishers.all()[0].comments is not None
    #     # assert o.edition_publishers.all()[0].comments is not None

    # def test_book_publisher(self):
    #     o = G('django_dynamic_fixture.BookPublisher')
    #     assert o.book_edition.book is not None
    #     assert o.publisher is not None
    #     assert o.comments is not None
