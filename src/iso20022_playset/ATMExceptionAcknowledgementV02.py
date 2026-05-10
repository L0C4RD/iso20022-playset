from . import base_types
from .ATMExceptionAcknowledgement2 import ATMExceptionAcknowledgement2
from .ContentInformationType10 import ContentInformationType10
from .ContentInformationType15 import ContentInformationType15
from .Header32 import Header32

class ATMExceptionAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_PrtctdATMXcptnAck", "_Hdr", "_SctyTrlr", "_ATMXcptnAck"]
	@property
	def PrtctdATMXcptnAck(self):
		return self._PrtctdATMXcptnAck

	@PrtctdATMXcptnAck.setter
	def PrtctdATMXcptnAck(self, value):
		self._PrtctdATMXcptnAck = value if type(value) != auto else self.make_default("PrtctdATMXcptnAck")

	@PrtctdATMXcptnAck.deleter
	def PrtctdATMXcptnAck(self):
		del self._PrtctdATMXcptnAck
		self._PrtctdATMXcptnAck = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def ATMXcptnAck(self):
		return self._ATMXcptnAck

	@ATMXcptnAck.setter
	def ATMXcptnAck(self, value):
		self._ATMXcptnAck = value if type(value) != auto else self.make_default("ATMXcptnAck")

	@ATMXcptnAck.deleter
	def ATMXcptnAck(self):
		del self._ATMXcptnAck
		self._ATMXcptnAck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdATMXcptnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMXcptnAck', type=ATMExceptionAcknowledgement2, min=0, max=1, mutex_group=None, array=False),
	))

