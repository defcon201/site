from migen.fhdl.std import *
from mibuild.generic_platform import *
from mibuild.platforms import papilio_pro
from misoclib.uart import UARTRX


# antenna pin description to place at one of the free GPIOs on the board
_transmitter_io = [
	("antenna", 0, Pins("A:0"), IOStandard("LVTTL"))
]


# clock manager generating 300 MHz clock
class ClockGen(Module):
	def __init__(self, platform):
		self.clock_domains.cd_sys = ClockDomain(reset_less=True)

		clk300_unbuffered = Signal()
		self.specials += Instance("DCM_CLKGEN",
			p_CLKFXDV_DIVIDE=8, p_CLKFX_DIVIDE=8, p_CLKFX_MD_MAX=9.375, p_CLKFX_MULTIPLY=75,
			p_CLKIN_PERIOD=31.25, p_SPREAD_SPECTRUM="NONE", p_STARTUP_WAIT="TRUE",
		
			i_CLKIN=platform.request("clk32"), o_CLKFX=clk300_unbuffered,
			i_FREEZEDCM=0, i_RST=0)
		self.specials += Instance("BUFG", i_I=clk300_unbuffered, o_O=self.cd_sys.clk)


# Phase Accumulator module generating the target output frequencies
# The magic happens here!
class PhaseAccumulator(Module):
	def __init__(self, ??):
		self.out = Signal()

		## your code here


class FMTransmitter(Module):
	def __init__(self, antenna, serial):
		# Clock generator module
		self.submodules.cg = ClockGen(platform)
		clk_freq = 300000000  # 300 MHz

		# UART receiver settings
		baud = 115200	# UART transmission speed

		# UART receiver
		self.submodules.uart = UARTRX(
			serial,
			baud*2**32//clk_freq)
		self.uart.source.payload.d.signed = True
		sample = Signal((8, True)) # the (signed) sound sample for you to transmit
		self.comb += sample.eq(self.uart.source.payload.d)

		# FM transmitter settings
		transmit_freq = ??	# carrier wave frequency in Hz
		phaseacc_nbits = ??	# counter width
		
		## your code here
		# some of the magic also happens here


if __name__ == "__main__":
	platform = papilio_pro.Platform()
	platform.add_extension(_transmitter_io)
	antenna = platform.request("antenna")
	serial = platform.request("serial")
	top = FMTransmitter(antenna, serial)
	platform.build_cmdline(top)
