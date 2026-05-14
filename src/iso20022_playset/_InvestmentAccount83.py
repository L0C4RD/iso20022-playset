# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BeneficiaryCertificationCompletion1Code import BeneficiaryCertificationCompletion1Code
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._FormOfSecurity1Code import FormOfSecurity1Code
from ._FundSettlementParameters25 import FundSettlementParameters25
from ._IncomePreference2Code import IncomePreference2Code
from ._Intermediary43 import Intermediary43
from ._Max35Text import Max35Text
from ._PartyIdentification139 import PartyIdentification139
from ._SafekeepingPlaceFormat42Choice import SafekeepingPlaceFormat42Choice
from ._SubAccount5 import SubAccount5
from ._YesNoIndicator import YesNoIndicator

class InvestmentAccount83(base_types._BaseFieldType):

	__slots__ = ["_AcctDsgnt", "_AcctId", "_AcctNm", "_AcctSvcr", "_BlckChainAdrOrWllt", "_BnfcryCertfctnCmpltn", "_DmtrlsdInd", "_IncmPref", "_IntrmyInf", "_OwnrId", "_SctiesForm", "_SfkpgPlc", "_SttlmPtiesDtls", "_SubAcctDtls"]
	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if type(value) != base_types.auto else self.make_default("AcctDsgnt")

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != base_types.auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if type(value) != base_types.auto else self.make_default("BnfcryCertfctnCmpltn")

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = None

	@property
	def DmtrlsdInd(self):
		return self._DmtrlsdInd

	@DmtrlsdInd.setter
	def DmtrlsdInd(self, value):
		self._DmtrlsdInd = value if type(value) != base_types.auto else self.make_default("DmtrlsdInd")

	@DmtrlsdInd.deleter
	def DmtrlsdInd(self):
		del self._DmtrlsdInd
		self._DmtrlsdInd = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != base_types.auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != base_types.auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if type(value) != base_types.auto else self.make_default("OwnrId")

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = None

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != base_types.auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if type(value) != base_types.auto else self.make_default("SttlmPtiesDtls")

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = None

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if type(value) != base_types.auto else self.make_default("SubAcctDtls")

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = None

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