from . import base_types
from ._AmountPrice1 import AmountPrice1
from ._PriceValueType5FormatChoice import PriceValueType5FormatChoice
from ._PriceRate1 import PriceRate1

class PriceFormat2Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Rate", "_NotSpcfd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def NotSpcfd(self):
		return self._NotSpcfd

	@NotSpcfd.setter
	def NotSpcfd(self, value):
		self._NotSpcfd = value if type(value) != base_types.auto else self.make_default("NotSpcfd")

	@NotSpcfd.deleter
	def NotSpcfd(self):
		del self._NotSpcfd
		self._NotSpcfd = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountPrice1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfd', type=PriceValueType5FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PriceRate1, min=0, max=1, mutex_group=1, array=False),
	))

