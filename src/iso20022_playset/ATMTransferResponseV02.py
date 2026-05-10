from . import base_types
from .ATMTransferResponse2 import ATMTransferResponse2
from .ContentInformationType10 import ContentInformationType10
from .ContentInformationType15 import ContentInformationType15
from .Header31 import Header31

class ATMTransferResponseV02(base_types._BaseFieldType):

	__slots__ = ["_ATMTrfRspn", "_PrtctdATMTrfRspn", "_Hdr", "_SctyTrlr"]
	@property
	def ATMTrfRspn(self):
		return self._ATMTrfRspn

	@ATMTrfRspn.setter
	def ATMTrfRspn(self, value):
		self._ATMTrfRspn = value if type(value) != auto else self.make_default("ATMTrfRspn")

	@ATMTrfRspn.deleter
	def ATMTrfRspn(self):
		del self._ATMTrfRspn
		self._ATMTrfRspn = None

	@property
	def PrtctdATMTrfRspn(self):
		return self._PrtctdATMTrfRspn

	@PrtctdATMTrfRspn.setter
	def PrtctdATMTrfRspn(self, value):
		self._PrtctdATMTrfRspn = value if type(value) != auto else self.make_default("PrtctdATMTrfRspn")

	@PrtctdATMTrfRspn.deleter
	def PrtctdATMTrfRspn(self):
		del self._PrtctdATMTrfRspn
		self._PrtctdATMTrfRspn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMTrfRspn', type=ATMTransferResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMTrfRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

