from . import base_types
from .CalculationMethod1Code import CalculationMethod1Code
from .InterestRate1Choice import InterestRate1Choice
from .Frequency1Code import Frequency1Code
from .Max140Text import Max140Text
from .InterestComputationMethod2Code import InterestComputationMethod2Code
from .InterestMethod1Code import InterestMethod1Code
from .DatePeriod2 import DatePeriod2
from .Max210Text import Max210Text
from .CollateralBalance1 import CollateralBalance1
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .YesNoIndicator import YesNoIndicator
from .CollateralPurpose1Choice import CollateralPurpose1Choice

class InterestAmount3(base_types._BaseFieldType):

	__slots__ = ["_ApldWhldgTax", "_CollPurp", "_ValDt", "_StdSttlmInstrs", "_ClctnMtd", "_AddtlInf", "_DayCntBsis", "_IntrstRate", "_AcrdIntrstAmt", "_ClctnFrqcy", "_ClsgCollBal", "_IntrstPrd", "_OpngCollBal", "_IntrstMtd"]
	@property
	def ApldWhldgTax(self):
		return self._ApldWhldgTax

	@ApldWhldgTax.setter
	def ApldWhldgTax(self, value):
		self._ApldWhldgTax = value if type(value) != base_types.auto else self.make_default("ApldWhldgTax")

	@ApldWhldgTax.deleter
	def ApldWhldgTax(self):
		del self._ApldWhldgTax
		self._ApldWhldgTax = None

	@property
	def CollPurp(self):
		return self._CollPurp

	@CollPurp.setter
	def CollPurp(self, value):
		self._CollPurp = value if type(value) != base_types.auto else self.make_default("CollPurp")

	@CollPurp.deleter
	def CollPurp(self):
		del self._CollPurp
		self._CollPurp = None

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
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if type(value) != base_types.auto else self.make_default("StdSttlmInstrs")

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = None

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if type(value) != base_types.auto else self.make_default("ClctnMtd")

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != base_types.auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def ClctnFrqcy(self):
		return self._ClctnFrqcy

	@ClctnFrqcy.setter
	def ClctnFrqcy(self, value):
		self._ClctnFrqcy = value if type(value) != base_types.auto else self.make_default("ClctnFrqcy")

	@ClctnFrqcy.deleter
	def ClctnFrqcy(self):
		del self._ClctnFrqcy
		self._ClctnFrqcy = None

	@property
	def ClsgCollBal(self):
		return self._ClsgCollBal

	@ClsgCollBal.setter
	def ClsgCollBal(self, value):
		self._ClsgCollBal = value if type(value) != base_types.auto else self.make_default("ClsgCollBal")

	@ClsgCollBal.deleter
	def ClsgCollBal(self):
		del self._ClsgCollBal
		self._ClsgCollBal = None

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if type(value) != base_types.auto else self.make_default("IntrstPrd")

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = None

	@property
	def OpngCollBal(self):
		return self._OpngCollBal

	@OpngCollBal.setter
	def OpngCollBal(self, value):
		self._OpngCollBal = value if type(value) != base_types.auto else self.make_default("OpngCollBal")

	@OpngCollBal.deleter
	def OpngCollBal(self):
		del self._OpngCollBal
		self._OpngCollBal = None

	@property
	def IntrstMtd(self):
		return self._IntrstMtd

	@IntrstMtd.setter
	def IntrstMtd(self, value):
		self._IntrstMtd = value if type(value) != base_types.auto else self.make_default("IntrstMtd")

	@IntrstMtd.deleter
	def IntrstMtd(self):
		del self._IntrstMtd
		self._IntrstMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldWhldgTax', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPurp', type=CollateralPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnMtd', type=CalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgCollBal', type=CollateralBalance1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngCollBal', type=CollateralBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstMtd', type=InterestMethod1Code, min=1, max=1, mutex_group=None, array=False),
	))

