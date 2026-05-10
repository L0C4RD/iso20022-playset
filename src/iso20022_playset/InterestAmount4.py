import base_types
import InterestRequestSequence1Code
import DatePeriod2
import InterestRate1Choice
import YesNoIndicator
import Reference20
import CalculationMethod1Code
import ISODate
import ActiveCurrencyAndAmount
import InterestMethod1Code
import Max140Text
import CollateralBalance1
import InterestComputationMethod2Code
import Max210Text
import CollateralPurpose1Choice
import Frequency1Code

class InterestAmount4(base_types._BaseFieldType):

	__slots__ = ["_DayCntBsis", "_ClctnMtd", "_RefDtls", "_StdSttlmInstrs", "_CollPurp", "_ValDt", "_AcrdIntrstAmt", "_OpngCollBal", "_IntrstRate", "_AddtlInf", "_ClctnFrqcy", "_IntrstReqSeq", "_ApldWhldgTax", "_IntrstPrd", "_IntrstMtd", "_ClsgCollBal"]
	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if type(value) != auto else self.make_default("ClctnMtd")

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = None

	@property
	def RefDtls(self):
		return self._RefDtls

	@RefDtls.setter
	def RefDtls(self, value):
		self._RefDtls = value if type(value) != auto else self.make_default("RefDtls")

	@RefDtls.deleter
	def RefDtls(self):
		del self._RefDtls
		self._RefDtls = None

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if type(value) != auto else self.make_default("StdSttlmInstrs")

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = None

	@property
	def CollPurp(self):
		return self._CollPurp

	@CollPurp.setter
	def CollPurp(self, value):
		self._CollPurp = value if type(value) != auto else self.make_default("CollPurp")

	@CollPurp.deleter
	def CollPurp(self):
		del self._CollPurp
		self._CollPurp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def OpngCollBal(self):
		return self._OpngCollBal

	@OpngCollBal.setter
	def OpngCollBal(self, value):
		self._OpngCollBal = value if type(value) != auto else self.make_default("OpngCollBal")

	@OpngCollBal.deleter
	def OpngCollBal(self):
		del self._OpngCollBal
		self._OpngCollBal = None

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
	def ClctnFrqcy(self):
		return self._ClctnFrqcy

	@ClctnFrqcy.setter
	def ClctnFrqcy(self, value):
		self._ClctnFrqcy = value if type(value) != auto else self.make_default("ClctnFrqcy")

	@ClctnFrqcy.deleter
	def ClctnFrqcy(self):
		del self._ClctnFrqcy
		self._ClctnFrqcy = None

	@property
	def IntrstReqSeq(self):
		return self._IntrstReqSeq

	@IntrstReqSeq.setter
	def IntrstReqSeq(self, value):
		self._IntrstReqSeq = value if type(value) != auto else self.make_default("IntrstReqSeq")

	@IntrstReqSeq.deleter
	def IntrstReqSeq(self):
		del self._IntrstReqSeq
		self._IntrstReqSeq = None

	@property
	def ApldWhldgTax(self):
		return self._ApldWhldgTax

	@ApldWhldgTax.setter
	def ApldWhldgTax(self, value):
		self._ApldWhldgTax = value if type(value) != auto else self.make_default("ApldWhldgTax")

	@ApldWhldgTax.deleter
	def ApldWhldgTax(self):
		del self._ApldWhldgTax
		self._ApldWhldgTax = None

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if type(value) != auto else self.make_default("IntrstPrd")

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = None

	@property
	def IntrstMtd(self):
		return self._IntrstMtd

	@IntrstMtd.setter
	def IntrstMtd(self, value):
		self._IntrstMtd = value if type(value) != auto else self.make_default("IntrstMtd")

	@IntrstMtd.deleter
	def IntrstMtd(self):
		del self._IntrstMtd
		self._IntrstMtd = None

	@property
	def ClsgCollBal(self):
		return self._ClsgCollBal

	@ClsgCollBal.setter
	def ClsgCollBal(self, value):
		self._ClsgCollBal = value if type(value) != auto else self.make_default("ClsgCollBal")

	@ClsgCollBal.deleter
	def ClsgCollBal(self):
		del self._ClsgCollBal
		self._ClsgCollBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnMtd', type=CalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDtls', type=Reference20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPurp', type=CollateralPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngCollBal', type=CollateralBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstReqSeq', type=InterestRequestSequence1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldWhldgTax', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstMtd', type=InterestMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgCollBal', type=CollateralBalance1, min=1, max=1, mutex_group=None, array=False),
	))

