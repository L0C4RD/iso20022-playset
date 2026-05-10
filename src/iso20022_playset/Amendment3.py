import base_types
import Document9
import Beneficiary1
import Narrative1
import UndertakingTermination3
import UndertakingAmount2
import Max35Text
import Undertaking10
import Undertaking9
import Max2000Text
import CommunicationChannel1
import PartyIdentification43
import ExpiryDetails2

class Amendment3(base_types._BaseFieldType):

	__slots__ = ["_DlvryChanl", "_TermntnDtls", "_ApplcntReqNb", "_AddtlInf", "_NewUdrtkgTermsAndConds", "_NclsdFile", "_Applcnt", "_CntrUdrtkg", "_UdrtkgId", "_NewXpryDtls", "_IncrDcrAmt", "_NewBnfcry"]
	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if type(value) != auto else self.make_default("DlvryChanl")

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = None

	@property
	def TermntnDtls(self):
		return self._TermntnDtls

	@TermntnDtls.setter
	def TermntnDtls(self, value):
		self._TermntnDtls = value if type(value) != auto else self.make_default("TermntnDtls")

	@TermntnDtls.deleter
	def TermntnDtls(self):
		del self._TermntnDtls
		self._TermntnDtls = None

	@property
	def ApplcntReqNb(self):
		return self._ApplcntReqNb

	@ApplcntReqNb.setter
	def ApplcntReqNb(self, value):
		self._ApplcntReqNb = value if type(value) != auto else self.make_default("ApplcntReqNb")

	@ApplcntReqNb.deleter
	def ApplcntReqNb(self):
		del self._ApplcntReqNb
		self._ApplcntReqNb = None

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
	def NewUdrtkgTermsAndConds(self):
		return self._NewUdrtkgTermsAndConds

	@NewUdrtkgTermsAndConds.setter
	def NewUdrtkgTermsAndConds(self, value):
		self._NewUdrtkgTermsAndConds = value if type(value) != auto else self.make_default("NewUdrtkgTermsAndConds")

	@NewUdrtkgTermsAndConds.deleter
	def NewUdrtkgTermsAndConds(self):
		del self._NewUdrtkgTermsAndConds
		self._NewUdrtkgTermsAndConds = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def Applcnt(self):
		return self._Applcnt

	@Applcnt.setter
	def Applcnt(self, value):
		self._Applcnt = value if type(value) != auto else self.make_default("Applcnt")

	@Applcnt.deleter
	def Applcnt(self):
		del self._Applcnt
		self._Applcnt = None

	@property
	def CntrUdrtkg(self):
		return self._CntrUdrtkg

	@CntrUdrtkg.setter
	def CntrUdrtkg(self, value):
		self._CntrUdrtkg = value if type(value) != auto else self.make_default("CntrUdrtkg")

	@CntrUdrtkg.deleter
	def CntrUdrtkg(self):
		del self._CntrUdrtkg
		self._CntrUdrtkg = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if type(value) != auto else self.make_default("NewXpryDtls")

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = None

	@property
	def IncrDcrAmt(self):
		return self._IncrDcrAmt

	@IncrDcrAmt.setter
	def IncrDcrAmt(self, value):
		self._IncrDcrAmt = value if type(value) != auto else self.make_default("IncrDcrAmt")

	@IncrDcrAmt.deleter
	def IncrDcrAmt(self):
		del self._IncrDcrAmt
		self._IncrDcrAmt = None

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if type(value) != auto else self.make_default("NewBnfcry")

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDtls', type=UndertakingTermination3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplcntReqNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewUdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Applcnt', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrUdrtkg', type=Undertaking10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrDcrAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBnfcry', type=Beneficiary1, min=0, max=1, mutex_group=None, array=False),
	))

