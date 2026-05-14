# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClearingMethod2Code import ClearingMethod2Code
from ._CreditDebit3Code import CreditDebit3Code
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ISODate import ISODate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Number import Number

class ClearingBatchData3(base_types._BaseFieldType):

	__slots__ = ["_AgtFeeAmt", "_AgtFeeCcy", "_AgtFeeCdtDbt", "_Dt", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_IntrchngFeeCdtDbt", "_Mtd", "_OthrMtd", "_Prty", "_TtlsAmt", "_TtlsCcy", "_TtlsCdtDbt", "_TtlsCnt"]
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
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

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
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != base_types.auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def OthrMtd(self):
		return self._OthrMtd

	@OthrMtd.setter
	def OthrMtd(self, value):
		self._OthrMtd = value if type(value) != base_types.auto else self.make_default("OthrMtd")

	@OthrMtd.deleter
	def OthrMtd(self):
		del self._OthrMtd
		self._OthrMtd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def TtlsAmt(self):
		return self._TtlsAmt

	@TtlsAmt.setter
	def TtlsAmt(self, value):
		self._TtlsAmt = value if type(value) != base_types.auto else self.make_default("TtlsAmt")

	@TtlsAmt.deleter
	def TtlsAmt(self):
		del self._TtlsAmt
		self._TtlsAmt = None

	@property
	def TtlsCcy(self):
		return self._TtlsCcy

	@TtlsCcy.setter
	def TtlsCcy(self, value):
		self._TtlsCcy = value if type(value) != base_types.auto else self.make_default("TtlsCcy")

	@TtlsCcy.deleter
	def TtlsCcy(self):
		del self._TtlsCcy
		self._TtlsCcy = None

	@property
	def TtlsCdtDbt(self):
		return self._TtlsCdtDbt

	@TtlsCdtDbt.setter
	def TtlsCdtDbt(self, value):
		self._TtlsCdtDbt = value if type(value) != base_types.auto else self.make_default("TtlsCdtDbt")

	@TtlsCdtDbt.deleter
	def TtlsCdtDbt(self):
		del self._TtlsCdtDbt
		self._TtlsCdtDbt = None

	@property
	def TtlsCnt(self):
		return self._TtlsCnt

	@TtlsCnt.setter
	def TtlsCnt(self, value):
		self._TtlsCnt = value if type(value) != base_types.auto else self.make_default("TtlsCnt")

	@TtlsCnt.deleter
	def TtlsCnt(self):
		del self._TtlsCnt
		self._TtlsCnt = None

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