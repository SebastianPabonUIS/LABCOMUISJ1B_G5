# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Calculo Potencia
# Author: Edson Rey & Sebastian Pabon
# Copyright: UIS
# GNU Radio version: 3.10.1.1

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
import ModulosEfren







class CalculoPotencia(gr.hier_block2, Qt.QWidget):
    def __init__(self, l_vect=1024):
        gr.hier_block2.__init__(
            self, "Calculo Potencia ",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(0, 0, 0),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.l_vect = l_vect

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.fft_vxx_0 = fft.fft_vfc(l_vect, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, l_vect)
        self.blocks_nlog10_ff_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 30)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1/(2*135115.625))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(l_vect)
        self.Potenciaw = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Potenciaw.set_update_time(0.10)
        self.Potenciaw.set_title("Potencia lineal [W]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['  [W]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Potenciaw.set_min(i, -1)
            self.Potenciaw.set_max(i, 1)
            self.Potenciaw.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Potenciaw.set_label(i, "Data {0}".format(i))
            else:
                self.Potenciaw.set_label(i, labels[i])
            self.Potenciaw.set_unit(i, units[i])
            self.Potenciaw.set_factor(i, factor[i])

        self.Potenciaw.enable_autoscale(True)
        self._Potenciaw_win = sip.wrapinstance(self.Potenciaw.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Potenciaw_win)
        self.PotenciaLogaritimicaw = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaLogaritimicaw.set_update_time(0.10)
        self.PotenciaLogaritimicaw.set_title("Potencia Logaritimica  [dBW]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = [' [dBW]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaLogaritimicaw.set_min(i, -1)
            self.PotenciaLogaritimicaw.set_max(i, 1)
            self.PotenciaLogaritimicaw.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaLogaritimicaw.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaLogaritimicaw.set_label(i, labels[i])
            self.PotenciaLogaritimicaw.set_unit(i, units[i])
            self.PotenciaLogaritimicaw.set_factor(i, factor[i])

        self.PotenciaLogaritimicaw.enable_autoscale(True)
        self._PotenciaLogaritimicaw_win = sip.wrapinstance(self.PotenciaLogaritimicaw.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaLogaritimicaw_win)
        self.PotenciaLogaritimica = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.PotenciaLogaritimica.set_update_time(0.10)
        self.PotenciaLogaritimica.set_title("Potencia Logaritimica  [dBm]")

        labels = ['Potencia', '', '', '', '',
            '', '', '', '', '']
        units = ['[dBm]', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.PotenciaLogaritimica.set_min(i, -1)
            self.PotenciaLogaritimica.set_max(i, 1)
            self.PotenciaLogaritimica.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.PotenciaLogaritimica.set_label(i, "Data {0}".format(i))
            else:
                self.PotenciaLogaritimica.set_label(i, labels[i])
            self.PotenciaLogaritimica.set_unit(i, units[i])
            self.PotenciaLogaritimica.set_factor(i, factor[i])

        self.PotenciaLogaritimica.enable_autoscale(True)
        self._PotenciaLogaritimica_win = sip.wrapinstance(self.PotenciaLogaritimica.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._PotenciaLogaritimica_win)
        self.ModulosEfren_SumaVector_0 = ModulosEfren.SumaVector(l_vect)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModulosEfren_SumaVector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.ModulosEfren_SumaVector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.Potenciaw, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_1, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.PotenciaLogaritimica, 0))
        self.connect((self.blocks_nlog10_ff_1, 0), (self.PotenciaLogaritimicaw, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def get_l_vect(self):
        return self.l_vect

    def set_l_vect(self, l_vect):
        self.l_vect = l_vect

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

