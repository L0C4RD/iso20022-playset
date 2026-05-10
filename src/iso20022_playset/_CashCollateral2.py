from . import base_types
from ._ISODate import ISODate
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._BaseOneRate import BaseOneRate
from ._YesNoIndicator import YesNoIndicator
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._PercentageRate import PercentageRate
from ._Max35Text import Max35Text
from ._DepositType1Code import DepositType1Code

class CashCollateral2(base_types._BaseFieldType):

	__slots__ = ["_CollVal", "_ValDt", "_Hrcut", "_CshAcctId", "_CollId", "_DpstTp", "_MtrtyDt", "_DpstAmt", "_XchgRate", "_RtrXcss"]
	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if type(value) != base_types.auto else self.make_default("CollId")

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = None

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if type(value) != base_types.auto else self.make_default("CollVal")

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = None

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if type(value) != base_types.auto else self.make_default("CshAcctId")

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = None

	@property
	def DpstAmt(self):
		return self._DpstAmt

	@DpstAmt.setter
	def DpstAmt(self, value):
		self._DpstAmt = value if type(value) != base_types.auto else self.make_default("DpstAmt")

	@DpstAmt.deleter
	def DpstAmt(self):
		del self._DpstAmt
		self._DpstAmt = None

	@property
	def DpstTp(self):
		return self._DpstTp

	@DpstTp.setter
	def DpstTp(self, value):
		self._DpstTp = value if type(value) != base_types.auto else self.make_default("DpstTp")

	@DpstTp.deleter
	def DpstTp(self):
		del self._DpstTp
		self._DpstTp = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != base_types.auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def RtrXcss(self):
		return self._RtrXcss

	@RtrXcss.setter
	def RtrXcss(self, value):
		self._RtrXcss = value if type(value) != base_types.auto else self.make_default("RtrXcss")

	@RtrXcss.deleter
	def RtrXcss(self):
		del self._RtrXcss
		self._RtrXcss = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstTp', type=DepositType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrXcss', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

