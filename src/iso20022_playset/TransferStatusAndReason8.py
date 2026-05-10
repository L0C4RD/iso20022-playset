import base_types
import BenefitCrystallisationEvent2
import DecimalNumber
import TransferStatus5Choice
import Unit11
import Drawdown2
import TransferStatusType3Choice
import AdditionalInformation15
import ActiveCurrencyAnd13DecimalAmount
import FinancialInstrument63Choice
import Drawdown3
import PaymentInstrument18
import Account33
import Max350Text
import PartyIdentification139
import ActiveOrHistoricCurrencyAnd13DecimalAmount
import Conversion2
import Max35Text
import ISODate
import AdditionalReference10
import Intermediary48

class TransferStatusAndReason8(base_types._BaseFieldType):

	__slots__ = ["_TtlUnitsNb", "_AvrgPric", "_QryRspn", "_UnitsDtls", "_Convs", "_MstrRef", "_ClntRef", "_OthrDrwdwnInf", "_TrfEvtTp", "_TrfRef", "_TradDt", "_SttlmDt", "_BnftCrstllstnEvt", "_IntrmyInf", "_InvstmtAcctDtls", "_SndOutDt", "_CshSttlmDt", "_TrfSts", "_TtlTrfVal", "_PmtDtls", "_DrwdwnTrch", "_StsIssr", "_StsInitr", "_AddtlInf", "_StsRcpt", "_CxlRef", "_Instrm"]
	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	@property
	def AvrgPric(self):
		return self._AvrgPric

	@AvrgPric.setter
	def AvrgPric(self, value):
		self._AvrgPric = value if type(value) != auto else self.make_default("AvrgPric")

	@AvrgPric.deleter
	def AvrgPric(self):
		del self._AvrgPric
		self._AvrgPric = None

	@property
	def QryRspn(self):
		return self._QryRspn

	@QryRspn.setter
	def QryRspn(self, value):
		self._QryRspn = value if type(value) != auto else self.make_default("QryRspn")

	@QryRspn.deleter
	def QryRspn(self):
		del self._QryRspn
		self._QryRspn = None

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if type(value) != auto else self.make_default("UnitsDtls")

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = None

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def OthrDrwdwnInf(self):
		return self._OthrDrwdwnInf

	@OthrDrwdwnInf.setter
	def OthrDrwdwnInf(self, value):
		self._OthrDrwdwnInf = value if type(value) != auto else self.make_default("OthrDrwdwnInf")

	@OthrDrwdwnInf.deleter
	def OthrDrwdwnInf(self):
		del self._OthrDrwdwnInf
		self._OthrDrwdwnInf = None

	@property
	def TrfEvtTp(self):
		return self._TrfEvtTp

	@TrfEvtTp.setter
	def TrfEvtTp(self, value):
		self._TrfEvtTp = value if type(value) != auto else self.make_default("TrfEvtTp")

	@TrfEvtTp.deleter
	def TrfEvtTp(self):
		del self._TrfEvtTp
		self._TrfEvtTp = None

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if type(value) != auto else self.make_default("TrfRef")

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def BnftCrstllstnEvt(self):
		return self._BnftCrstllstnEvt

	@BnftCrstllstnEvt.setter
	def BnftCrstllstnEvt(self, value):
		self._BnftCrstllstnEvt = value if type(value) != auto else self.make_default("BnftCrstllstnEvt")

	@BnftCrstllstnEvt.deleter
	def BnftCrstllstnEvt(self):
		del self._BnftCrstllstnEvt
		self._BnftCrstllstnEvt = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def SndOutDt(self):
		return self._SndOutDt

	@SndOutDt.setter
	def SndOutDt(self, value):
		self._SndOutDt = value if type(value) != auto else self.make_default("SndOutDt")

	@SndOutDt.deleter
	def SndOutDt(self):
		del self._SndOutDt
		self._SndOutDt = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def TrfSts(self):
		return self._TrfSts

	@TrfSts.setter
	def TrfSts(self, value):
		self._TrfSts = value if type(value) != auto else self.make_default("TrfSts")

	@TrfSts.deleter
	def TrfSts(self):
		del self._TrfSts
		self._TrfSts = None

	@property
	def TtlTrfVal(self):
		return self._TtlTrfVal

	@TtlTrfVal.setter
	def TtlTrfVal(self, value):
		self._TtlTrfVal = value if type(value) != auto else self.make_default("TtlTrfVal")

	@TtlTrfVal.deleter
	def TtlTrfVal(self):
		del self._TtlTrfVal
		self._TtlTrfVal = None

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if type(value) != auto else self.make_default("PmtDtls")

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = None

	@property
	def DrwdwnTrch(self):
		return self._DrwdwnTrch

	@DrwdwnTrch.setter
	def DrwdwnTrch(self, value):
		self._DrwdwnTrch = value if type(value) != auto else self.make_default("DrwdwnTrch")

	@DrwdwnTrch.deleter
	def DrwdwnTrch(self):
		del self._DrwdwnTrch
		self._DrwdwnTrch = None

	@property
	def StsIssr(self):
		return self._StsIssr

	@StsIssr.setter
	def StsIssr(self, value):
		self._StsIssr = value if type(value) != auto else self.make_default("StsIssr")

	@StsIssr.deleter
	def StsIssr(self):
		del self._StsIssr
		self._StsIssr = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

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
	def StsRcpt(self):
		return self._StsRcpt

	@StsRcpt.setter
	def StsRcpt(self, value):
		self._StsRcpt = value if type(value) != auto else self.make_default("StsRcpt")

	@StsRcpt.deleter
	def StsRcpt(self):
		del self._StsRcpt
		self._StsRcpt = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRspn', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnitsDtls', type=Unit11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Convs', type=Conversion2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDrwdwnInf', type=Drawdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfEvtTp', type=TransferStatusType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnftCrstllstnEvt', type=BenefitCrystallisationEvent2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=Account33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfSts', type=TransferStatus5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTrfVal', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrwdwnTrch', type=Drawdown2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsIssr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsRcpt', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument63Choice, min=0, max=1, mutex_group=None, array=False),
	))

