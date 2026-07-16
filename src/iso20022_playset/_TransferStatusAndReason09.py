# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account36
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import AdditionalReference10
from . import BenefitCrystallisationEvent2
from . import Conversion4
from . import DecimalNumber
from . import Drawdown04
from . import Drawdown3
from . import FinancialInstrument101Choice
from . import ISODate
from . import Intermediary48
from . import Max350Text
from . import Max35Text
from . import PartyIdentification139
from . import PaymentInstrument23
from . import TransferStatus5Choice
from . import TransferStatusType3Choice
from . import Unit14

class TransferStatusAndReason09(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AvrgPric", "_BnftCrstllstnEvt", "_ClntRef", "_Convs", "_CshSttlmDt", "_CxlRef", "_DrwdwnTrch", "_Instrm", "_IntrmyInf", "_InvstmtAcctDtls", "_MstrRef", "_OthrDrwdwnInf", "_PmtDtls", "_QryRspn", "_SndOutDt", "_StsInitr", "_StsIssr", "_StsRcpt", "_SttlmDt", "_TradDt", "_TrfEvtTp", "_TrfRef", "_TrfSts", "_TtlTrfVal", "_TtlUnitsNb", "_UnitsDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def AvrgPric(self):
		return self._AvrgPric

	@AvrgPric.setter
	def AvrgPric(self, value):
		self._AvrgPric = value if value is not None else base_types.UninitialisedField(self, 'AvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@AvrgPric.deleter
	def AvrgPric(self):
		del self._AvrgPric
		self._AvrgPric = base_types.UninitialisedField(self, 'AvrgPric', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def BnftCrstllstnEvt(self):
		return self._BnftCrstllstnEvt

	@BnftCrstllstnEvt.setter
	def BnftCrstllstnEvt(self, value):
		self._BnftCrstllstnEvt = value if value is not None else base_types.UninitialisedField(self, 'BnftCrstllstnEvt', BenefitCrystallisationEvent2, True)

	@BnftCrstllstnEvt.deleter
	def BnftCrstllstnEvt(self):
		del self._BnftCrstllstnEvt
		self._BnftCrstllstnEvt = base_types.UninitialisedField(self, 'BnftCrstllstnEvt', BenefitCrystallisationEvent2, True)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if value is not None else base_types.UninitialisedField(self, 'Convs', Conversion4, False)

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = base_types.UninitialisedField(self, 'Convs', Conversion4, False)

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if value is not None else base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@property
	def DrwdwnTrch(self):
		return self._DrwdwnTrch

	@DrwdwnTrch.setter
	def DrwdwnTrch(self, value):
		self._DrwdwnTrch = value if value is not None else base_types.UninitialisedField(self, 'DrwdwnTrch', Drawdown04, True)

	@DrwdwnTrch.deleter
	def DrwdwnTrch(self):
		del self._DrwdwnTrch
		self._DrwdwnTrch = base_types.UninitialisedField(self, 'DrwdwnTrch', Drawdown04, True)

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', FinancialInstrument101Choice, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', FinancialInstrument101Choice, False)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary48, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary48, True)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', Account36, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', Account36, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def OthrDrwdwnInf(self):
		return self._OthrDrwdwnInf

	@OthrDrwdwnInf.setter
	def OthrDrwdwnInf(self, value):
		self._OthrDrwdwnInf = value if value is not None else base_types.UninitialisedField(self, 'OthrDrwdwnInf', Drawdown3, False)

	@OthrDrwdwnInf.deleter
	def OthrDrwdwnInf(self):
		del self._OthrDrwdwnInf
		self._OthrDrwdwnInf = base_types.UninitialisedField(self, 'OthrDrwdwnInf', Drawdown3, False)

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument23, True)

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument23, True)

	@property
	def QryRspn(self):
		return self._QryRspn

	@QryRspn.setter
	def QryRspn(self, value):
		self._QryRspn = value if value is not None else base_types.UninitialisedField(self, 'QryRspn', Max350Text, True)

	@QryRspn.deleter
	def QryRspn(self):
		del self._QryRspn
		self._QryRspn = base_types.UninitialisedField(self, 'QryRspn', Max350Text, True)

	@property
	def SndOutDt(self):
		return self._SndOutDt

	@SndOutDt.setter
	def SndOutDt(self, value):
		self._SndOutDt = value if value is not None else base_types.UninitialisedField(self, 'SndOutDt', ISODate, False)

	@SndOutDt.deleter
	def SndOutDt(self):
		del self._SndOutDt
		self._SndOutDt = base_types.UninitialisedField(self, 'SndOutDt', ISODate, False)

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if value is not None else base_types.UninitialisedField(self, 'StsInitr', PartyIdentification139, False)

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = base_types.UninitialisedField(self, 'StsInitr', PartyIdentification139, False)

	@property
	def StsIssr(self):
		return self._StsIssr

	@StsIssr.setter
	def StsIssr(self, value):
		self._StsIssr = value if value is not None else base_types.UninitialisedField(self, 'StsIssr', PartyIdentification139, False)

	@StsIssr.deleter
	def StsIssr(self):
		del self._StsIssr
		self._StsIssr = base_types.UninitialisedField(self, 'StsIssr', PartyIdentification139, False)

	@property
	def StsRcpt(self):
		return self._StsRcpt

	@StsRcpt.setter
	def StsRcpt(self, value):
		self._StsRcpt = value if value is not None else base_types.UninitialisedField(self, 'StsRcpt', PartyIdentification139, False)

	@StsRcpt.deleter
	def StsRcpt(self):
		del self._StsRcpt
		self._StsRcpt = base_types.UninitialisedField(self, 'StsRcpt', PartyIdentification139, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TrfEvtTp(self):
		return self._TrfEvtTp

	@TrfEvtTp.setter
	def TrfEvtTp(self, value):
		self._TrfEvtTp = value if value is not None else base_types.UninitialisedField(self, 'TrfEvtTp', TransferStatusType3Choice, True)

	@TrfEvtTp.deleter
	def TrfEvtTp(self):
		del self._TrfEvtTp
		self._TrfEvtTp = base_types.UninitialisedField(self, 'TrfEvtTp', TransferStatusType3Choice, True)

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfRef', AdditionalReference10, False)

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = base_types.UninitialisedField(self, 'TrfRef', AdditionalReference10, False)

	@property
	def TrfSts(self):
		return self._TrfSts

	@TrfSts.setter
	def TrfSts(self, value):
		self._TrfSts = value if value is not None else base_types.UninitialisedField(self, 'TrfSts', TransferStatus5Choice, False)

	@TrfSts.deleter
	def TrfSts(self):
		del self._TrfSts
		self._TrfSts = base_types.UninitialisedField(self, 'TrfSts', TransferStatus5Choice, False)

	@property
	def TtlTrfVal(self):
		return self._TtlTrfVal

	@TtlTrfVal.setter
	def TtlTrfVal(self, value):
		self._TtlTrfVal = value if value is not None else base_types.UninitialisedField(self, 'TtlTrfVal', ActiveCurrencyAnd13DecimalAmount, False)

	@TtlTrfVal.deleter
	def TtlTrfVal(self):
		del self._TtlTrfVal
		self._TtlTrfVal = base_types.UninitialisedField(self, 'TtlTrfVal', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if value is not None else base_types.UninitialisedField(self, 'UnitsDtls', Unit14, True)

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = base_types.UninitialisedField(self, 'UnitsDtls', Unit14, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AvrgPric', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnftCrstllstnEvt', type=BenefitCrystallisationEvent2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=Conversion4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTrch', type=Drawdown04, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument101Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=Account36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDrwdwnInf', type=Drawdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QryRspn', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SndOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsIssr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRcpt', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfEvtTp', type=TransferStatusType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfRef', type=AdditionalReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfSts', type=TransferStatus5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTrfVal', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit14, min=0, max=None, mutex_group=None, array=True),
	))