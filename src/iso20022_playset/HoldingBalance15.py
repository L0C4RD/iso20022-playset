from . import base_types
from .SignedQuantityFormat15 import SignedQuantityFormat15
from .SecuritiesEntryType2Code import SecuritiesEntryType2Code
from .SafekeepingPlaceFormat42Choice import SafekeepingPlaceFormat42Choice

class HoldingBalance15(base_types._BaseFieldType):

	__slots__ = ["_BalTp", "_SfkpgPlc", "_Bal"]
	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTp', type=SecuritiesEntryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat15, min=1, max=1, mutex_group=None, array=False),
	))

