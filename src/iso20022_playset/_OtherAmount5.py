# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Number

class OtherAmount5(base_types._BaseFieldType):

	__slots__ = ["_AgtFeeAmt", "_AgtFeeCcy", "_AgtFeeCdtDbt", "_ClrAmt", "_ClrCcy", "_ClrCdtDbt", "_ClrCnt", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_IntrchngFeeCdtDbt"]
	@property
	def AgtFeeAmt(self):
		return self._AgtFeeAmt

	@AgtFeeAmt.setter
	def AgtFeeAmt(self, value):
		self._AgtFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeAmt', ImpliedCurrencyAndAmount, False)

	@AgtFeeAmt.deleter
	def AgtFeeAmt(self):
		del self._AgtFeeAmt
		self._AgtFeeAmt = base_types.UninitialisedField(self, 'AgtFeeAmt', ImpliedCurrencyAndAmount, False)

	@property
	def AgtFeeCcy(self):
		return self._AgtFeeCcy

	@AgtFeeCcy.setter
	def AgtFeeCcy(self, value):
		self._AgtFeeCcy = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeCcy', ISO3NumericCurrencyCode, False)

	@AgtFeeCcy.deleter
	def AgtFeeCcy(self):
		del self._AgtFeeCcy
		self._AgtFeeCcy = base_types.UninitialisedField(self, 'AgtFeeCcy', ISO3NumericCurrencyCode, False)

	@property
	def AgtFeeCdtDbt(self):
		return self._AgtFeeCdtDbt

	@AgtFeeCdtDbt.setter
	def AgtFeeCdtDbt(self, value):
		self._AgtFeeCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeCdtDbt', CreditDebit3Code, False)

	@AgtFeeCdtDbt.deleter
	def AgtFeeCdtDbt(self):
		del self._AgtFeeCdtDbt
		self._AgtFeeCdtDbt = base_types.UninitialisedField(self, 'AgtFeeCdtDbt', CreditDebit3Code, False)

	@property
	def ClrAmt(self):
		return self._ClrAmt

	@ClrAmt.setter
	def ClrAmt(self, value):
		self._ClrAmt = value if value is not None else base_types.UninitialisedField(self, 'ClrAmt', ImpliedCurrencyAndAmount, False)

	@ClrAmt.deleter
	def ClrAmt(self):
		del self._ClrAmt
		self._ClrAmt = base_types.UninitialisedField(self, 'ClrAmt', ImpliedCurrencyAndAmount, False)

	@property
	def ClrCcy(self):
		return self._ClrCcy

	@ClrCcy.setter
	def ClrCcy(self, value):
		self._ClrCcy = value if value is not None else base_types.UninitialisedField(self, 'ClrCcy', ISO3NumericCurrencyCode, False)

	@ClrCcy.deleter
	def ClrCcy(self):
		del self._ClrCcy
		self._ClrCcy = base_types.UninitialisedField(self, 'ClrCcy', ISO3NumericCurrencyCode, False)

	@property
	def ClrCdtDbt(self):
		return self._ClrCdtDbt

	@ClrCdtDbt.setter
	def ClrCdtDbt(self, value):
		self._ClrCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'ClrCdtDbt', CreditDebit3Code, False)

	@ClrCdtDbt.deleter
	def ClrCdtDbt(self):
		del self._ClrCdtDbt
		self._ClrCdtDbt = base_types.UninitialisedField(self, 'ClrCdtDbt', CreditDebit3Code, False)

	@property
	def ClrCnt(self):
		return self._ClrCnt

	@ClrCnt.setter
	def ClrCnt(self, value):
		self._ClrCnt = value if value is not None else base_types.UninitialisedField(self, 'ClrCnt', Number, False)

	@ClrCnt.deleter
	def ClrCnt(self):
		del self._ClrCnt
		self._ClrCnt = base_types.UninitialisedField(self, 'ClrCnt', Number, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtFeeAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCnt', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
	))