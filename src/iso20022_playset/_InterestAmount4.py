# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CalculationMethod1Code
from . import CollateralBalance1
from . import CollateralPurpose1Choice
from . import DatePeriod2
from . import Frequency1Code
from . import ISODate
from . import InterestComputationMethod2Code
from . import InterestMethod1Code
from . import InterestRate1Choice
from . import InterestRequestSequence1Code
from . import Max140Text
from . import Max210Text
from . import Reference20
from . import YesNoIndicator

class InterestAmount4(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AddtlInf", "_ApldWhldgTax", "_ClctnFrqcy", "_ClctnMtd", "_ClsgCollBal", "_CollPurp", "_DayCntBsis", "_IntrstMtd", "_IntrstPrd", "_IntrstRate", "_IntrstReqSeq", "_OpngCollBal", "_RefDtls", "_StdSttlmInstrs", "_ValDt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max210Text, False)

	@property
	def ApldWhldgTax(self):
		return self._ApldWhldgTax

	@ApldWhldgTax.setter
	def ApldWhldgTax(self, value):
		self._ApldWhldgTax = value if value is not None else base_types.UninitialisedField(self, 'ApldWhldgTax', YesNoIndicator, False)

	@ApldWhldgTax.deleter
	def ApldWhldgTax(self):
		del self._ApldWhldgTax
		self._ApldWhldgTax = base_types.UninitialisedField(self, 'ApldWhldgTax', YesNoIndicator, False)

	@property
	def ClctnFrqcy(self):
		return self._ClctnFrqcy

	@ClctnFrqcy.setter
	def ClctnFrqcy(self, value):
		self._ClctnFrqcy = value if value is not None else base_types.UninitialisedField(self, 'ClctnFrqcy', Frequency1Code, False)

	@ClctnFrqcy.deleter
	def ClctnFrqcy(self):
		del self._ClctnFrqcy
		self._ClctnFrqcy = base_types.UninitialisedField(self, 'ClctnFrqcy', Frequency1Code, False)

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'ClctnMtd', CalculationMethod1Code, False)

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = base_types.UninitialisedField(self, 'ClctnMtd', CalculationMethod1Code, False)

	@property
	def ClsgCollBal(self):
		return self._ClsgCollBal

	@ClsgCollBal.setter
	def ClsgCollBal(self, value):
		self._ClsgCollBal = value if value is not None else base_types.UninitialisedField(self, 'ClsgCollBal', CollateralBalance1, False)

	@ClsgCollBal.deleter
	def ClsgCollBal(self):
		del self._ClsgCollBal
		self._ClsgCollBal = base_types.UninitialisedField(self, 'ClsgCollBal', CollateralBalance1, False)

	@property
	def CollPurp(self):
		return self._CollPurp

	@CollPurp.setter
	def CollPurp(self, value):
		self._CollPurp = value if value is not None else base_types.UninitialisedField(self, 'CollPurp', CollateralPurpose1Choice, False)

	@CollPurp.deleter
	def CollPurp(self):
		del self._CollPurp
		self._CollPurp = base_types.UninitialisedField(self, 'CollPurp', CollateralPurpose1Choice, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethod2Code, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethod2Code, False)

	@property
	def IntrstMtd(self):
		return self._IntrstMtd

	@IntrstMtd.setter
	def IntrstMtd(self, value):
		self._IntrstMtd = value if value is not None else base_types.UninitialisedField(self, 'IntrstMtd', InterestMethod1Code, False)

	@IntrstMtd.deleter
	def IntrstMtd(self):
		del self._IntrstMtd
		self._IntrstMtd = base_types.UninitialisedField(self, 'IntrstMtd', InterestMethod1Code, False)

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if value is not None else base_types.UninitialisedField(self, 'IntrstPrd', DatePeriod2, False)

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = base_types.UninitialisedField(self, 'IntrstPrd', DatePeriod2, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRate1Choice, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRate1Choice, False)

	@property
	def IntrstReqSeq(self):
		return self._IntrstReqSeq

	@IntrstReqSeq.setter
	def IntrstReqSeq(self, value):
		self._IntrstReqSeq = value if value is not None else base_types.UninitialisedField(self, 'IntrstReqSeq', InterestRequestSequence1Code, False)

	@IntrstReqSeq.deleter
	def IntrstReqSeq(self):
		del self._IntrstReqSeq
		self._IntrstReqSeq = base_types.UninitialisedField(self, 'IntrstReqSeq', InterestRequestSequence1Code, False)

	@property
	def OpngCollBal(self):
		return self._OpngCollBal

	@OpngCollBal.setter
	def OpngCollBal(self, value):
		self._OpngCollBal = value if value is not None else base_types.UninitialisedField(self, 'OpngCollBal', CollateralBalance1, False)

	@OpngCollBal.deleter
	def OpngCollBal(self):
		del self._OpngCollBal
		self._OpngCollBal = base_types.UninitialisedField(self, 'OpngCollBal', CollateralBalance1, False)

	@property
	def RefDtls(self):
		return self._RefDtls

	@RefDtls.setter
	def RefDtls(self, value):
		self._RefDtls = value if value is not None else base_types.UninitialisedField(self, 'RefDtls', Reference20, False)

	@RefDtls.deleter
	def RefDtls(self):
		del self._RefDtls
		self._RefDtls = base_types.UninitialisedField(self, 'RefDtls', Reference20, False)

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldWhldgTax', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnMtd', type=CalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgCollBal', type=CollateralBalance1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPurp', type=CollateralPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstMtd', type=InterestMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstReqSeq', type=InterestRequestSequence1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngCollBal', type=CollateralBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDtls', type=Reference20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))