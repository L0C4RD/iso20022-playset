from . import base_types
from ._ContentInformationType10 import ContentInformationType10
from ._Header31 import Header31
from ._ContentInformationType15 import ContentInformationType15
from ._ATMWithdrawalResponse3 import ATMWithdrawalResponse3

class ATMWithdrawalResponseV03(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_ATMWdrwlRspn", "_PrtctdATMWdrwlRspn"]
	@property
	def ATMWdrwlRspn(self):
		return self._ATMWdrwlRspn

	@ATMWdrwlRspn.setter
	def ATMWdrwlRspn(self, value):
		self._ATMWdrwlRspn = value if type(value) != base_types.auto else self.make_default("ATMWdrwlRspn")

	@ATMWdrwlRspn.deleter
	def ATMWdrwlRspn(self):
		del self._ATMWdrwlRspn
		self._ATMWdrwlRspn = None

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
	def PrtctdATMWdrwlRspn(self):
		return self._PrtctdATMWdrwlRspn

	@PrtctdATMWdrwlRspn.setter
	def PrtctdATMWdrwlRspn(self, value):
		self._PrtctdATMWdrwlRspn = value if type(value) != base_types.auto else self.make_default("PrtctdATMWdrwlRspn")

	@PrtctdATMWdrwlRspn.deleter
	def PrtctdATMWdrwlRspn(self):
		del self._PrtctdATMWdrwlRspn
		self._PrtctdATMWdrwlRspn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMWdrwlRspn', type=ATMWithdrawalResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header31, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMWdrwlRspn', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))

