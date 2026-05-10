import base_types
import ISODateTime
import Max35Text
import Max1025Text
import ImpliedCurrencyAndAmount
import AmountUnit1Code
import ActiveCurrencyCode
import TrueFalseIndicator

class CustomerOrder1(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_OpnOrdrStat", "_AddtlInf", "_Ccy", "_StartDt", "_FrcstdAmt", "_CurAmt", "_AccsdBy", "_CstmrOrdrId", "_SaleRefId", "_Unit"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def OpnOrdrStat(self):
		return self._OpnOrdrStat

	@OpnOrdrStat.setter
	def OpnOrdrStat(self, value):
		self._OpnOrdrStat = value if type(value) != auto else self.make_default("OpnOrdrStat")

	@OpnOrdrStat.deleter
	def OpnOrdrStat(self):
		del self._OpnOrdrStat
		self._OpnOrdrStat = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

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
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def FrcstdAmt(self):
		return self._FrcstdAmt

	@FrcstdAmt.setter
	def FrcstdAmt(self, value):
		self._FrcstdAmt = value if type(value) != auto else self.make_default("FrcstdAmt")

	@FrcstdAmt.deleter
	def FrcstdAmt(self):
		del self._FrcstdAmt
		self._FrcstdAmt = None

	@property
	def CurAmt(self):
		return self._CurAmt

	@CurAmt.setter
	def CurAmt(self, value):
		self._CurAmt = value if type(value) != auto else self.make_default("CurAmt")

	@CurAmt.deleter
	def CurAmt(self):
		del self._CurAmt
		self._CurAmt = None

	@property
	def AccsdBy(self):
		return self._AccsdBy

	@AccsdBy.setter
	def AccsdBy(self, value):
		self._AccsdBy = value if type(value) != auto else self.make_default("AccsdBy")

	@AccsdBy.deleter
	def AccsdBy(self):
		del self._AccsdBy
		self._AccsdBy = None

	@property
	def CstmrOrdrId(self):
		return self._CstmrOrdrId

	@CstmrOrdrId.setter
	def CstmrOrdrId(self, value):
		self._CstmrOrdrId = value if type(value) != auto else self.make_default("CstmrOrdrId")

	@CstmrOrdrId.deleter
	def CstmrOrdrId(self):
		del self._CstmrOrdrId
		self._CstmrOrdrId = None

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if type(value) != auto else self.make_default("SaleRefId")

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnOrdrStat', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrcstdAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccsdBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=AmountUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))

