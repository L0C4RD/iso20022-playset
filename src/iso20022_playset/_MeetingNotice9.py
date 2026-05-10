from . import base_types
from .FinancialInstrumentQuantity18Choice import FinancialInstrumentQuantity18Choice
from .DateFormat60Choice import DateFormat60Choice
from .AdditionalRights4 import AdditionalRights4
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .Attendance2 import Attendance2
from .YesNoIndicator import YesNoIndicator
from .Max2048Text import Max2048Text
from .Number import Number
from .MeetingType4Code import MeetingType4Code
from .MeetingTypeClassification2Choice import MeetingTypeClassification2Choice
from .DateFormat58Choice import DateFormat58Choice
from .Proxy5Choice import Proxy5Choice
from .DateFormat3Choice import DateFormat3Choice
from .MeetingContactPerson3 import MeetingContactPerson3
from .PostalAddress1 import PostalAddress1
from .DateFormat1 import DateFormat1
from .Max35Text import Max35Text
from .ParticipationMethod2 import ParticipationMethod2

class MeetingNotice9(base_types._BaseFieldType):

	__slots__ = ["_PrxyChc", "_IssrMtgId", "_CtctPrsnDtls", "_RegnSctiesDdln", "_SctiesBlckgPrdEndDt", "_Tp", "_EnrlmntMktDdln", "_EvtPrcgWebSiteAdr", "_RegnSctiesMktDdln", "_OneManOneVoteInd", "_AnncmntDt", "_TtlNbOfSctiesOutsdng", "_Clssfctn", "_RsltPblctnDt", "_Prtcptn", "_EnrlmntDdln", "_TtlNbOfVtngRghts", "_EntitlmntFxgDt", "_MtgId", "_PrxyAppntmntNtfctnAdr", "_AddtlDcmnttnURLAdr", "_AddtlPrcdrDtls", "_Attndnc"]
	@property
	def PrxyChc(self):
		return self._PrxyChc

	@PrxyChc.setter
	def PrxyChc(self, value):
		self._PrxyChc = value if type(value) != base_types.auto else self.make_default("PrxyChc")

	@PrxyChc.deleter
	def PrxyChc(self):
		del self._PrxyChc
		self._PrxyChc = None

	@property
	def IssrMtgId(self):
		return self._IssrMtgId

	@IssrMtgId.setter
	def IssrMtgId(self, value):
		self._IssrMtgId = value if type(value) != base_types.auto else self.make_default("IssrMtgId")

	@IssrMtgId.deleter
	def IssrMtgId(self):
		del self._IssrMtgId
		self._IssrMtgId = None

	@property
	def CtctPrsnDtls(self):
		return self._CtctPrsnDtls

	@CtctPrsnDtls.setter
	def CtctPrsnDtls(self, value):
		self._CtctPrsnDtls = value if type(value) != base_types.auto else self.make_default("CtctPrsnDtls")

	@CtctPrsnDtls.deleter
	def CtctPrsnDtls(self):
		del self._CtctPrsnDtls
		self._CtctPrsnDtls = None

	@property
	def RegnSctiesDdln(self):
		return self._RegnSctiesDdln

	@RegnSctiesDdln.setter
	def RegnSctiesDdln(self, value):
		self._RegnSctiesDdln = value if type(value) != base_types.auto else self.make_default("RegnSctiesDdln")

	@RegnSctiesDdln.deleter
	def RegnSctiesDdln(self):
		del self._RegnSctiesDdln
		self._RegnSctiesDdln = None

	@property
	def SctiesBlckgPrdEndDt(self):
		return self._SctiesBlckgPrdEndDt

	@SctiesBlckgPrdEndDt.setter
	def SctiesBlckgPrdEndDt(self, value):
		self._SctiesBlckgPrdEndDt = value if type(value) != base_types.auto else self.make_default("SctiesBlckgPrdEndDt")

	@SctiesBlckgPrdEndDt.deleter
	def SctiesBlckgPrdEndDt(self):
		del self._SctiesBlckgPrdEndDt
		self._SctiesBlckgPrdEndDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def EnrlmntMktDdln(self):
		return self._EnrlmntMktDdln

	@EnrlmntMktDdln.setter
	def EnrlmntMktDdln(self, value):
		self._EnrlmntMktDdln = value if type(value) != base_types.auto else self.make_default("EnrlmntMktDdln")

	@EnrlmntMktDdln.deleter
	def EnrlmntMktDdln(self):
		del self._EnrlmntMktDdln
		self._EnrlmntMktDdln = None

	@property
	def EvtPrcgWebSiteAdr(self):
		return self._EvtPrcgWebSiteAdr

	@EvtPrcgWebSiteAdr.setter
	def EvtPrcgWebSiteAdr(self, value):
		self._EvtPrcgWebSiteAdr = value if type(value) != base_types.auto else self.make_default("EvtPrcgWebSiteAdr")

	@EvtPrcgWebSiteAdr.deleter
	def EvtPrcgWebSiteAdr(self):
		del self._EvtPrcgWebSiteAdr
		self._EvtPrcgWebSiteAdr = None

	@property
	def RegnSctiesMktDdln(self):
		return self._RegnSctiesMktDdln

	@RegnSctiesMktDdln.setter
	def RegnSctiesMktDdln(self, value):
		self._RegnSctiesMktDdln = value if type(value) != base_types.auto else self.make_default("RegnSctiesMktDdln")

	@RegnSctiesMktDdln.deleter
	def RegnSctiesMktDdln(self):
		del self._RegnSctiesMktDdln
		self._RegnSctiesMktDdln = None

	@property
	def OneManOneVoteInd(self):
		return self._OneManOneVoteInd

	@OneManOneVoteInd.setter
	def OneManOneVoteInd(self, value):
		self._OneManOneVoteInd = value if type(value) != base_types.auto else self.make_default("OneManOneVoteInd")

	@OneManOneVoteInd.deleter
	def OneManOneVoteInd(self):
		del self._OneManOneVoteInd
		self._OneManOneVoteInd = None

	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if type(value) != base_types.auto else self.make_default("AnncmntDt")

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = None

	@property
	def TtlNbOfSctiesOutsdng(self):
		return self._TtlNbOfSctiesOutsdng

	@TtlNbOfSctiesOutsdng.setter
	def TtlNbOfSctiesOutsdng(self, value):
		self._TtlNbOfSctiesOutsdng = value if type(value) != base_types.auto else self.make_default("TtlNbOfSctiesOutsdng")

	@TtlNbOfSctiesOutsdng.deleter
	def TtlNbOfSctiesOutsdng(self):
		del self._TtlNbOfSctiesOutsdng
		self._TtlNbOfSctiesOutsdng = None

	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != base_types.auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	@property
	def RsltPblctnDt(self):
		return self._RsltPblctnDt

	@RsltPblctnDt.setter
	def RsltPblctnDt(self, value):
		self._RsltPblctnDt = value if type(value) != base_types.auto else self.make_default("RsltPblctnDt")

	@RsltPblctnDt.deleter
	def RsltPblctnDt(self):
		del self._RsltPblctnDt
		self._RsltPblctnDt = None

	@property
	def Prtcptn(self):
		return self._Prtcptn

	@Prtcptn.setter
	def Prtcptn(self, value):
		self._Prtcptn = value if type(value) != base_types.auto else self.make_default("Prtcptn")

	@Prtcptn.deleter
	def Prtcptn(self):
		del self._Prtcptn
		self._Prtcptn = None

	@property
	def EnrlmntDdln(self):
		return self._EnrlmntDdln

	@EnrlmntDdln.setter
	def EnrlmntDdln(self, value):
		self._EnrlmntDdln = value if type(value) != base_types.auto else self.make_default("EnrlmntDdln")

	@EnrlmntDdln.deleter
	def EnrlmntDdln(self):
		del self._EnrlmntDdln
		self._EnrlmntDdln = None

	@property
	def TtlNbOfVtngRghts(self):
		return self._TtlNbOfVtngRghts

	@TtlNbOfVtngRghts.setter
	def TtlNbOfVtngRghts(self, value):
		self._TtlNbOfVtngRghts = value if type(value) != base_types.auto else self.make_default("TtlNbOfVtngRghts")

	@TtlNbOfVtngRghts.deleter
	def TtlNbOfVtngRghts(self):
		del self._TtlNbOfVtngRghts
		self._TtlNbOfVtngRghts = None

	@property
	def EntitlmntFxgDt(self):
		return self._EntitlmntFxgDt

	@EntitlmntFxgDt.setter
	def EntitlmntFxgDt(self, value):
		self._EntitlmntFxgDt = value if type(value) != base_types.auto else self.make_default("EntitlmntFxgDt")

	@EntitlmntFxgDt.deleter
	def EntitlmntFxgDt(self):
		del self._EntitlmntFxgDt
		self._EntitlmntFxgDt = None

	@property
	def MtgId(self):
		return self._MtgId

	@MtgId.setter
	def MtgId(self, value):
		self._MtgId = value if type(value) != base_types.auto else self.make_default("MtgId")

	@MtgId.deleter
	def MtgId(self):
		del self._MtgId
		self._MtgId = None

	@property
	def PrxyAppntmntNtfctnAdr(self):
		return self._PrxyAppntmntNtfctnAdr

	@PrxyAppntmntNtfctnAdr.setter
	def PrxyAppntmntNtfctnAdr(self, value):
		self._PrxyAppntmntNtfctnAdr = value if type(value) != base_types.auto else self.make_default("PrxyAppntmntNtfctnAdr")

	@PrxyAppntmntNtfctnAdr.deleter
	def PrxyAppntmntNtfctnAdr(self):
		del self._PrxyAppntmntNtfctnAdr
		self._PrxyAppntmntNtfctnAdr = None

	@property
	def AddtlDcmnttnURLAdr(self):
		return self._AddtlDcmnttnURLAdr

	@AddtlDcmnttnURLAdr.setter
	def AddtlDcmnttnURLAdr(self, value):
		self._AddtlDcmnttnURLAdr = value if type(value) != base_types.auto else self.make_default("AddtlDcmnttnURLAdr")

	@AddtlDcmnttnURLAdr.deleter
	def AddtlDcmnttnURLAdr(self):
		del self._AddtlDcmnttnURLAdr
		self._AddtlDcmnttnURLAdr = None

	@property
	def AddtlPrcdrDtls(self):
		return self._AddtlPrcdrDtls

	@AddtlPrcdrDtls.setter
	def AddtlPrcdrDtls(self, value):
		self._AddtlPrcdrDtls = value if type(value) != base_types.auto else self.make_default("AddtlPrcdrDtls")

	@AddtlPrcdrDtls.deleter
	def AddtlPrcdrDtls(self):
		del self._AddtlPrcdrDtls
		self._AddtlPrcdrDtls = None

	@property
	def Attndnc(self):
		return self._Attndnc

	@Attndnc.setter
	def Attndnc(self, value):
		self._Attndnc = value if type(value) != base_types.auto else self.make_default("Attndnc")

	@Attndnc.deleter
	def Attndnc(self):
		del self._Attndnc
		self._Attndnc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrxyChc', type=Proxy5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrMtgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsnDtls', type=MeetingContactPerson3, min=0, max=12, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnSctiesDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBlckgPrdEndDt', type=DateFormat60Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MeetingType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgWebSiteAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnSctiesMktDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OneManOneVoteInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AnncmntDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfSctiesOutsdng', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clssfctn', type=MeetingTypeClassification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltPblctnDt', type=DateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtcptn', type=ParticipationMethod2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EnrlmntDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfVtngRghts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitlmntFxgDt', type=DateFormat1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrxyAppntmntNtfctnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlDcmnttnURLAdr', type=Max2048Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlPrcdrDtls', type=AdditionalRights4, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Attndnc', type=Attendance2, min=0, max=1, mutex_group=None, array=False),
	))

