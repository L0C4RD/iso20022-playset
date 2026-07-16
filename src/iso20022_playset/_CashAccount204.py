# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountDesignation1Choice
from . import AccountIdentificationAndName5
from . import AccountType2Choice
from . import ActiveCurrencyCode
from . import BranchData4
from . import CashAccountType3Choice
from . import CreditDebit3Code
from . import FinancialInstitutionIdentification11Choice
from . import GenericIdentification82
from . import PartyIdentification125Choice
from . import PercentageBoundedRate
from . import SettlementInstructionReason1Choice

class CashAccount204(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctOwnrOthrId", "_AcctSvcr", "_AcctSvcrBrnch", "_CdtDbt", "_CshAcctDsgnt", "_CshAcctPurp", "_DvddPctg", "_Id", "_InvstmtAcctTp", "_SttlmCcy", "_SttlmInstrRsn"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification125Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification125Choice, False)

	@property
	def AcctOwnrOthrId(self):
		return self._AcctOwnrOthrId

	@AcctOwnrOthrId.setter
	def AcctOwnrOthrId(self, value):
		self._AcctOwnrOthrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrOthrId', GenericIdentification82, True)

	@AcctOwnrOthrId.deleter
	def AcctOwnrOthrId(self):
		del self._AcctOwnrOthrId
		self._AcctOwnrOthrId = base_types.UninitialisedField(self, 'AcctOwnrOthrId', GenericIdentification82, True)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', FinancialInstitutionIdentification11Choice, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', FinancialInstitutionIdentification11Choice, False)

	@property
	def AcctSvcrBrnch(self):
		return self._AcctSvcrBrnch

	@AcctSvcrBrnch.setter
	def AcctSvcrBrnch(self, value):
		self._AcctSvcrBrnch = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrBrnch', BranchData4, False)

	@AcctSvcrBrnch.deleter
	def AcctSvcrBrnch(self):
		del self._AcctSvcrBrnch
		self._AcctSvcrBrnch = base_types.UninitialisedField(self, 'AcctSvcrBrnch', BranchData4, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def CshAcctDsgnt(self):
		return self._CshAcctDsgnt

	@CshAcctDsgnt.setter
	def CshAcctDsgnt(self, value):
		self._CshAcctDsgnt = value if value is not None else base_types.UninitialisedField(self, 'CshAcctDsgnt', AccountDesignation1Choice, False)

	@CshAcctDsgnt.deleter
	def CshAcctDsgnt(self):
		del self._CshAcctDsgnt
		self._CshAcctDsgnt = base_types.UninitialisedField(self, 'CshAcctDsgnt', AccountDesignation1Choice, False)

	@property
	def CshAcctPurp(self):
		return self._CshAcctPurp

	@CshAcctPurp.setter
	def CshAcctPurp(self, value):
		self._CshAcctPurp = value if value is not None else base_types.UninitialisedField(self, 'CshAcctPurp', CashAccountType3Choice, False)

	@CshAcctPurp.deleter
	def CshAcctPurp(self):
		del self._CshAcctPurp
		self._CshAcctPurp = base_types.UninitialisedField(self, 'CshAcctPurp', CashAccountType3Choice, False)

	@property
	def DvddPctg(self):
		return self._DvddPctg

	@DvddPctg.setter
	def DvddPctg(self, value):
		self._DvddPctg = value if value is not None else base_types.UninitialisedField(self, 'DvddPctg', PercentageBoundedRate, False)

	@DvddPctg.deleter
	def DvddPctg(self):
		del self._DvddPctg
		self._DvddPctg = base_types.UninitialisedField(self, 'DvddPctg', PercentageBoundedRate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentificationAndName5, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentificationAndName5, False)

	@property
	def InvstmtAcctTp(self):
		return self._InvstmtAcctTp

	@InvstmtAcctTp.setter
	def InvstmtAcctTp(self, value):
		self._InvstmtAcctTp = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctTp', AccountType2Choice, False)

	@InvstmtAcctTp.deleter
	def InvstmtAcctTp(self):
		del self._InvstmtAcctTp
		self._InvstmtAcctTp = base_types.UninitialisedField(self, 'InvstmtAcctTp', AccountType2Choice, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def SttlmInstrRsn(self):
		return self._SttlmInstrRsn

	@SttlmInstrRsn.setter
	def SttlmInstrRsn(self, value):
		self._SttlmInstrRsn = value if value is not None else base_types.UninitialisedField(self, 'SttlmInstrRsn', SettlementInstructionReason1Choice, False)

	@SttlmInstrRsn.deleter
	def SttlmInstrRsn(self):
		del self._SttlmInstrRsn
		self._SttlmInstrRsn = base_types.UninitialisedField(self, 'SttlmInstrRsn', SettlementInstructionReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrOthrId', type=GenericIdentification82, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=FinancialInstitutionIdentification11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrBrnch', type=BranchData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctDsgnt', type=AccountDesignation1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctPurp', type=CashAccountType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPctg', type=PercentageBoundedRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentificationAndName5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctTp', type=AccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrRsn', type=SettlementInstructionReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))