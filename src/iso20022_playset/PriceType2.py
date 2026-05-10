from . import base_types
from .Max350Text import Max350Text
from .TypeOfPrice6Code import TypeOfPrice6Code

class PriceType2(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_AddtlInf"]
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
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strd', type=TypeOfPrice6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

