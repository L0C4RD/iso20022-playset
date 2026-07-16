# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ISO8583AmountTypeCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import TrueFalseIndicator

class CardAccountBalance1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_BalDt", "_Ccy", "_CdtDbt", "_CrdhldrCcy", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def BalDt(self):
		return self._BalDt

	@BalDt.setter
	def BalDt(self, value):
		self._BalDt = value if value is not None else base_types.UninitialisedField(self, 'BalDt', ISODate, False)

	@BalDt.deleter
	def BalDt(self):
		del self._BalDt
		self._BalDt = base_types.UninitialisedField(self, 'BalDt', ISODate, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def CrdhldrCcy(self):
		return self._CrdhldrCcy

	@CrdhldrCcy.setter
	def CrdhldrCcy(self, value):
		self._CrdhldrCcy = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrCcy', TrueFalseIndicator, False)

	@CrdhldrCcy.deleter
	def CrdhldrCcy(self):
		del self._CrdhldrCcy
		self._CrdhldrCcy = base_types.UninitialisedField(self, 'CrdhldrCcy', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ISO8583AmountTypeCode, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ISO8583AmountTypeCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrCcy', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ISO8583AmountTypeCode, min=1, max=1, mutex_group=None, array=False),
	))