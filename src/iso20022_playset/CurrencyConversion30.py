import base_types
import CurrencyConversion29
import TrueFalseIndicator

class CurrencyConversion30(base_types._BaseFieldType):

	__slots__ = ["_Convs", "_AccptdByCrdhldr"]
	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	@property
	def AccptdByCrdhldr(self):
		return self._AccptdByCrdhldr

	@AccptdByCrdhldr.setter
	def AccptdByCrdhldr(self, value):
		self._AccptdByCrdhldr = value if type(value) != auto else self.make_default("AccptdByCrdhldr")

	@AccptdByCrdhldr.deleter
	def AccptdByCrdhldr(self):
		del self._AccptdByCrdhldr
		self._AccptdByCrdhldr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Convs', type=CurrencyConversion29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdByCrdhldr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

