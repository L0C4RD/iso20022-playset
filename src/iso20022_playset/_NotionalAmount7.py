# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd19DecimalAmount
from . import LongFraction19DecimalNumber

class NotionalAmount7(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtInFct", "_WghtdAvrgDlta"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd19DecimalAmount, False)

	@property
	def AmtInFct(self):
		return self._AmtInFct

	@AmtInFct.setter
	def AmtInFct(self, value):
		self._AmtInFct = value if value is not None else base_types.UninitialisedField(self, 'AmtInFct', ActiveOrHistoricCurrencyAnd19DecimalAmount, True)

	@AmtInFct.deleter
	def AmtInFct(self):
		del self._AmtInFct
		self._AmtInFct = base_types.UninitialisedField(self, 'AmtInFct', ActiveOrHistoricCurrencyAnd19DecimalAmount, True)

	@property
	def WghtdAvrgDlta(self):
		return self._WghtdAvrgDlta

	@WghtdAvrgDlta.setter
	def WghtdAvrgDlta(self, value):
		self._WghtdAvrgDlta = value if value is not None else base_types.UninitialisedField(self, 'WghtdAvrgDlta', LongFraction19DecimalNumber, False)

	@WghtdAvrgDlta.deleter
	def WghtdAvrgDlta(self):
		del self._WghtdAvrgDlta
		self._WghtdAvrgDlta = base_types.UninitialisedField(self, 'WghtdAvrgDlta', LongFraction19DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtInFct', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WghtdAvrgDlta', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))