from . import base_types
from ._Max140Text import Max140Text
from ._StructuredRemittanceInformation16 import StructuredRemittanceInformation16
from ._RemittanceLocation7 import RemittanceLocation7

class Remittance1(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_Rltd", "_Ustrd"]
	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if type(value) != base_types.auto else self.make_default("Strd")

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = None

	@property
	def Rltd(self):
		return self._Rltd

	@Rltd.setter
	def Rltd(self, value):
		self._Rltd = value if type(value) != base_types.auto else self.make_default("Rltd")

	@Rltd.deleter
	def Rltd(self):
		del self._Rltd
		self._Rltd = None

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if type(value) != base_types.auto else self.make_default("Ustrd")

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strd', type=StructuredRemittanceInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rltd', type=RemittanceLocation7, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))

