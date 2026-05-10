from . import base_types
from ._Max35Text import Max35Text
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class HypotheticalCapitalMeasure1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DfltWtrfllId"]
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
	def DfltWtrfllId(self):
		return self._DfltWtrfllId

	@DfltWtrfllId.setter
	def DfltWtrfllId(self, value):
		self._DfltWtrfllId = value if type(value) != base_types.auto else self.make_default("DfltWtrfllId")

	@DfltWtrfllId.deleter
	def DfltWtrfllId(self):
		del self._DfltWtrfllId
		self._DfltWtrfllId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltWtrfllId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

