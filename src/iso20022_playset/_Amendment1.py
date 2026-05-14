# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CommunicationChannel1 import CommunicationChannel1
from ._Document9 import Document9
from ._ExpiryDetails1 import ExpiryDetails1
from ._ISODate import ISODate
from ._Max2000Text import Max2000Text
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._Narrative1 import Narrative1
from ._PartyIdentification43 import PartyIdentification43
from ._Undertaking11 import Undertaking11
from ._Undertaking7 import Undertaking7
from ._UndertakingAmount2 import UndertakingAmount2
from ._UndertakingTermination3 import UndertakingTermination3
from ._YesNoIndicator import YesNoIndicator

class Amendment1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvsgPty", "_BnfcryCnsntReqInd", "_DlvryChanl", "_DtOfIssnc", "_LclUdrtkg", "_NclsdFile", "_NewBnfcry", "_NewUdrtkgTermsAndConds", "_NewXpryDtls", "_ScndAdvsgPty", "_SeqNb", "_TermntnDtls", "_UdrtkgAmtAdjstmnt", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if type(value) != base_types.auto else self.make_default("AdvsgPty")

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = None

	@property
	def BnfcryCnsntReqInd(self):
		return self._BnfcryCnsntReqInd

	@BnfcryCnsntReqInd.setter
	def BnfcryCnsntReqInd(self, value):
		self._BnfcryCnsntReqInd = value if type(value) != base_types.auto else self.make_default("BnfcryCnsntReqInd")

	@BnfcryCnsntReqInd.deleter
	def BnfcryCnsntReqInd(self):
		del self._BnfcryCnsntReqInd
		self._BnfcryCnsntReqInd = None

	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if type(value) != base_types.auto else self.make_default("DlvryChanl")

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = None

	@property
	def DtOfIssnc(self):
		return self._DtOfIssnc

	@DtOfIssnc.setter
	def DtOfIssnc(self, value):
		self._DtOfIssnc = value if type(value) != base_types.auto else self.make_default("DtOfIssnc")

	@DtOfIssnc.deleter
	def DtOfIssnc(self):
		del self._DtOfIssnc
		self._DtOfIssnc = None

	@property
	def LclUdrtkg(self):
		return self._LclUdrtkg

	@LclUdrtkg.setter
	def LclUdrtkg(self, value):
		self._LclUdrtkg = value if type(value) != base_types.auto else self.make_default("LclUdrtkg")

	@LclUdrtkg.deleter
	def LclUdrtkg(self):
		del self._LclUdrtkg
		self._LclUdrtkg = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != base_types.auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if type(value) != base_types.auto else self.make_default("NewBnfcry")

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = None

	@property
	def NewUdrtkgTermsAndConds(self):
		return self._NewUdrtkgTermsAndConds

	@NewUdrtkgTermsAndConds.setter
	def NewUdrtkgTermsAndConds(self, value):
		self._NewUdrtkgTermsAndConds = value if type(value) != base_types.auto else self.make_default("NewUdrtkgTermsAndConds")

	@NewUdrtkgTermsAndConds.deleter
	def NewUdrtkgTermsAndConds(self):
		del self._NewUdrtkgTermsAndConds
		self._NewUdrtkgTermsAndConds = None

	@property
	def NewXpryDtls(self):
		return self._NewXpryDtls

	@NewXpryDtls.setter
	def NewXpryDtls(self, value):
		self._NewXpryDtls = value if type(value) != base_types.auto else self.make_default("NewXpryDtls")

	@NewXpryDtls.deleter
	def NewXpryDtls(self):
		del self._NewXpryDtls
		self._NewXpryDtls = None

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPty")

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def TermntnDtls(self):
		return self._TermntnDtls

	@TermntnDtls.setter
	def TermntnDtls(self, value):
		self._TermntnDtls = value if type(value) != base_types.auto else self.make_default("TermntnDtls")

	@TermntnDtls.deleter
	def TermntnDtls(self):
		del self._TermntnDtls
		self._TermntnDtls = None

	@property
	def UdrtkgAmtAdjstmnt(self):
		return self._UdrtkgAmtAdjstmnt

	@UdrtkgAmtAdjstmnt.setter
	def UdrtkgAmtAdjstmnt(self, value):
		self._UdrtkgAmtAdjstmnt = value if type(value) != base_types.auto else self.make_default("UdrtkgAmtAdjstmnt")

	@UdrtkgAmtAdjstmnt.deleter
	def UdrtkgAmtAdjstmnt(self):
		del self._UdrtkgAmtAdjstmnt
		self._UdrtkgAmtAdjstmnt = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

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