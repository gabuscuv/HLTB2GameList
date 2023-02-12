#!/usr/bin/python3
import os
from HLTB2GameList import HLTB2GameList

##TODO Commandline Interface

HLTB2GameList(os.getenv("HOME",".")+"/"+"GameLists.db").run()
