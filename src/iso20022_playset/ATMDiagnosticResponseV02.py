from . import base_types
from .Header31 import Header31
from .ContentInformationType15 import ContentInformationType15
from .ContentInformationType10 import ContentInformationType10
from .ATMDiagnosticResponse2 import ATMDiagnosticResponse2

class ATMDiagnosticResponseV02(base_types._BaseFieldType):

	__slots__ = ["_ATMDgnstcRspn", "_SctyTrlr", "_Hdr", "_PrtctdATMDgnstcRspn"]
	@property
	def ATMDgnstcRspn(self):
		return self._ATMDgnstcRspn

	@ATMDgnstcRspn.setter
	def ATMDgnstcRspn(self, value):
		self._ATMDgnstcRspn = value if type(value) != base_types.auto else self.make_default("ATMDgnstcRspn")

	@ATMDgnstcRspn.deleter
	def ATMDgnstcRspn(self):
		del self._ATMDgnstcRspn
		self._ATMDgnstcRspn = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def PrtctdATMDgnstcRspn(self):
		return self._PrtctdATMDgnstcRspn

	@PrtctdATMDgnstcRspn.setter
	def PrtctdATMDgnstcRspn(self, value):
		self._PrtctdATMDgnstcRspn = value if type(value) != base_types.auto else self.make_default("PrtctdATMDgnstcRspn")

	@PrtctdATMDgnstcRspn.deleter
	def PrtctdATMDgnstcRspn(self):
		del self._PrtctdATMDgnstcRspn
		self._PrtctdATMDgnstcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMDgnstcRspn', type=ATMDiagnosticResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMDgnstcRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

