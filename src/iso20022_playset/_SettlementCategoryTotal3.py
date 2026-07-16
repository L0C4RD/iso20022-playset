# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Number

class SettlementCategoryTotal3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_CdtDbt", "_Cnt", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_IntrchngFeeCdtDbt", "_PrcgFeeAmt", "_PrcgFeeCcy", "_PrcgFeeCdtDbt"]
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
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if value is not None else base_types.UninitialisedField(self, 'Cnt', Number, False)

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = base_types.UninitialisedField(self, 'Cnt', Number, False)

	@property
	def IntrchngFeeAmt(self):
		return self._IntrchngFeeAmt

	@IntrchngFeeAmt.setter
	def IntrchngFeeAmt(self, value):
		self._IntrchngFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeAmt', ImpliedCurrencyAndAmount, False)

	@IntrchngFeeAmt.deleter
	def IntrchngFeeAmt(self):
		del self._IntrchngFeeAmt
		self._IntrchngFeeAmt = base_types.UninitialisedField(self, 'IntrchngFeeAmt', ImpliedCurrencyAndAmount, False)

	@property
	def IntrchngFeeCcy(self):
		return self._IntrchngFeeCcy

	@IntrchngFeeCcy.setter
	def IntrchngFeeCcy(self, value):
		self._IntrchngFeeCcy = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeCcy', ISO3NumericCurrencyCode, False)

	@IntrchngFeeCcy.deleter
	def IntrchngFeeCcy(self):
		del self._IntrchngFeeCcy
		self._IntrchngFeeCcy = base_types.UninitialisedField(self, 'IntrchngFeeCcy', ISO3NumericCurrencyCode, False)

	@property
	def IntrchngFeeCdtDbt(self):
		return self._IntrchngFeeCdtDbt

	@IntrchngFeeCdtDbt.setter
	def IntrchngFeeCdtDbt(self, value):
		self._IntrchngFeeCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeCdtDbt', CreditDebit3Code, False)

	@IntrchngFeeCdtDbt.deleter
	def IntrchngFeeCdtDbt(self):
		del self._IntrchngFeeCdtDbt
		self._IntrchngFeeCdtDbt = base_types.UninitialisedField(self, 'IntrchngFeeCdtDbt', CreditDebit3Code, False)

	@property
	def PrcgFeeAmt(self):
		return self._PrcgFeeAmt

	@PrcgFeeAmt.setter
	def PrcgFeeAmt(self, value):
		self._PrcgFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'PrcgFeeAmt', ImpliedCurrencyAndAmount, False)

	@PrcgFeeAmt.deleter
	def PrcgFeeAmt(self):
		del self._PrcgFeeAmt
		self._PrcgFeeAmt = base_types.UninitialisedField(self, 'PrcgFeeAmt', ImpliedCurrencyAndAmount, False)

	@property
	def PrcgFeeCcy(self):
		return self._PrcgFeeCcy

	@PrcgFeeCcy.setter
	def PrcgFeeCcy(self, value):
		self._PrcgFeeCcy = value if value is not None else base_types.UninitialisedField(self, 'PrcgFeeCcy', ISO3NumericCurrencyCode, False)

	@PrcgFeeCcy.deleter
	def PrcgFeeCcy(self):
		del self._PrcgFeeCcy
		self._PrcgFeeCcy = base_types.UninitialisedField(self, 'PrcgFeeCcy', ISO3NumericCurrencyCode, False)

	@property
	def PrcgFeeCdtDbt(self):
		return self._PrcgFeeCdtDbt

	@PrcgFeeCdtDbt.setter
	def PrcgFeeCdtDbt(self, value):
		self._PrcgFeeCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'PrcgFeeCdtDbt', CreditDebit3Code, False)

	@PrcgFeeCdtDbt.deleter
	def PrcgFeeCdtDbt(self):
		del self._PrcgFeeCdtDbt
		self._PrcgFeeCdtDbt = base_types.UninitialisedField(self, 'PrcgFeeCdtDbt', CreditDebit3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
	))