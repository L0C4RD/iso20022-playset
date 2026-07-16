# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AmountUnit1Code
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import Max1025Text
from . import Max35Text
from . import TrueFalseIndicator

class CustomerOrder1(base_types._BaseFieldType):

	__slots__ = ["_AccsdBy", "_AddtlInf", "_Ccy", "_CstmrOrdrId", "_CurAmt", "_EndDt", "_FrcstdAmt", "_OpnOrdrStat", "_SaleRefId", "_StartDt", "_Unit"]
	@property
	def AccsdBy(self):
		return self._AccsdBy

	@AccsdBy.setter
	def AccsdBy(self, value):
		self._AccsdBy = value if value is not None else base_types.UninitialisedField(self, 'AccsdBy', Max35Text, False)

	@AccsdBy.deleter
	def AccsdBy(self):
		del self._AccsdBy
		self._AccsdBy = base_types.UninitialisedField(self, 'AccsdBy', Max35Text, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CstmrOrdrId(self):
		return self._CstmrOrdrId

	@CstmrOrdrId.setter
	def CstmrOrdrId(self, value):
		self._CstmrOrdrId = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdrId', Max35Text, False)

	@CstmrOrdrId.deleter
	def CstmrOrdrId(self):
		del self._CstmrOrdrId
		self._CstmrOrdrId = base_types.UninitialisedField(self, 'CstmrOrdrId', Max35Text, False)

	@property
	def CurAmt(self):
		return self._CurAmt

	@CurAmt.setter
	def CurAmt(self, value):
		self._CurAmt = value if value is not None else base_types.UninitialisedField(self, 'CurAmt', ImpliedCurrencyAndAmount, False)

	@CurAmt.deleter
	def CurAmt(self):
		del self._CurAmt
		self._CurAmt = base_types.UninitialisedField(self, 'CurAmt', ImpliedCurrencyAndAmount, False)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODateTime, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODateTime, False)

	@property
	def FrcstdAmt(self):
		return self._FrcstdAmt

	@FrcstdAmt.setter
	def FrcstdAmt(self, value):
		self._FrcstdAmt = value if value is not None else base_types.UninitialisedField(self, 'FrcstdAmt', ImpliedCurrencyAndAmount, False)

	@FrcstdAmt.deleter
	def FrcstdAmt(self):
		del self._FrcstdAmt
		self._FrcstdAmt = base_types.UninitialisedField(self, 'FrcstdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def OpnOrdrStat(self):
		return self._OpnOrdrStat

	@OpnOrdrStat.setter
	def OpnOrdrStat(self, value):
		self._OpnOrdrStat = value if value is not None else base_types.UninitialisedField(self, 'OpnOrdrStat', TrueFalseIndicator, False)

	@OpnOrdrStat.deleter
	def OpnOrdrStat(self):
		del self._OpnOrdrStat
		self._OpnOrdrStat = base_types.UninitialisedField(self, 'OpnOrdrStat', TrueFalseIndicator, False)

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if value is not None else base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODateTime, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODateTime, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', AmountUnit1Code, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', AmountUnit1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccsdBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrcstdAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnOrdrStat', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=AmountUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))