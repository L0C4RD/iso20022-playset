# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BeneficiaryCertificationCompletion1Code
from . import BlockChainAddressWallet3
from . import FormOfSecurity1Code
from . import FundSettlementParameters25
from . import IncomePreference2Code
from . import Intermediary43
from . import Max35Text
from . import PartyIdentification139
from . import SafekeepingPlaceFormat42Choice
from . import SubAccount5
from . import YesNoIndicator

class InvestmentAccount83(base_types._BaseFieldType):

	__slots__ = ["_AcctDsgnt", "_AcctId", "_AcctNm", "_AcctSvcr", "_BlckChainAdrOrWllt", "_BnfcryCertfctnCmpltn", "_DmtrlsdInd", "_IncmPref", "_IntrmyInf", "_OwnrId", "_SctiesForm", "_SfkpgPlc", "_SttlmPtiesDtls", "_SubAcctDtls"]
	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if value is not None else base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification139, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification139, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if value is not None else base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@property
	def DmtrlsdInd(self):
		return self._DmtrlsdInd

	@DmtrlsdInd.setter
	def DmtrlsdInd(self, value):
		self._DmtrlsdInd = value if value is not None else base_types.UninitialisedField(self, 'DmtrlsdInd', YesNoIndicator, False)

	@DmtrlsdInd.deleter
	def DmtrlsdInd(self):
		del self._DmtrlsdInd
		self._DmtrlsdInd = base_types.UninitialisedField(self, 'DmtrlsdInd', YesNoIndicator, False)

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if value is not None else base_types.UninitialisedField(self, 'OwnrId', PartyIdentification139, True)

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = base_types.UninitialisedField(self, 'OwnrId', PartyIdentification139, True)

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if value is not None else base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters25, False)

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters25, False)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount5, False)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryCertfctnCmpltn', type=BeneficiaryCertificationCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OwnrId', type=PartyIdentification139, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccount5, min=0, max=1, mutex_group=None, array=False),
	))