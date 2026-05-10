from . import base_types
from .ExternalTypeOfParty1Code import ExternalTypeOfParty1Code
from .Max2000Text import Max2000Text
from .PartyIdentification43 import PartyIdentification43
from .UndertakingName1Code import UndertakingName1Code
from .ExpiryDetails2 import ExpiryDetails2
from .UndertakingAmount1 import UndertakingAmount1
from .YesNoIndicator import YesNoIndicator
from .GovernanceRules1 import GovernanceRules1

class Undertaking2(base_types._BaseFieldType):

	__slots__ = ["_CntrUdrtkgAmt", "_StdClmDocInd", "_ConfChrgsPyblBy", "_GovncRulesAndLaw", "_Bnfcry", "_XpryDtls", "_Nm", "_AddtlInf"]
	@property
	def CntrUdrtkgAmt(self):
		return self._CntrUdrtkgAmt

	@CntrUdrtkgAmt.setter
	def CntrUdrtkgAmt(self, value):
		self._CntrUdrtkgAmt = value if type(value) != base_types.auto else self.make_default("CntrUdrtkgAmt")

	@CntrUdrtkgAmt.deleter
	def CntrUdrtkgAmt(self):
		del self._CntrUdrtkgAmt
		self._CntrUdrtkgAmt = None

	@property
	def StdClmDocInd(self):
		return self._StdClmDocInd

	@StdClmDocInd.setter
	def StdClmDocInd(self, value):
		self._StdClmDocInd = value if type(value) != base_types.auto else self.make_default("StdClmDocInd")

	@StdClmDocInd.deleter
	def StdClmDocInd(self):
		del self._StdClmDocInd
		self._StdClmDocInd = None

	@property
	def ConfChrgsPyblBy(self):
		return self._ConfChrgsPyblBy

	@ConfChrgsPyblBy.setter
	def ConfChrgsPyblBy(self, value):
		self._ConfChrgsPyblBy = value if type(value) != base_types.auto else self.make_default("ConfChrgsPyblBy")

	@ConfChrgsPyblBy.deleter
	def ConfChrgsPyblBy(self):
		del self._ConfChrgsPyblBy
		self._ConfChrgsPyblBy = None

	@property
	def GovncRulesAndLaw(self):
		return self._GovncRulesAndLaw

	@GovncRulesAndLaw.setter
	def GovncRulesAndLaw(self, value):
		self._GovncRulesAndLaw = value if type(value) != base_types.auto else self.make_default("GovncRulesAndLaw")

	@GovncRulesAndLaw.deleter
	def GovncRulesAndLaw(self):
		del self._GovncRulesAndLaw
		self._GovncRulesAndLaw = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != base_types.auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def XpryDtls(self):
		return self._XpryDtls

	@XpryDtls.setter
	def XpryDtls(self, value):
		self._XpryDtls = value if type(value) != base_types.auto else self.make_default("XpryDtls")

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrUdrtkgAmt', type=UndertakingAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdClmDocInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovncRulesAndLaw', type=GovernanceRules1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtls', type=ExpiryDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=UndertakingName1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

