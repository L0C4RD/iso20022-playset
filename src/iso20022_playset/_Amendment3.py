# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Beneficiary1
from . import CommunicationChannel1
from . import Document9
from . import ExpiryDetails2
from . import Max2000Text
from . import Max35Text
from . import Narrative1
from . import PartyIdentification43
from . import Undertaking10
from . import Undertaking9
from . import UndertakingAmount2
from . import UndertakingTermination3

class Amendment3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Applcnt", "_ApplcntReqNb", "_CntrUdrtkg", "_DlvryChanl", "_IncrDcrAmt", "_NclsdFile", "_NewBnfcry", "_NewUdrtkgTermsAndConds", "_NewXpryDtls", "_TermntnDtls", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def Applcnt(self):
		return self._Applcnt

	@Applcnt.setter
	def Applcnt(self, value):
		self._Applcnt = value if value is not None else base_types.UninitialisedField(self, 'Applcnt', PartyIdentification43, False)

	@Applcnt.deleter
	def Applcnt(self):
		del self._Applcnt
		self._Applcnt = base_types.UninitialisedField(self, 'Applcnt', PartyIdentification43, False)

	@property
	def ApplcntReqNb(self):
		return self._ApplcntReqNb

	@ApplcntReqNb.setter
	def ApplcntReqNb(self, value):
		self._ApplcntReqNb = value if value is not None else base_types.UninitialisedField(self, 'ApplcntReqNb', Max35Text, False)

	@ApplcntReqNb.deleter
	def ApplcntReqNb(self):
		del self._ApplcntReqNb
		self._ApplcntReqNb = base_types.UninitialisedField(self, 'ApplcntReqNb', Max35Text, False)

	@property
	def CntrUdrtkg(self):
		return self._CntrUdrtkg

	@CntrUdrtkg.setter
	def CntrUdrtkg(self, value):
		self._CntrUdrtkg = value if value is not None else base_types.UninitialisedField(self, 'CntrUdrtkg', Undertaking10, False)

	@CntrUdrtkg.deleter
	def CntrUdrtkg(self):
		del self._CntrUdrtkg
		self._CntrUdrtkg = base_types.UninitialisedField(self, 'CntrUdrtkg', Undertaking10, False)

	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if value is not None else base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@property
	def IncrDcrAmt(self):
		return self._IncrDcrAmt

	@IncrDcrAmt.setter
	def IncrDcrAmt(self, value):
		self._IncrDcrAmt = value if value is not None else base_types.UninitialisedField(self, 'IncrDcrAmt', UndertakingAmount2, False)

	@IncrDcrAmt.deleter
	def IncrDcrAmt(self):
		del self._IncrDcrAmt
		self._IncrDcrAmt = base_types.UninitialisedField(self, 'IncrDcrAmt', UndertakingAmount2, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if value is not None else base_types.UninitialisedField(self, 'NewBnfcry', Beneficiary1, False)

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = base_types.UninitialisedField(self, 'NewBnfcry', Beneficiary1, False)

	@property
	def NewUdrtkgTermsAndConds(self):
		return self._NewUdrtkgTermsAndConds

	@NewUdrtkgTermsAndConds.setter
	def NewUdrtkgTermsAndConds(self, value):
		self._NewUdrtkgTermsAndConds = value if value is not None else base_types.UninitialisedField(self, 'NewUdrtkgTermsAndConds', Narrative1, True)

	@NewUdrtkgTermsAndConds.deleter
	def NewUdrtkgTermsAndConds(self):
		del self._NewUdrtkgTermsAndConds
		self._NewUdrtkgTermsAndConds = base_types.UninitialisedField(self, 'NewUdrtkgTermsAndConds', Narrative1, True)

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if value is not None else base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails2, False)

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails2, False)

	@property
	def TermntnDtls(self):
		return self._TermntnDtls

	@TermntnDtls.setter
	def TermntnDtls(self, value):
		self._TermntnDtls = value if value is not None else base_types.UninitialisedField(self, 'TermntnDtls', UndertakingTermination3, False)

	@TermntnDtls.deleter
	def TermntnDtls(self):
		del self._TermntnDtls
		self._TermntnDtls = base_types.UninitialisedField(self, 'TermntnDtls', UndertakingTermination3, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Applcnt', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplcntReqNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrUdrtkg', type=Undertaking10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrDcrAmt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewBnfcry', type=Beneficiary1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDtls', type=UndertakingTermination3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))