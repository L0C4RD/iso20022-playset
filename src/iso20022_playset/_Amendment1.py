# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationChannel1
from . import Document9
from . import ExpiryDetails1
from . import ISODate
from . import Max2000Text
from . import Max4AlphaNumericText
from . import Narrative1
from . import PartyIdentification43
from . import Undertaking11
from . import Undertaking7
from . import UndertakingAmount2
from . import UndertakingTermination3
from . import YesNoIndicator

class Amendment1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvsgPty", "_BnfcryCnsntReqInd", "_DlvryChanl", "_DtOfIssnc", "_LclUdrtkg", "_NclsdFile", "_NewBnfcry", "_NewUdrtkgTermsAndConds", "_NewXpryDtls", "_ScndAdvsgPty", "_SeqNb", "_TermntnDtls", "_UdrtkgAmtAdjstmnt", "_UdrtkgId"]
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
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@property
	def BnfcryCnsntReqInd(self):
		return self._BnfcryCnsntReqInd

	@BnfcryCnsntReqInd.setter
	def BnfcryCnsntReqInd(self, value):
		self._BnfcryCnsntReqInd = value if value is not None else base_types.UninitialisedField(self, 'BnfcryCnsntReqInd', YesNoIndicator, False)

	@BnfcryCnsntReqInd.deleter
	def BnfcryCnsntReqInd(self):
		del self._BnfcryCnsntReqInd
		self._BnfcryCnsntReqInd = base_types.UninitialisedField(self, 'BnfcryCnsntReqInd', YesNoIndicator, False)

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
	def DtOfIssnc(self):
		return self._DtOfIssnc

	@DtOfIssnc.setter
	def DtOfIssnc(self, value):
		self._DtOfIssnc = value if value is not None else base_types.UninitialisedField(self, 'DtOfIssnc', ISODate, False)

	@DtOfIssnc.deleter
	def DtOfIssnc(self):
		del self._DtOfIssnc
		self._DtOfIssnc = base_types.UninitialisedField(self, 'DtOfIssnc', ISODate, False)

	@property
	def LclUdrtkg(self):
		return self._LclUdrtkg

	@LclUdrtkg.setter
	def LclUdrtkg(self, value):
		self._LclUdrtkg = value if value is not None else base_types.UninitialisedField(self, 'LclUdrtkg', Undertaking11, False)

	@LclUdrtkg.deleter
	def LclUdrtkg(self):
		del self._LclUdrtkg
		self._LclUdrtkg = base_types.UninitialisedField(self, 'LclUdrtkg', Undertaking11, False)

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
		self._NewBnfcry = value if value is not None else base_types.UninitialisedField(self, 'NewBnfcry', PartyIdentification43, False)

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = base_types.UninitialisedField(self, 'NewBnfcry', PartyIdentification43, False)

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
		self._NewXpryDtls = value if value is not None else base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = base_types.UninitialisedField(self, 'NewXpryDtls', ExpiryDetails1, False)

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Max4AlphaNumericText, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Max4AlphaNumericText, False)

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
	def UdrtkgAmtAdjstmnt(self):
		return self._UdrtkgAmtAdjstmnt

	@UdrtkgAmtAdjstmnt.setter
	def UdrtkgAmtAdjstmnt(self, value):
		self._UdrtkgAmtAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmtAdjstmnt', UndertakingAmount2, False)

	@UdrtkgAmtAdjstmnt.deleter
	def UdrtkgAmtAdjstmnt(self):
		del self._UdrtkgAmtAdjstmnt
		self._UdrtkgAmtAdjstmnt = base_types.UninitialisedField(self, 'UdrtkgAmtAdjstmnt', UndertakingAmount2, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking7, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryCnsntReqInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfIssnc', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclUdrtkg', type=Undertaking11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewBnfcry', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUdrtkgTermsAndConds', type=Narrative1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewXpryDtls', type=ExpiryDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDtls', type=UndertakingTermination3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmtAdjstmnt', type=UndertakingAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking7, min=1, max=1, mutex_group=None, array=False),
	))