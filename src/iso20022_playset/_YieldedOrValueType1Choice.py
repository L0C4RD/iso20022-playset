from . import base_types
from ._PriceValueType1Code import PriceValueType1Code
from ._YesNoIndicator import YesNoIndicator

class YieldedOrValueType1Choice(base_types._BaseFieldType):

	__slots__ = ["_ValTp", "_Yldd"]
	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if type(value) != base_types.auto else self.make_default("ValTp")

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = None

	@property
	def Yldd(self):
		return self._Yldd

	@Yldd.setter
	def Yldd(self, value):
		self._Yldd = value if type(value) != base_types.auto else self.make_default("Yldd")

	@Yldd.deleter
	def Yldd(self):
		del self._Yldd
		self._Yldd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValTp', type=PriceValueType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yldd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))

