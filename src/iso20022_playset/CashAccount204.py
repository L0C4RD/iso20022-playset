import base_types
import SettlementInstructionReason1Choice
import ActiveCurrencyCode
import CashAccountType3Choice
import PercentageBoundedRate
import PartyIdentification125Choice
import AccountIdentificationAndName5
import AccountDesignation1Choice
import FinancialInstitutionIdentification11Choice
import AccountType2Choice
import CreditDebit3Code
import GenericIdentification82
import BranchData4

class CashAccount204(base_types._BaseFieldType):

	__slots__ = ["_CdtDbt", "_InvstmtAcctTp", "_CshAcctDsgnt", "_CshAcctPurp", "_AcctOwnrOthrId", "_DvddPctg", "_AcctSvcr", "_AcctOwnr", "_AcctSvcrBrnch", "_Id", "_SttlmInstrRsn", "_SttlmCcy"]
	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def InvstmtAcctTp(self):
		return self._InvstmtAcctTp

	@InvstmtAcctTp.setter
	def InvstmtAcctTp(self, value):
		self._InvstmtAcctTp = value if type(value) != auto else self.make_default("InvstmtAcctTp")

	@InvstmtAcctTp.deleter
	def InvstmtAcctTp(self):
		del self._InvstmtAcctTp
		self._InvstmtAcctTp = None

	@property
	def CshAcctDsgnt(self):
		return self._CshAcctDsgnt

	@CshAcctDsgnt.setter
	def CshAcctDsgnt(self, value):
		self._CshAcctDsgnt = value if type(value) != auto else self.make_default("CshAcctDsgnt")

	@CshAcctDsgnt.deleter
	def CshAcctDsgnt(self):
		del self._CshAcctDsgnt
		self._CshAcctDsgnt = None

	@property
	def CshAcctPurp(self):
		return self._CshAcctPurp

	@CshAcctPurp.setter
	def CshAcctPurp(self, value):
		self._CshAcctPurp = value if type(value) != auto else self.make_default("CshAcctPurp")

	@CshAcctPurp.deleter
	def CshAcctPurp(self):
		del self._CshAcctPurp
		self._CshAcctPurp = None

	@property
	def AcctOwnrOthrId(self):
		return self._AcctOwnrOthrId

	@AcctOwnrOthrId.setter
	def AcctOwnrOthrId(self, value):
		self._AcctOwnrOthrId = value if type(value) != auto else self.make_default("AcctOwnrOthrId")

	@AcctOwnrOthrId.deleter
	def AcctOwnrOthrId(self):
		del self._AcctOwnrOthrId
		self._AcctOwnrOthrId = None

	@property
	def DvddPctg(self):
		return self._DvddPctg

	@DvddPctg.setter
	def DvddPctg(self, value):
		self._DvddPctg = value if type(value) != auto else self.make_default("DvddPctg")

	@DvddPctg.deleter
	def DvddPctg(self):
		del self._DvddPctg
		self._DvddPctg = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctSvcrBrnch(self):
		return self._AcctSvcrBrnch

	@AcctSvcrBrnch.setter
	def AcctSvcrBrnch(self, value):
		self._AcctSvcrBrnch = value if type(value) != auto else self.make_default("AcctSvcrBrnch")

	@AcctSvcrBrnch.deleter
	def AcctSvcrBrnch(self):
		del self._AcctSvcrBrnch
		self._AcctSvcrBrnch = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def SttlmInstrRsn(self):
		return self._SttlmInstrRsn

	@SttlmInstrRsn.setter
	def SttlmInstrRsn(self, value):
		self._SttlmInstrRsn = value if type(value) != auto else self.make_default("SttlmInstrRsn")

	@SttlmInstrRsn.deleter
	def SttlmInstrRsn(self):
		del self._SttlmInstrRsn
		self._SttlmInstrRsn = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctTp', type=AccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctDsgnt', type=AccountDesignation1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctPurp', type=CashAccountType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrOthrId', type=GenericIdentification82, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvddPctg', type=PercentageBoundedRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=FinancialInstitutionIdentification11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrBrnch', type=BranchData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentificationAndName5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrRsn', type=SettlementInstructionReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

