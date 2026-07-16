# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingMethod2Code
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Number

class ClearingBatchData3(base_types._BaseFieldType):

	__slots__ = ["_AgtFeeAmt", "_AgtFeeCcy", "_AgtFeeCdtDbt", "_Dt", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_IntrchngFeeCdtDbt", "_Mtd", "_OthrMtd", "_Prty", "_TtlsAmt", "_TtlsCcy", "_TtlsCdtDbt", "_TtlsCnt"]
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
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

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
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', ClearingMethod2Code, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', ClearingMethod2Code, False)

	@property
	def OthrMtd(self):
		return self._OthrMtd

	@OthrMtd.setter
	def OthrMtd(self, value):
		self._OthrMtd = value if value is not None else base_types.UninitialisedField(self, 'OthrMtd', Max35Text, False)

	@OthrMtd.deleter
	def OthrMtd(self):
		del self._OthrMtd
		self._OthrMtd = base_types.UninitialisedField(self, 'OthrMtd', Max35Text, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Max35Text, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Max35Text, False)

	@property
	def TtlsAmt(self):
		return self._TtlsAmt

	@TtlsAmt.setter
	def TtlsAmt(self, value):
		self._TtlsAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlsAmt', ImpliedCurrencyAndAmount, False)

	@TtlsAmt.deleter
	def TtlsAmt(self):
		del self._TtlsAmt
		self._TtlsAmt = base_types.UninitialisedField(self, 'TtlsAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TtlsCcy(self):
		return self._TtlsCcy

	@TtlsCcy.setter
	def TtlsCcy(self, value):
		self._TtlsCcy = value if value is not None else base_types.UninitialisedField(self, 'TtlsCcy', ISO3NumericCurrencyCode, False)

	@TtlsCcy.deleter
	def TtlsCcy(self):
		del self._TtlsCcy
		self._TtlsCcy = base_types.UninitialisedField(self, 'TtlsCcy', ISO3NumericCurrencyCode, False)

	@property
	def TtlsCdtDbt(self):
		return self._TtlsCdtDbt

	@TtlsCdtDbt.setter
	def TtlsCdtDbt(self, value):
		self._TtlsCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'TtlsCdtDbt', CreditDebit3Code, False)

	@TtlsCdtDbt.deleter
	def TtlsCdtDbt(self):
		del self._TtlsCdtDbt
		self._TtlsCdtDbt = base_types.UninitialisedField(self, 'TtlsCdtDbt', CreditDebit3Code, False)

	@property
	def TtlsCnt(self):
		return self._TtlsCnt

	@TtlsCnt.setter
	def TtlsCnt(self, value):
		self._TtlsCnt = value if value is not None else base_types.UninitialisedField(self, 'TtlsCnt', Number, False)

	@TtlsCnt.deleter
	def TtlsCnt(self):
		del self._TtlsCnt
		self._TtlsCnt = base_types.UninitialisedField(self, 'TtlsCnt', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=ClearingMethod2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsCnt', type=Number, min=0, max=1, mutex_group=None, array=False),
	))