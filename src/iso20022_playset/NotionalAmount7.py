from . import base_types
import LongFraction19DecimalNumber
import ActiveOrHistoricCurrencyAnd19DecimalAmount

class NotionalAmount7(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_WghtdAvrgDlta", "_AmtInFct"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def WghtdAvrgDlta(self):
		return self._WghtdAvrgDlta

	@WghtdAvrgDlta.setter
	def WghtdAvrgDlta(self, value):
		self._WghtdAvrgDlta = value if type(value) != auto else self.make_default("WghtdAvrgDlta")

	@WghtdAvrgDlta.deleter
	def WghtdAvrgDlta(self):
		del self._WghtdAvrgDlta
		self._WghtdAvrgDlta = None

	@property
	def AmtInFct(self):
		return self._AmtInFct

	@AmtInFct.setter
	def AmtInFct(self, value):
		self._AmtInFct = value if type(value) != auto else self.make_default("AmtInFct")

	@AmtInFct.deleter
	def AmtInFct(self):
		del self._AmtInFct
		self._AmtInFct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgDlta', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtInFct', type=ActiveOrHistoricCurrencyAnd19DecimalAmount, min=0, max=None, mutex_group=None, array=True),
	))

