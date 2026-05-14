# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._DecimalNumber import DecimalNumber
from ._FinancialInstrument107 import FinancialInstrument107
from ._InvestmentAccount81 import InvestmentAccount81
from ._Max30DecimalNumber import Max30DecimalNumber
from ._PercentageRate import PercentageRate

class FundOrderData7(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknUnit", "_FinInstrmDtls", "_GrssAmt", "_HldgsRedRate", "_InvstmtAcctDtls", "_NetAmt", "_QtdCcy", "_SttlmAmt", "_UnitCcy", "_UnitsNb"]
	@property
	def DgtlTknUnit(self):
		return self._DgtlTknUnit

	@DgtlTknUnit.setter
	def DgtlTknUnit(self, value):
		self._DgtlTknUnit = value if type(value) != base_types.auto else self.make_default("DgtlTknUnit")

	@DgtlTknUnit.deleter
	def DgtlTknUnit(self):
		del self._DgtlTknUnit
		self._DgtlTknUnit = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if type(value) != base_types.auto else self.make_default("HldgsRedRate")

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if type(value) != base_types.auto else self.make_default("QtdCcy")

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if type(value) != base_types.auto else self.make_default("UnitCcy")

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlTknUnit', type=Max30DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))