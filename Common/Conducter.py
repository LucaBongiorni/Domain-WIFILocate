# -*- coding: utf-8 -*-
import subprocess
import json
from pprint import pprint
from Helpers import helpers
from Common import kmlBuilder
from Common import wigleAPI


class Conducter:


    def __init__(self, filename, kmlname, username, password, verbose=False):

        self.ResultsList = []
        self.WifiPoints = []
        self.WigleUser = str(username)
        self.WiglePassword = str(password)
        self.Verbose = verbose
        self.FileName = str(filename)
        self.KMLname = str(kmlname)
        self.LoadedJson = ""
        self.NetworkList = []

    def TaskController(self):
        self.LoadJson()
        self.ParseJson()
        self.BuildObject()

    def LoadJson(self):
        '''
        Takes the loaded JSON file, and loads it into
        a JSON dict.
        '''
        try:
            with open(self.FileName, "r") as myfile:
                print " [*] File has been loaded"
                try:
                    jsonObj = json.load(myfile)
                    # pprint(jsonObj)
                    self.LoadedJson = jsonObj
                except Exception as e:
                    print e
        except Exception as e:
            print e

    def ParseJson(self):
        try:
            Networks = self.LoadedJson['Networks']
            for item in Networks:
                self.NetworkList.append(item)
        except Exception as e:
            print e

    def BuildObject(self):
        '''
        This func will build one obj
        and return the obj.
        '''
        try:
            # simply pass to my wigle api class
            wa = wigleAPI.WigleAgent(self.WigleUser, self.WiglePassword)
            for Network in self.NetworkList:
                final = wa.get_lat_lng(str(Network['DefaultGatewayMac']))
                if final:
                    print final
        except Exception as e:
            print e



