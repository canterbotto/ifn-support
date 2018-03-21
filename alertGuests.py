import sys
import os
import glob
import ts3lib as ts
import ts3defines

from pluginhost import PluginHost

import pytson
from ts3plugin import ts3plugin


class IFNSupport(ts3plugin):
    name = "IFN Support Plugin"
    requestAutoload = False
    version = "1.0"
    apiVersion = 21
    author = "RuskiPotato"
    description = "A plugin created to help IFN Support Staff do their duties - fully client sided."
    offersConfigure = True
    commandKeyword = "pySupport"
    infoTitle = "IFN Support Assistant - Plugin"
    menuItems = []
    hotkeys = []
    
    def __init__(self):
        print("If you experience any issues please contact RuskiPotato (Canter#0548 on discord)")
        global clientid, lobbyid, waitingRoomid
        clientid = ts.getClientID(1)[1]
        lobbyid = 17227
        waitingRoomid = 17233
        print("Initiated")

    def onClientMoveEvent(self, serverConnectionHandlerID, clientID, oldChannelID, newChannelID, visibility, moveMessage):
        print(self, serverConnectionHandlerID, clientID, oldChannelID, newChannelID, visibility, moveMessage)
        if serverConnectionHandlerID != 1: return
        if newChannelID == lobbyid or newChannelID == waitingRoomid: return
            