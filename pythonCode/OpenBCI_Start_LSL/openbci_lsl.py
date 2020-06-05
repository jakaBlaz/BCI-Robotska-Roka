#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
  openbci_lsl.py
  ---------------

  This is the main module for establishing an OpenBCI stream through the Lab Streaming Layer (LSL).

  Lab streaming layer is a networking system for real time streaming, recording, and analysis of time-series 
  data. LSL can be used to connect OpenBCI to applications that can record, analyze, and manipulate the data, 
  such as Matlab, NeuroPype, BCILAB, and others.

  To run the program as a GUI application, enter `python openbci_lsl.py`. 

  To run the program as a command line interface, enter `python openbci_lsl.py [port] --stream`. The port argument
  is optional, since the program automatically detects the OpenBCI port. However, if this functionality fails, the 
  port must be specified as an argument.

  For more information, see the readme on the Github repo:

  https://github.com/gabrielibagon/OpenBCI_LSL

'''

import sys
import lib.streamerlsl as streamerlsl
import random

sys.path.append('/usr/local/Cellar/pyqt@4/4.12.1_1/lib/python2.7/site-packages') #inštalacija PyQt4

### set stream parameters ###
random_id = random.randint(0,255)
stream1 = {'name': 'openbci_eeg',
          'type': 'EEG',
          'channels': 4,
          'sample_rate': 200.0,
          'datatype': 'float32',
          'id': 'openbci_eeg_id' + str(random_id)} # Hz
stream2 = {'name': 'openbci_aux',
          'type': 'AUX',
          'channels': 3,
          'sample_rate': 200.0,
          'datatype': 'float32',
          'id': 'openbci_aux_id' + str(random_id)}
#############################

def main(argv):  
  # if no arguments are provided, default to the stream parameters specified below
  if not argv:
    lsl = streamerlsl.StreamerLSL(GUI=False)
    
    '''
    # PyQt4 Gui ne dela, ker je pač PyQt4!
    import lib.gui as gui
    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    window = gui.GUI()
    sys.exit(app.exec_())
    '''
  # if user specifies CLI using the "--stream" argument, check if a port is also specified
  else:                                             # izklopljen GUI
    if argv[0] == '--stream':                       # ni definiran port /dev/tty.*
      lsl = streamerlsl.StreamerLSL(GUI=False)
    else:                                           # definiran port /dev/tty.*
      try:
        if argv[1] != '--stream':
          print ("Command '%s' not recognized" % argv[1])
          return
      except IndexError:
        print("Command '%s' not recognized" % argv[0])
        return
      port = argv[0]
      lsl = streamerlsl.StreamerLSL(port=port,GUI=False)
  lsl.create_lsl(stream1=stream1, stream2=stream2)
  lsl.begin()
    

if __name__ == '__main__':
  main(sys.argv[1:])
