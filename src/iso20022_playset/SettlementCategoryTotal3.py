import base_types
import ImpliedCurrencyAndAmount
import ISO3NumericCurrencyCode
import CreditDebit3Code
import Number

class SettlementCategoryTotal3(base_types._BaseFieldType):

	__slots__ = ["_CdtDbt", "_IntrchngFeeCdtDbt", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_Ccy", "_PrcgFeeCcy", "_PrcgFeeAmt", "_PrcgFeeCdtDbt", "_Cnt", "_Amt"]
	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def IntrchngFeeCdtDbt(self):
		return self._IntrchngFeeCdtDbt

	@IntrchngFeeCdtDbt.setter
	def IntrchngFeeCdtDbt(self, value):
		self._IntrchngFeeCdtDbt = value if type(value) != auto else self.make_default("IntrchngFeeCdtDbt")

	@IntrchngFeeCdtDbt.deleter
	def IntrchngFeeCdtDbt(self):
		del self._IntrchngFeeCdtDbt
		self._IntrchngFeeCdtDbt = None

	@property
	def IntrchngFeeAmt(self):
		return self._IntrchngFeeAmt

	@IntrchngFeeAmt.setter
	def IntrchngFeeAmt(self, value):
		self._IntrchngFeeAmt = value if type(value) != auto else self.make_default("IntrchngFeeAmt")

	@IntrchngFeeAmt.deleter
	def IntrchngFeeAmt(self):
		del self._IntrchngFeeAmt
		self._IntrchngFeeAmt = None

	@property
	def IntrchngFeeCcy(self):
		return self._IntrchngFeeCcy

	@IntrchngFeeCcy.setter
	def IntrchngFeeCcy(self, value):
		self._IntrchngFeeCcy = value if type(value) != auto else self.make_default("IntrchngFeeCcy")

	@IntrchngFeeCcy.deleter
	def IntrchngFeeCcy(self):
		del self._IntrchngFeeCcy
		self._IntrchngFeeCcy = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def PrcgFeeCcy(self):
		return self._PrcgFeeCcy

	@PrcgFeeCcy.setter
	def PrcgFeeCcy(self, value):
		self._PrcgFeeCcy = value if type(value) != auto else self.make_default("PrcgFeeCcy")

	@PrcgFeeCcy.deleter
	def PrcgFeeCcy(self):
		del self._PrcgFeeCcy
		self._PrcgFeeCcy = None

	@property
	def PrcgFeeAmt(self):
		return self._PrcgFeeAmt

	@PrcgFeeAmt.setter
	def PrcgFeeAmt(self, value):
		self._PrcgFeeAmt = value if type(value) != auto else self.make_default("PrcgFeeAmt")

	@PrcgFeeAmt.deleter
	def PrcgFeeAmt(self):
		del self._PrcgFeeAmt
		self._PrcgFeeAmt = None

	@property
	def PrcgFeeCdtDbt(self):
		return self._PrcgFeeCdtDbt

	@PrcgFeeCdtDbt.setter
	def PrcgFeeCdtDbt(self, value):
		self._PrcgFeeCdtDbt = value if type(value) != auto else self.make_default("PrcgFeeCdtDbt")

	@PrcgFeeCdtDbt.deleter
	def PrcgFeeCdtDbt(self):
		del self._PrcgFeeCdtDbt
		self._PrcgFeeCdtDbt = None

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if type(value) != auto else self.make_default("Cnt")

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

