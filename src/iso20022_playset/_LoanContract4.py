# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import ContractCollateral1
from . import DocumentGeneralInformation5
from . import DocumentIdentification22
from . import Exact1NumericText
from . import ISODate
from . import InterestPaymentSchedule1
from . import InterestRate2Choice
from . import LoanContractTranche1
from . import Max35Text
from . import PaymentSchedule1
from . import SpecialCondition1
from . import SyndicatedLoan3
from . import TradeParty6
from . import TrueFalseIndicator

class LoanContract4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Attchmnt", "_Buyr", "_Coll", "_CtrctDocId", "_DrtnCd", "_IntraCpnyLn", "_IntrstRate", "_IntrstSchdl", "_LnTpId", "_MtrtyDt", "_PmtSchdl", "_PrlngtnFlg", "_Sellr", "_SndctdLn", "_SpclConds", "_StartDt", "_SttlmCcy", "_Trch"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', TradeParty6, True)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', TradeParty6, True)

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', ContractCollateral1, False)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', ContractCollateral1, False)

	@property
	def CtrctDocId(self):
		return self._CtrctDocId

	@CtrctDocId.setter
	def CtrctDocId(self, value):
		self._CtrctDocId = value if value is not None else base_types.UninitialisedField(self, 'CtrctDocId', DocumentIdentification22, False)

	@CtrctDocId.deleter
	def CtrctDocId(self):
		del self._CtrctDocId
		self._CtrctDocId = base_types.UninitialisedField(self, 'CtrctDocId', DocumentIdentification22, False)

	@property
	def DrtnCd(self):
		return self._DrtnCd

	@DrtnCd.setter
	def DrtnCd(self, value):
		self._DrtnCd = value if value is not None else base_types.UninitialisedField(self, 'DrtnCd', Exact1NumericText, False)

	@DrtnCd.deleter
	def DrtnCd(self):
		del self._DrtnCd
		self._DrtnCd = base_types.UninitialisedField(self, 'DrtnCd', Exact1NumericText, False)

	@property
	def IntraCpnyLn(self):
		return self._IntraCpnyLn

	@IntraCpnyLn.setter
	def IntraCpnyLn(self, value):
		self._IntraCpnyLn = value if value is not None else base_types.UninitialisedField(self, 'IntraCpnyLn', TrueFalseIndicator, False)

	@IntraCpnyLn.deleter
	def IntraCpnyLn(self):
		del self._IntraCpnyLn
		self._IntraCpnyLn = base_types.UninitialisedField(self, 'IntraCpnyLn', TrueFalseIndicator, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRate2Choice, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRate2Choice, False)

	@property
	def IntrstSchdl(self):
		return self._IntrstSchdl

	@IntrstSchdl.setter
	def IntrstSchdl(self, value):
		self._IntrstSchdl = value if value is not None else base_types.UninitialisedField(self, 'IntrstSchdl', InterestPaymentSchedule1, True)

	@IntrstSchdl.deleter
	def IntrstSchdl(self):
		del self._IntrstSchdl
		self._IntrstSchdl = base_types.UninitialisedField(self, 'IntrstSchdl', InterestPaymentSchedule1, True)

	@property
	def LnTpId(self):
		return self._LnTpId

	@LnTpId.setter
	def LnTpId(self, value):
		self._LnTpId = value if value is not None else base_types.UninitialisedField(self, 'LnTpId', Max35Text, False)

	@LnTpId.deleter
	def LnTpId(self):
		del self._LnTpId
		self._LnTpId = base_types.UninitialisedField(self, 'LnTpId', Max35Text, False)

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
	def PmtSchdl(self):
		return self._PmtSchdl

	@PmtSchdl.setter
	def PmtSchdl(self, value):
		self._PmtSchdl = value if value is not None else base_types.UninitialisedField(self, 'PmtSchdl', PaymentSchedule1, True)

	@PmtSchdl.deleter
	def PmtSchdl(self):
		del self._PmtSchdl
		self._PmtSchdl = base_types.UninitialisedField(self, 'PmtSchdl', PaymentSchedule1, True)

	@property
	def PrlngtnFlg(self):
		return self._PrlngtnFlg

	@PrlngtnFlg.setter
	def PrlngtnFlg(self, value):
		self._PrlngtnFlg = value if value is not None else base_types.UninitialisedField(self, 'PrlngtnFlg', TrueFalseIndicator, False)

	@PrlngtnFlg.deleter
	def PrlngtnFlg(self):
		del self._PrlngtnFlg
		self._PrlngtnFlg = base_types.UninitialisedField(self, 'PrlngtnFlg', TrueFalseIndicator, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', TradeParty6, True)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', TradeParty6, True)

	@property
	def SndctdLn(self):
		return self._SndctdLn

	@SndctdLn.setter
	def SndctdLn(self, value):
		self._SndctdLn = value if value is not None else base_types.UninitialisedField(self, 'SndctdLn', SyndicatedLoan3, True)

	@SndctdLn.deleter
	def SndctdLn(self):
		del self._SndctdLn
		self._SndctdLn = base_types.UninitialisedField(self, 'SndctdLn', SyndicatedLoan3, True)

	@property
	def SpclConds(self):
		return self._SpclConds

	@SpclConds.setter
	def SpclConds(self, value):
		self._SpclConds = value if value is not None else base_types.UninitialisedField(self, 'SpclConds', SpecialCondition1, False)

	@SpclConds.deleter
	def SpclConds(self):
		del self._SpclConds
		self._SpclConds = base_types.UninitialisedField(self, 'SpclConds', SpecialCondition1, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def Trch(self):
		return self._Trch

	@Trch.setter
	def Trch(self, value):
		self._Trch = value if value is not None else base_types.UninitialisedField(self, 'Trch', LoanContractTranche1, True)

	@Trch.deleter
	def Trch(self):
		del self._Trch
		self._Trch = base_types.UninitialisedField(self, 'Trch', LoanContractTranche1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Buyr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Coll', type=ContractCollateral1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDocId', type=DocumentIdentification22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtnCd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraCpnyLn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstSchdl', type=InterestPaymentSchedule1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LnTpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdl', type=PaymentSchedule1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrlngtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndctdLn', type=SyndicatedLoan3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpclConds', type=SpecialCondition1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trch', type=LoanContractTranche1, min=0, max=None, mutex_group=None, array=True),
	))