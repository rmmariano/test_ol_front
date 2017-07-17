#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Responsible module to create handlers.
"""


from .base_controller import BaseHandler


class IndexHandler(BaseHandler):
    """
        Responsible class to render the Home Page (Index).
    """

    # A list of URLs that can be use for the HTTP methods
    urls = [r"/", r"/index", r"/index/"]

    def get(self):
        """
            Responsible method to be the GET method for the URLs listed in the attribute called urls.

            Args:
                Nothing until the moment.

            Returns:
                Just render the index page with some context given.

            Raises:
                Nothing until the moment.
        """

        # Some fictional context
        context = {"text": "Welcome"}

        # The ** before the context do that dictionary is "break" in the positions of the render method
        # The under line is like this: self.render("index.html", text = "Welcome")
        self.render("index.html", **context)


class OpenLayersBasicExampleHandler(BaseHandler):
    # https://openlayers.org/en/latest/doc/quickstart.html

    # A list of URLs that can be use for the HTTP methods
    urls = [r"/test_ol_basic_example", r"/test_ol_basic_example/"]

    def get(self):
        # Some fictional context
        context = {"text": "Basic Example"}

        # The ** before the context do that dictionary is "break" in the positions of the render method
        # The under line is like this: self.render("index.html", text = "Welcome")
        self.render("ol/test_ol_basic_example.html", **context)


class OL3BeginnersGuide01Handler(BaseHandler):
    # https://openlayersbook.github.io/ch01-getting-started-with-openlayers/example-01.html

    urls = [r"/ol3beginnersguide/01", r"/ol3beginnersguide/01/"]

    def get(self):
        context = {"text": "Creating your first map"}

        self.render("ol/ol3beginnersguide/01.html", **context)
