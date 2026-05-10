from . import base_types
from ._SafekeepingPlaceFormat42Choice import SafekeepingPlaceFormat42Choice
from ._ISODate import ISODate
from ._SignedQuantityFormat14 import SignedQuantityFormat14
from ._SecuritiesEntryType2Code import SecuritiesEntryType2Code

class HoldingBalance14(base_types._BaseFieldType):

	__slots__ = ["_BalTp", "_Bal", "_SfkpgPlc", "_Dt"]
	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != base_types.auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTp', type=SecuritiesEntryType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

