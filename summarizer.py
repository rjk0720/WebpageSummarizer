#!/usr/bin/env python
# summarizer.py

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize(url):
    LANGUAGE = "english"
    SENTENCES_COUNT = 2
    REMOVE_STOP_WORDS = True

    # url = "https://dototot.com/reply-tweets-python-tweepy-twitter-bot/"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = ""

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        cutSentence = ""

        if REMOVE_STOP_WORDS:
            # Cut out unnecessary words and things
            for word in str(sentence).split():
                word = word.lower()
                if not word in summarizer.stop_words:
                    if cutSentence != "" and not cutSentence.endswith(" "):
                        cutSentence = cutSentence + " "
                    # Capitalize if first word
                    if cutSentence == "":
                        word = word.title()
                    cutSentence += word
                elif word == "and" and not cutSentence.endswith(","):
                    cutSentence += ", "
        else:
            cutSentence = str(sentence)

        if summary != "":
            summary += "\n"
        summary += cutSentence

    chars = len(summary)
    return summary,chars