# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._DepositType1Code import DepositType1Code
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate

class CashCollateral4(base_types._BaseFieldType):

	__slots__ = ["_AsstNb", "_BlckdAmt", "_CollVal", "_DpstAmt", "_DpstTp", "_Hrcut", "_MtrtyDt", "_ValDt", "_XchgRate"]
	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if type(value) != base_types.auto else self.make_default("AsstNb")

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = None

	@property
	def BlckdAmt(self):
		return self._BlckdAmt

	@BlckdAmt.setter
	def BlckdAmt(self, value):
		self._BlckdAmt = value if type(value) != base_types.auto else self.make_default("BlckdAmt")

	@BlckdAmt.deleter
	def BlckdAmt(self):
		del self._BlckdAmt
		self._BlckdAmt = None

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
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstTp', type=DepositType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))