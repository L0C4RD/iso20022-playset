from . import base_types
from ._ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from ._PriceValueAndRate4 import PriceValueAndRate4
from ._TypeOfPrice27Choice import TypeOfPrice27Choice

class PriceInformation10(base_types._BaseFieldType):

	__slots__ = ["_AmtOfChng", "_CurPric", "_PrvsPric", "_Tp"]
	@property
	def AmtOfChng(self):
		return self._AmtOfChng

	@AmtOfChng.setter
	def AmtOfChng(self, value):
		self._AmtOfChng = value if type(value) != base_types.auto else self.make_default("AmtOfChng")

	@AmtOfChng.deleter
	def AmtOfChng(self):
		del self._AmtOfChng
		self._AmtOfChng = None

	@property
	def CurPric(self):
		return self._CurPric

	@CurPric.setter
	def CurPric(self, value):
		self._CurPric = value if type(value) != base_types.auto else self.make_default("CurPric")

	@CurPric.deleter
	def CurPric(self):
		del self._CurPric
		self._CurPric = None

	@property
	def PrvsPric(self):
		return self._PrvsPric

	@PrvsPric.setter
	def PrvsPric(self, value):
		self._PrvsPric = value if type(value) != base_types.auto else self.make_default("PrvsPric")

	@PrvsPric.deleter
	def PrvsPric(self):
		del self._PrvsPric
		self._PrvsPric = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOfChng', type=PriceValueAndRate4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice27Choice, min=1, max=1, mutex_group=None, array=False),
	))

