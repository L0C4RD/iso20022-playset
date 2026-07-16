# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import PriceValueAndRate4
from . import TypeOfPrice27Choice

class PriceInformation10(base_types._BaseFieldType):

	__slots__ = ["_AmtOfChng", "_CurPric", "_PrvsPric", "_Tp"]
	@property
	def AmtOfChng(self):
		return self._AmtOfChng

	@AmtOfChng.setter
	def AmtOfChng(self, value):
		self._AmtOfChng = value if value is not None else base_types.UninitialisedField(self, 'AmtOfChng', PriceValueAndRate4, False)

	@AmtOfChng.deleter
	def AmtOfChng(self):
		del self._AmtOfChng
		self._AmtOfChng = base_types.UninitialisedField(self, 'AmtOfChng', PriceValueAndRate4, False)

	@property
	def CurPric(self):
		return self._CurPric

	@CurPric.setter
	def CurPric(self, value):
		self._CurPric = value if value is not None else base_types.UninitialisedField(self, 'CurPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@CurPric.deleter
	def CurPric(self):
		del self._CurPric
		self._CurPric = base_types.UninitialisedField(self, 'CurPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def PrvsPric(self):
		return self._PrvsPric

	@PrvsPric.setter
	def PrvsPric(self, value):
		self._PrvsPric = value if value is not None else base_types.UninitialisedField(self, 'PrvsPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@PrvsPric.deleter
	def PrvsPric(self):
		del self._PrvsPric
		self._PrvsPric = base_types.UninitialisedField(self, 'PrvsPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfPrice27Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfPrice27Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOfChng', type=PriceValueAndRate4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice27Choice, min=1, max=1, mutex_group=None, array=False),
	))