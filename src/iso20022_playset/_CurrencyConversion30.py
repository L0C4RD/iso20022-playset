from . import base_types
from ._CurrencyConversion29 import CurrencyConversion29
from ._TrueFalseIndicator import TrueFalseIndicator

class CurrencyConversion30(base_types._BaseFieldType):

	__slots__ = ["_AccptdByCrdhldr", "_Convs"]
	@property
	def AccptdByCrdhldr(self):
		return self._AccptdByCrdhldr

	@AccptdByCrdhldr.setter
	def AccptdByCrdhldr(self, value):
		self._AccptdByCrdhldr = value if type(value) != base_types.auto else self.make_default("AccptdByCrdhldr")

	@AccptdByCrdhldr.deleter
	def AccptdByCrdhldr(self):
		del self._AccptdByCrdhldr
		self._AccptdByCrdhldr = None

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != base_types.auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdByCrdhldr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=CurrencyConversion29, min=0, max=1, mutex_group=None, array=False),
	))

