# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DatePeriod2
from . import ISODate
from . import Max140Text
from . import PercentageRate
from . import TrueFalseIndicator

class CompensationResponse1(base_types._BaseFieldType):

	__slots__ = ["_AmtDue", "_Grantd", "_InitlAmt", "_IntrstRate", "_PdChrgs", "_Prd", "_Rsn", "_XpctdValDt"]
	@property
	def AmtDue(self):
		return self._AmtDue

	@AmtDue.setter
	def AmtDue(self, value):
		self._AmtDue = value if value is not None else base_types.UninitialisedField(self, 'AmtDue', ActiveCurrencyAndAmount, False)

	@AmtDue.deleter
	def AmtDue(self):
		del self._AmtDue
		self._AmtDue = base_types.UninitialisedField(self, 'AmtDue', ActiveCurrencyAndAmount, False)

	@property
	def Grantd(self):
		return self._Grantd

	@Grantd.setter
	def Grantd(self, value):
		self._Grantd = value if value is not None else base_types.UninitialisedField(self, 'Grantd', TrueFalseIndicator, False)

	@Grantd.deleter
	def Grantd(self):
		del self._Grantd
		self._Grantd = base_types.UninitialisedField(self, 'Grantd', TrueFalseIndicator, False)

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if value is not None else base_types.UninitialisedField(self, 'InitlAmt', ActiveCurrencyAndAmount, False)

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = base_types.UninitialisedField(self, 'InitlAmt', ActiveCurrencyAndAmount, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@property
	def PdChrgs(self):
		return self._PdChrgs

	@PdChrgs.setter
	def PdChrgs(self, value):
		self._PdChrgs = value if value is not None else base_types.UninitialisedField(self, 'PdChrgs', ActiveCurrencyAndAmount, False)

	@PdChrgs.deleter
	def PdChrgs(self):
		del self._PdChrgs
		self._PdChrgs = base_types.UninitialisedField(self, 'PdChrgs', ActiveCurrencyAndAmount, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DatePeriod2, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DatePeriod2, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max140Text, False)

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDue', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grantd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdChrgs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))