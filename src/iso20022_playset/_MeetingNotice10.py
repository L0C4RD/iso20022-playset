# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalRights4
from . import Attendance2
from . import DateAndDateTime2Choice
from . import DateFormat1
from . import DateFormat3Choice
from . import DateFormat58Choice
from . import DateFormat60Choice
from . import FinancialInstrumentQuantity18Choice
from . import Max2048Text
from . import Max35Text
from . import MeetingContactPerson3
from . import MeetingType4Code
from . import MeetingTypeClassification2Choice
from . import Number
from . import ParticipationMethod3
from . import PostalAddress1
from . import Proxy5Choice
from . import YesNoIndicator

class MeetingNotice10(base_types._BaseFieldType):

	__slots__ = ["_AddtlDcmnttnURLAdr", "_AddtlPrcdrDtls", "_AnncmntDt", "_Attndnc", "_Clssfctn", "_CtctPrsnDtls", "_EnrlmntDdln", "_EnrlmntMktDdln", "_EntitlmntFxgDt", "_EvtPrcgWebSiteAdr", "_IssrMtgId", "_MtgId", "_OneManOneVoteInd", "_Prtcptn", "_PrxyAppntmntNtfctnAdr", "_PrxyChc", "_RegnSctiesDdln", "_RegnSctiesMktDdln", "_RsltPblctnDt", "_SctiesBlckgPrdEndDt", "_Tp", "_TtlNbOfSctiesOutsdng", "_TtlNbOfVtngRghts"]
	@property
	def AddtlDcmnttnURLAdr(self):
		return self._AddtlDcmnttnURLAdr

	@AddtlDcmnttnURLAdr.setter
	def AddtlDcmnttnURLAdr(self, value):
		self._AddtlDcmnttnURLAdr = value if value is not None else base_types.UninitialisedField(self, 'AddtlDcmnttnURLAdr', Max2048Text, True)

	@AddtlDcmnttnURLAdr.deleter
	def AddtlDcmnttnURLAdr(self):
		del self._AddtlDcmnttnURLAdr
		self._AddtlDcmnttnURLAdr = base_types.UninitialisedField(self, 'AddtlDcmnttnURLAdr', Max2048Text, True)

	@property
	def AddtlPrcdrDtls(self):
		return self._AddtlPrcdrDtls

	@AddtlPrcdrDtls.setter
	def AddtlPrcdrDtls(self, value):
		self._AddtlPrcdrDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlPrcdrDtls', AdditionalRights4, True)

	@AddtlPrcdrDtls.deleter
	def AddtlPrcdrDtls(self):
		del self._AddtlPrcdrDtls
		self._AddtlPrcdrDtls = base_types.UninitialisedField(self, 'AddtlPrcdrDtls', AdditionalRights4, True)

	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if value is not None else base_types.UninitialisedField(self, 'AnncmntDt', DateAndDateTime2Choice, False)

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = base_types.UninitialisedField(self, 'AnncmntDt', DateAndDateTime2Choice, False)

	@property
	def Attndnc(self):
		return self._Attndnc

	@Attndnc.setter
	def Attndnc(self, value):
		self._Attndnc = value if value is not None else base_types.UninitialisedField(self, 'Attndnc', Attendance2, False)

	@Attndnc.deleter
	def Attndnc(self):
		del self._Attndnc
		self._Attndnc = base_types.UninitialisedField(self, 'Attndnc', Attendance2, False)

	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', MeetingTypeClassification2Choice, False)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', MeetingTypeClassification2Choice, False)

	@property
	def CtctPrsnDtls(self):
		return self._CtctPrsnDtls

	@CtctPrsnDtls.setter
	def CtctPrsnDtls(self, value):
		self._CtctPrsnDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsnDtls', MeetingContactPerson3, True)

	@CtctPrsnDtls.deleter
	def CtctPrsnDtls(self):
		del self._CtctPrsnDtls
		self._CtctPrsnDtls = base_types.UninitialisedField(self, 'CtctPrsnDtls', MeetingContactPerson3, True)

	@property
	def EnrlmntDdln(self):
		return self._EnrlmntDdln

	@EnrlmntDdln.setter
	def EnrlmntDdln(self, value):
		self._EnrlmntDdln = value if value is not None else base_types.UninitialisedField(self, 'EnrlmntDdln', DateFormat58Choice, False)

	@EnrlmntDdln.deleter
	def EnrlmntDdln(self):
		del self._EnrlmntDdln
		self._EnrlmntDdln = base_types.UninitialisedField(self, 'EnrlmntDdln', DateFormat58Choice, False)

	@property
	def EnrlmntMktDdln(self):
		return self._EnrlmntMktDdln

	@EnrlmntMktDdln.setter
	def EnrlmntMktDdln(self, value):
		self._EnrlmntMktDdln = value if value is not None else base_types.UninitialisedField(self, 'EnrlmntMktDdln', DateFormat58Choice, False)

	@EnrlmntMktDdln.deleter
	def EnrlmntMktDdln(self):
		del self._EnrlmntMktDdln
		self._EnrlmntMktDdln = base_types.UninitialisedField(self, 'EnrlmntMktDdln', DateFormat58Choice, False)

	@property
	def EntitlmntFxgDt(self):
		return self._EntitlmntFxgDt

	@EntitlmntFxgDt.setter
	def EntitlmntFxgDt(self, value):
		self._EntitlmntFxgDt = value if value is not None else base_types.UninitialisedField(self, 'EntitlmntFxgDt', DateFormat1, False)

	@EntitlmntFxgDt.deleter
	def EntitlmntFxgDt(self):
		del self._EntitlmntFxgDt
		self._EntitlmntFxgDt = base_types.UninitialisedField(self, 'EntitlmntFxgDt', DateFormat1, False)

	@property
	def EvtPrcgWebSiteAdr(self):
		return self._EvtPrcgWebSiteAdr

	@EvtPrcgWebSiteAdr.setter
	def EvtPrcgWebSiteAdr(self, value):
		self._EvtPrcgWebSiteAdr = value if value is not None else base_types.UninitialisedField(self, 'EvtPrcgWebSiteAdr', Max2048Text, False)

	@EvtPrcgWebSiteAdr.deleter
	def EvtPrcgWebSiteAdr(self):
		del self._EvtPrcgWebSiteAdr
		self._EvtPrcgWebSiteAdr = base_types.UninitialisedField(self, 'EvtPrcgWebSiteAdr', Max2048Text, False)

	@property
	def IssrMtgId(self):
		return self._IssrMtgId

	@IssrMtgId.setter
	def IssrMtgId(self, value):
		self._IssrMtgId = value if value is not None else base_types.UninitialisedField(self, 'IssrMtgId', Max35Text, False)

	@IssrMtgId.deleter
	def IssrMtgId(self):
		del self._IssrMtgId
		self._IssrMtgId = base_types.UninitialisedField(self, 'IssrMtgId', Max35Text, False)

	@property
	def MtgId(self):
		return self._MtgId

	@MtgId.setter
	def MtgId(self, value):
		self._MtgId = value if value is not None else base_types.UninitialisedField(self, 'MtgId', Max35Text, False)

	@MtgId.deleter
	def MtgId(self):
		del self._MtgId
		self._MtgId = base_types.UninitialisedField(self, 'MtgId', Max35Text, False)

	@property
	def OneManOneVoteInd(self):
		return self._OneManOneVoteInd

	@OneManOneVoteInd.setter
	def OneManOneVoteInd(self, value):
		self._OneManOneVoteInd = value if value is not None else base_types.UninitialisedField(self, 'OneManOneVoteInd', YesNoIndicator, False)

	@OneManOneVoteInd.deleter
	def OneManOneVoteInd(self):
		del self._OneManOneVoteInd
		self._OneManOneVoteInd = base_types.UninitialisedField(self, 'OneManOneVoteInd', YesNoIndicator, False)

	@property
	def Prtcptn(self):
		return self._Prtcptn

	@Prtcptn.setter
	def Prtcptn(self, value):
		self._Prtcptn = value if value is not None else base_types.UninitialisedField(self, 'Prtcptn', ParticipationMethod3, True)

	@Prtcptn.deleter
	def Prtcptn(self):
		del self._Prtcptn
		self._Prtcptn = base_types.UninitialisedField(self, 'Prtcptn', ParticipationMethod3, True)

	@property
	def PrxyAppntmntNtfctnAdr(self):
		return self._PrxyAppntmntNtfctnAdr

	@PrxyAppntmntNtfctnAdr.setter
	def PrxyAppntmntNtfctnAdr(self, value):
		self._PrxyAppntmntNtfctnAdr = value if value is not None else base_types.UninitialisedField(self, 'PrxyAppntmntNtfctnAdr', PostalAddress1, False)

	@PrxyAppntmntNtfctnAdr.deleter
	def PrxyAppntmntNtfctnAdr(self):
		del self._PrxyAppntmntNtfctnAdr
		self._PrxyAppntmntNtfctnAdr = base_types.UninitialisedField(self, 'PrxyAppntmntNtfctnAdr', PostalAddress1, False)

	@property
	def PrxyChc(self):
		return self._PrxyChc

	@PrxyChc.setter
	def PrxyChc(self, value):
		self._PrxyChc = value if value is not None else base_types.UninitialisedField(self, 'PrxyChc', Proxy5Choice, False)

	@PrxyChc.deleter
	def PrxyChc(self):
		del self._PrxyChc
		self._PrxyChc = base_types.UninitialisedField(self, 'PrxyChc', Proxy5Choice, False)

	@property
	def RegnSctiesDdln(self):
		return self._RegnSctiesDdln

	@RegnSctiesDdln.setter
	def RegnSctiesDdln(self, value):
		self._RegnSctiesDdln = value if value is not None else base_types.UninitialisedField(self, 'RegnSctiesDdln', DateFormat58Choice, False)

	@RegnSctiesDdln.deleter
	def RegnSctiesDdln(self):
		del self._RegnSctiesDdln
		self._RegnSctiesDdln = base_types.UninitialisedField(self, 'RegnSctiesDdln', DateFormat58Choice, False)

	@property
	def RegnSctiesMktDdln(self):
		return self._RegnSctiesMktDdln

	@RegnSctiesMktDdln.setter
	def RegnSctiesMktDdln(self, value):
		self._RegnSctiesMktDdln = value if value is not None else base_types.UninitialisedField(self, 'RegnSctiesMktDdln', DateFormat58Choice, False)

	@RegnSctiesMktDdln.deleter
	def RegnSctiesMktDdln(self):
		del self._RegnSctiesMktDdln
		self._RegnSctiesMktDdln = base_types.UninitialisedField(self, 'RegnSctiesMktDdln', DateFormat58Choice, False)

	@property
	def RsltPblctnDt(self):
		return self._RsltPblctnDt

	@RsltPblctnDt.setter
	def RsltPblctnDt(self, value):
		self._RsltPblctnDt = value if value is not None else base_types.UninitialisedField(self, 'RsltPblctnDt', DateFormat3Choice, False)

	@RsltPblctnDt.deleter
	def RsltPblctnDt(self):
		del self._RsltPblctnDt
		self._RsltPblctnDt = base_types.UninitialisedField(self, 'RsltPblctnDt', DateFormat3Choice, False)

	@property
	def SctiesBlckgPrdEndDt(self):
		return self._SctiesBlckgPrdEndDt

	@SctiesBlckgPrdEndDt.setter
	def SctiesBlckgPrdEndDt(self, value):
		self._SctiesBlckgPrdEndDt = value if value is not None else base_types.UninitialisedField(self, 'SctiesBlckgPrdEndDt', DateFormat60Choice, False)

	@SctiesBlckgPrdEndDt.deleter
	def SctiesBlckgPrdEndDt(self):
		del self._SctiesBlckgPrdEndDt
		self._SctiesBlckgPrdEndDt = base_types.UninitialisedField(self, 'SctiesBlckgPrdEndDt', DateFormat60Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MeetingType4Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MeetingType4Code, False)

	@property
	def TtlNbOfSctiesOutsdng(self):
		return self._TtlNbOfSctiesOutsdng

	@TtlNbOfSctiesOutsdng.setter
	def TtlNbOfSctiesOutsdng(self, value):
		self._TtlNbOfSctiesOutsdng = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfSctiesOutsdng', FinancialInstrumentQuantity18Choice, False)

	@TtlNbOfSctiesOutsdng.deleter
	def TtlNbOfSctiesOutsdng(self):
		del self._TtlNbOfSctiesOutsdng
		self._TtlNbOfSctiesOutsdng = base_types.UninitialisedField(self, 'TtlNbOfSctiesOutsdng', FinancialInstrumentQuantity18Choice, False)

	@property
	def TtlNbOfVtngRghts(self):
		return self._TtlNbOfVtngRghts

	@TtlNbOfVtngRghts.setter
	def TtlNbOfVtngRghts(self, value):
		self._TtlNbOfVtngRghts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfVtngRghts', Number, False)

	@TtlNbOfVtngRghts.deleter
	def TtlNbOfVtngRghts(self):
		del self._TtlNbOfVtngRghts
		self._TtlNbOfVtngRghts = base_types.UninitialisedField(self, 'TtlNbOfVtngRghts', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlDcmnttnURLAdr', type=Max2048Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlPrcdrDtls', type=AdditionalRights4, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AnncmntDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attndnc', type=Attendance2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clssfctn', type=MeetingTypeClassification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsnDtls', type=MeetingContactPerson3, min=0, max=12, mutex_group=None, array=True),
		base_types.FieldEntry(name='EnrlmntDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitlmntFxgDt', type=DateFormat1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgWebSiteAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrMtgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OneManOneVoteInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtcptn', type=ParticipationMethod3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrxyAppntmntNtfctnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrxyChc', type=Proxy5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnSctiesDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnSctiesMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltPblctnDt', type=DateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBlckgPrdEndDt', type=DateFormat60Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MeetingType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfSctiesOutsdng', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfVtngRghts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))