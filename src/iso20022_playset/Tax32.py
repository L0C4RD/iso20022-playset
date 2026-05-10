from . import base_types
import PercentageRate
import CountryCode
import YesNoIndicator
import ActiveCurrencyAndAmount
import TaxCalculationInformation10
import PartyIdentification113
import TaxType3Choice
import ExemptionReason1Choice

class Tax32(base_types._BaseFieldType):

	__slots__ = ["_InftvRate", "_RcptId", "_Tp", "_TaxClctnDtls", "_XmptnRsn", "_Ctry", "_InftvAmt", "_XmptnInd"]
	@property
	def InftvRate(self):
		return self._InftvRate

	@InftvRate.setter
	def InftvRate(self, value):
		self._InftvRate = value if type(value) != auto else self.make_default("InftvRate")

	@InftvRate.deleter
	def InftvRate(self):
		del self._InftvRate
		self._InftvRate = None

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

	@property
	def XmptnRsn(self):
		return self._XmptnRsn

	@XmptnRsn.setter
	def XmptnRsn(self, value):
		self._XmptnRsn = value if type(value) != auto else self.make_default("XmptnRsn")

	@XmptnRsn.deleter
	def XmptnRsn(self):
		del self._XmptnRsn
		self._XmptnRsn = None

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
	def InftvAmt(self):
		return self._InftvAmt

	@InftvAmt.setter
	def InftvAmt(self, value):
		self._InftvAmt = value if type(value) != auto else self.make_default("InftvAmt")

	@InftvAmt.deleter
	def InftvAmt(self):
		del self._InftvAmt
		self._InftvAmt = None

	@property
	def XmptnInd(self):
		return self._XmptnInd

	@XmptnInd.setter
	def XmptnInd(self, value):
		self._XmptnInd = value if type(value) != auto else self.make_default("XmptnInd")

	@XmptnInd.deleter
	def XmptnInd(self):
		del self._XmptnInd
		self._XmptnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InftvRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsn', type=ExemptionReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

