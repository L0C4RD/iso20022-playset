# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData1 import AdditionalData1
from ._CreditDebit3Code import CreditDebit3Code
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LodgingService1Code import LodgingService1Code
from ._Max35Text import Max35Text
from ._Max4NumericText import Max4NumericText
from ._Tax41 import Tax41
from ._TrueFalseIndicator import TrueFalseIndicator

class LodgingLineItem3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_CdtDbt", "_Drtn", "_Dt", "_OthrTp", "_PstChckOut", "_SubTtlAmt", "_Tax", "_Tm", "_Tp", "_UnitAmt"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	@property
	def PstChckOut(self):
		return self._PstChckOut

	@PstChckOut.setter
	def PstChckOut(self, value):
		self._PstChckOut = value if type(value) != base_types.auto else self.make_default("PstChckOut")

	@PstChckOut.deleter
	def PstChckOut(self):
		del self._PstChckOut
		self._PstChckOut = None

	@property
	def SubTtlAmt(self):
		return self._SubTtlAmt

	@SubTtlAmt.setter
	def SubTtlAmt(self, value):
		self._SubTtlAmt = value if type(value) != base_types.auto else self.make_default("SubTtlAmt")

	@SubTtlAmt.deleter
	def SubTtlAmt(self):
		del self._SubTtlAmt
		self._SubTtlAmt = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def UnitAmt(self):
		return self._UnitAmt

	@UnitAmt.setter
	def UnitAmt(self, value):
		self._UnitAmt = value if type(value) != base_types.auto else self.make_default("UnitAmt")

	@UnitAmt.deleter
	def UnitAmt(self):
		del self._UnitAmt
		self._UnitAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstChckOut', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LodgingService1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))