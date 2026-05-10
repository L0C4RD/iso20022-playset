from . import base_types
from .Number import Number
from .ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .CreditDebit3Code import CreditDebit3Code

class OtherAmount5(base_types._BaseFieldType):

	__slots__ = ["_IntrchngFeeCcy", "_IntrchngFeeAmt", "_ClrCdtDbt", "_ClrCcy", "_ClrCnt", "_AgtFeeCcy", "_IntrchngFeeCdtDbt", "_AgtFeeAmt", "_AgtFeeCdtDbt", "_ClrAmt"]
	@property
	def IntrchngFeeCcy(self):
		return self._IntrchngFeeCcy

	@IntrchngFeeCcy.setter
	def IntrchngFeeCcy(self, value):
		self._IntrchngFeeCcy = value if type(value) != base_types.auto else self.make_default("IntrchngFeeCcy")

	@IntrchngFeeCcy.deleter
	def IntrchngFeeCcy(self):
		del self._IntrchngFeeCcy
		self._IntrchngFeeCcy = None

	@property
	def IntrchngFeeAmt(self):
		return self._IntrchngFeeAmt

	@IntrchngFeeAmt.setter
	def IntrchngFeeAmt(self, value):
		self._IntrchngFeeAmt = value if type(value) != base_types.auto else self.make_default("IntrchngFeeAmt")

	@IntrchngFeeAmt.deleter
	def IntrchngFeeAmt(self):
		del self._IntrchngFeeAmt
		self._IntrchngFeeAmt = None

	@property
	def ClrCdtDbt(self):
		return self._ClrCdtDbt

	@ClrCdtDbt.setter
	def ClrCdtDbt(self, value):
		self._ClrCdtDbt = value if type(value) != base_types.auto else self.make_default("ClrCdtDbt")

	@ClrCdtDbt.deleter
	def ClrCdtDbt(self):
		del self._ClrCdtDbt
		self._ClrCdtDbt = None

	@property
	def ClrCcy(self):
		return self._ClrCcy

	@ClrCcy.setter
	def ClrCcy(self, value):
		self._ClrCcy = value if type(value) != base_types.auto else self.make_default("ClrCcy")

	@ClrCcy.deleter
	def ClrCcy(self):
		del self._ClrCcy
		self._ClrCcy = None

	@property
	def ClrCnt(self):
		return self._ClrCnt

	@ClrCnt.setter
	def ClrCnt(self, value):
		self._ClrCnt = value if type(value) != base_types.auto else self.make_default("ClrCnt")

	@ClrCnt.deleter
	def ClrCnt(self):
		del self._ClrCnt
		self._ClrCnt = None

	@property
	def AgtFeeCcy(self):
		return self._AgtFeeCcy

	@AgtFeeCcy.setter
	def AgtFeeCcy(self, value):
		self._AgtFeeCcy = value if type(value) != base_types.auto else self.make_default("AgtFeeCcy")

	@AgtFeeCcy.deleter
	def AgtFeeCcy(self):
		del self._AgtFeeCcy
		self._AgtFeeCcy = None

	@property
	def IntrchngFeeCdtDbt(self):
		return self._IntrchngFeeCdtDbt

	@IntrchngFeeCdtDbt.setter
	def IntrchngFeeCdtDbt(self, value):
		self._IntrchngFeeCdtDbt = value if type(value) != base_types.auto else self.make_default("IntrchngFeeCdtDbt")

	@IntrchngFeeCdtDbt.deleter
	def IntrchngFeeCdtDbt(self):
		del self._IntrchngFeeCdtDbt
		self._IntrchngFeeCdtDbt = None

	@property
	def AgtFeeAmt(self):
		return self._AgtFeeAmt

	@AgtFeeAmt.setter
	def AgtFeeAmt(self, value):
		self._AgtFeeAmt = value if type(value) != base_types.auto else self.make_default("AgtFeeAmt")

	@AgtFeeAmt.deleter
	def AgtFeeAmt(self):
		del self._AgtFeeAmt
		self._AgtFeeAmt = None

	@property
	def AgtFeeCdtDbt(self):
		return self._AgtFeeCdtDbt

	@AgtFeeCdtDbt.setter
	def AgtFeeCdtDbt(self, value):
		self._AgtFeeCdtDbt = value if type(value) != base_types.auto else self.make_default("AgtFeeCdtDbt")

	@AgtFeeCdtDbt.deleter
	def AgtFeeCdtDbt(self):
		del self._AgtFeeCdtDbt
		self._AgtFeeCdtDbt = None

	@property
	def ClrAmt(self):
		return self._ClrAmt

	@ClrAmt.setter
	def ClrAmt(self, value):
		self._ClrAmt = value if type(value) != base_types.auto else self.make_default("ClrAmt")

	@ClrAmt.deleter
	def ClrAmt(self):
		del self._ClrAmt
		self._ClrAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCnt', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

