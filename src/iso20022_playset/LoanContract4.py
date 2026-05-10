from . import base_types
import ISODate
import DocumentGeneralInformation5
import Max35Text
import ActiveCurrencyAndAmount
import ActiveCurrencyCode
import PaymentSchedule1
import Exact1NumericText
import TrueFalseIndicator
import LoanContractTranche1
import ContractCollateral1
import TradeParty6
import SyndicatedLoan3
import InterestPaymentSchedule1
import DocumentIdentification22
import SpecialCondition1
import InterestRate2Choice

class LoanContract4(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_MtrtyDt", "_Coll", "_IntrstRate", "_Amt", "_IntrstSchdl", "_Sellr", "_SpclConds", "_LnTpId", "_CtrctDocId", "_SttlmCcy", "_DrtnCd", "_StartDt", "_Attchmnt", "_PrlngtnFlg", "_IntraCpnyLn", "_Trch", "_SndctdLn", "_PmtSchdl"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

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
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def IntrstSchdl(self):
		return self._IntrstSchdl

	@IntrstSchdl.setter
	def IntrstSchdl(self, value):
		self._IntrstSchdl = value if type(value) != auto else self.make_default("IntrstSchdl")

	@IntrstSchdl.deleter
	def IntrstSchdl(self):
		del self._IntrstSchdl
		self._IntrstSchdl = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def SpclConds(self):
		return self._SpclConds

	@SpclConds.setter
	def SpclConds(self, value):
		self._SpclConds = value if type(value) != auto else self.make_default("SpclConds")

	@SpclConds.deleter
	def SpclConds(self):
		del self._SpclConds
		self._SpclConds = None

	@property
	def LnTpId(self):
		return self._LnTpId

	@LnTpId.setter
	def LnTpId(self, value):
		self._LnTpId = value if type(value) != auto else self.make_default("LnTpId")

	@LnTpId.deleter
	def LnTpId(self):
		del self._LnTpId
		self._LnTpId = None

	@property
	def CtrctDocId(self):
		return self._CtrctDocId

	@CtrctDocId.setter
	def CtrctDocId(self, value):
		self._CtrctDocId = value if type(value) != auto else self.make_default("CtrctDocId")

	@CtrctDocId.deleter
	def CtrctDocId(self):
		del self._CtrctDocId
		self._CtrctDocId = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def DrtnCd(self):
		return self._DrtnCd

	@DrtnCd.setter
	def DrtnCd(self, value):
		self._DrtnCd = value if type(value) != auto else self.make_default("DrtnCd")

	@DrtnCd.deleter
	def DrtnCd(self):
		del self._DrtnCd
		self._DrtnCd = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def PrlngtnFlg(self):
		return self._PrlngtnFlg

	@PrlngtnFlg.setter
	def PrlngtnFlg(self, value):
		self._PrlngtnFlg = value if type(value) != auto else self.make_default("PrlngtnFlg")

	@PrlngtnFlg.deleter
	def PrlngtnFlg(self):
		del self._PrlngtnFlg
		self._PrlngtnFlg = None

	@property
	def IntraCpnyLn(self):
		return self._IntraCpnyLn

	@IntraCpnyLn.setter
	def IntraCpnyLn(self, value):
		self._IntraCpnyLn = value if type(value) != auto else self.make_default("IntraCpnyLn")

	@IntraCpnyLn.deleter
	def IntraCpnyLn(self):
		del self._IntraCpnyLn
		self._IntraCpnyLn = None

	@property
	def Trch(self):
		return self._Trch

	@Trch.setter
	def Trch(self, value):
		self._Trch = value if type(value) != auto else self.make_default("Trch")

	@Trch.deleter
	def Trch(self):
		del self._Trch
		self._Trch = None

	@property
	def SndctdLn(self):
		return self._SndctdLn

	@SndctdLn.setter
	def SndctdLn(self, value):
		self._SndctdLn = value if type(value) != auto else self.make_default("SndctdLn")

	@SndctdLn.deleter
	def SndctdLn(self):
		del self._SndctdLn
		self._SndctdLn = None

	@property
	def PmtSchdl(self):
		return self._PmtSchdl

	@PmtSchdl.setter
	def PmtSchdl(self, value):
		self._PmtSchdl = value if type(value) != auto else self.make_default("PmtSchdl")

	@PmtSchdl.deleter
	def PmtSchdl(self):
		del self._PmtSchdl
		self._PmtSchdl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=ContractCollateral1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstSchdl', type=InterestPaymentSchedule1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpclConds', type=SpecialCondition1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnTpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDocId', type=DocumentIdentification22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtnCd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrlngtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraCpnyLn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trch', type=LoanContractTranche1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndctdLn', type=SyndicatedLoan3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSchdl', type=PaymentSchedule1, min=0, max=None, mutex_group=None, array=True),
	))

