import base_types
import DatePeriod2
import ISODate
import PercentageRate
import TrueFalseIndicator
import Max140Text
import ActiveCurrencyAndAmount

class CompensationResponse1(base_types._BaseFieldType):

	__slots__ = ["_PdChrgs", "_XpctdValDt", "_InitlAmt", "_Rsn", "_Prd", "_AmtDue", "_IntrstRate", "_Grantd"]
	@property
	def PdChrgs(self):
		return self._PdChrgs

	@PdChrgs.setter
	def PdChrgs(self, value):
		self._PdChrgs = value if type(value) != auto else self.make_default("PdChrgs")

	@PdChrgs.deleter
	def PdChrgs(self):
		del self._PdChrgs
		self._PdChrgs = None

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if type(value) != auto else self.make_default("XpctdValDt")

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = None

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if type(value) != auto else self.make_default("InitlAmt")

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def AmtDue(self):
		return self._AmtDue

	@AmtDue.setter
	def AmtDue(self, value):
		self._AmtDue = value if type(value) != auto else self.make_default("AmtDue")

	@AmtDue.deleter
	def AmtDue(self):
		del self._AmtDue
		self._AmtDue = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def Grantd(self):
		return self._Grantd

	@Grantd.setter
	def Grantd(self, value):
		self._Grantd = value if type(value) != auto else self.make_default("Grantd")

	@Grantd.deleter
	def Grantd(self):
		del self._Grantd
		self._Grantd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdChrgs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDue', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grantd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))

