from . import base_types
from .CountryCode import CountryCode
from .TaxCalculationInformation10 import TaxCalculationInformation10
from .PercentageRate import PercentageRate
from .PartyIdentification139 import PartyIdentification139
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .TaxType3Choice import TaxType3Choice

class Tax35(base_types._BaseFieldType):

	__slots__ = ["_ApldRate", "_RcptId", "_ApldAmt", "_Ctry", "_Tp", "_TaxClctnDtls"]
	@property
	def ApldRate(self):
		return self._ApldRate

	@ApldRate.setter
	def ApldRate(self, value):
		self._ApldRate = value if type(value) != auto else self.make_default("ApldRate")

	@ApldRate.deleter
	def ApldRate(self):
		del self._ApldRate
		self._ApldRate = None

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if type(value) != auto else self.make_default("RcptId")

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = None

	@property
	def ApldAmt(self):
		return self._ApldAmt

	@ApldAmt.setter
	def ApldAmt(self, value):
		self._ApldAmt = value if type(value) != auto else self.make_default("ApldAmt")

	@ApldAmt.deleter
	def ApldAmt(self):
		del self._ApldAmt
		self._ApldAmt = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if type(value) != auto else self.make_default("TaxClctnDtls")

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation10, min=0, max=1, mutex_group=None, array=False),
	))

