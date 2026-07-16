# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExpiryDetails2
from . import ExternalTypeOfParty1Code
from . import GovernanceRules1
from . import Max2000Text
from . import PartyIdentification43
from . import UndertakingAmount1
from . import UndertakingName1Code
from . import YesNoIndicator

class Undertaking2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Bnfcry", "_CntrUdrtkgAmt", "_ConfChrgsPyblBy", "_GovncRulesAndLaw", "_Nm", "_StdClmDocInd", "_XpryDtls"]
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
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification43, False)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification43, False)

	@property
	def CntrUdrtkgAmt(self):
		return self._CntrUdrtkgAmt

	@CntrUdrtkgAmt.setter
	def CntrUdrtkgAmt(self, value):
		self._CntrUdrtkgAmt = value if value is not None else base_types.UninitialisedField(self, 'CntrUdrtkgAmt', UndertakingAmount1, False)

	@CntrUdrtkgAmt.deleter
	def CntrUdrtkgAmt(self):
		del self._CntrUdrtkgAmt
		self._CntrUdrtkgAmt = base_types.UninitialisedField(self, 'CntrUdrtkgAmt', UndertakingAmount1, False)

	@property
	def ConfChrgsPyblBy(self):
		return self._ConfChrgsPyblBy

	@ConfChrgsPyblBy.setter
	def ConfChrgsPyblBy(self, value):
		self._ConfChrgsPyblBy = value if value is not None else base_types.UninitialisedField(self, 'ConfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@ConfChrgsPyblBy.deleter
	def ConfChrgsPyblBy(self):
		del self._ConfChrgsPyblBy
		self._ConfChrgsPyblBy = base_types.UninitialisedField(self, 'ConfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@property
	def GovncRulesAndLaw(self):
		return self._GovncRulesAndLaw

	@GovncRulesAndLaw.setter
	def GovncRulesAndLaw(self, value):
		self._GovncRulesAndLaw = value if value is not None else base_types.UninitialisedField(self, 'GovncRulesAndLaw', GovernanceRules1, False)

	@GovncRulesAndLaw.deleter
	def GovncRulesAndLaw(self):
		del self._GovncRulesAndLaw
		self._GovncRulesAndLaw = base_types.UninitialisedField(self, 'GovncRulesAndLaw', GovernanceRules1, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', UndertakingName1Code, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', UndertakingName1Code, False)

	@property
	def StdClmDocInd(self):
		return self._StdClmDocInd

	@StdClmDocInd.setter
	def StdClmDocInd(self, value):
		self._StdClmDocInd = value if value is not None else base_types.UninitialisedField(self, 'StdClmDocInd', YesNoIndicator, False)

	@StdClmDocInd.deleter
	def StdClmDocInd(self):
		del self._StdClmDocInd
		self._StdClmDocInd = base_types.UninitialisedField(self, 'StdClmDocInd', YesNoIndicator, False)

	@property
	def XpryDtls(self):
		return self._XpryDtls

	@XpryDtls.setter
	def XpryDtls(self, value):
		self._XpryDtls = value if value is not None else base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails2, False)

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrUdrtkgAmt', type=UndertakingAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovncRulesAndLaw', type=GovernanceRules1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=UndertakingName1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdClmDocInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtls', type=ExpiryDetails2, min=0, max=1, mutex_group=None, array=False),
	))