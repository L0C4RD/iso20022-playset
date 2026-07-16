# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyAndAmount
from . import BaseOneRate
from . import DepositType1Code
from . import ISODate
from . import Max35Text
from . import PercentageRate

class CashCollateral5(base_types._BaseFieldType):

	__slots__ = ["_AsstNb", "_CollId", "_CollVal", "_CshAcctId", "_DpstAmt", "_DpstTp", "_Hrcut", "_MtrtyDt", "_ValDt", "_XchgRate"]
	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if value is not None else base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if value is not None else base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if value is not None else base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

	@property
	def DpstAmt(self):
		return self._DpstAmt

	@DpstAmt.setter
	def DpstAmt(self, value):
		self._DpstAmt = value if value is not None else base_types.UninitialisedField(self, 'DpstAmt', ActiveCurrencyAndAmount, False)

	@DpstAmt.deleter
	def DpstAmt(self):
		del self._DpstAmt
		self._DpstAmt = base_types.UninitialisedField(self, 'DpstAmt', ActiveCurrencyAndAmount, False)

	@property
	def DpstTp(self):
		return self._DpstTp

	@DpstTp.setter
	def DpstTp(self, value):
		self._DpstTp = value if value is not None else base_types.UninitialisedField(self, 'DpstTp', DepositType1Code, False)

	@DpstTp.deleter
	def DpstTp(self):
		del self._DpstTp
		self._DpstTp = base_types.UninitialisedField(self, 'DpstTp', DepositType1Code, False)

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstTp', type=DepositType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))