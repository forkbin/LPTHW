from nose.tools import *
from ex49 import lexicon
from ex49 import sentence


def test_princess():
    list = lexicon.scan("princess go east")
    sen = sentence.parse_sentence(list)
    print "subj: %s, verb: %s, obj: %s" % (sen.subject, sen.verb, sen.object)
    

def test_bear():
    list = lexicon.scan("bear eat door")
    sen = sentence.parse_sentence(list)
    print "subj: %s, verb: %s, obj: %s" % (sen.subject, sen.verb, sen.object)


def test_exception():
    list = lexicon.scan("open the door")
    sen = sentence.parse_sentence(list)
    print "subj: %s, verb: %s, obj: %s" % (sen.subject, sen.verb, sen.object)
