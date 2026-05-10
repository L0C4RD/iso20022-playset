import base_types
import CreditDebitCode
import PartyIdentification272
import EntryStatus1Code
import ActiveOrHistoricAmountRange2Choice
import AccountIdentificationSearchCriteria2Choice
import ActiveOrHistoricCurrencyCode
import DateAndDateTimeSearch3Choice
import BranchAndFinancialInstitutionIdentification8

class CashAccountEntrySearch8(base_types._BaseFieldType):

	__slots__ = ["_NtryDt", "_NtryAmtCcy", "_AcctSvcr", "_NtrySts", "_NtryAmt", "_CdtDbtInd", "_AcctId", "_AcctOwnr"]
	@property
	def NtryDt(self):
		return self._NtryDt

	@NtryDt.setter
	def NtryDt(self, value):
		self._NtryDt = value if type(value) != auto else self.make_default("NtryDt")

	@NtryDt.deleter
	def NtryDt(self):
		del self._NtryDt
		self._NtryDt = None

	@property
	def NtryAmtCcy(self):
		return self._NtryAmtCcy

	@NtryAmtCcy.setter
	def NtryAmtCcy(self, value):
		self._NtryAmtCcy = value if type(value) != auto else self.make_default("NtryAmtCcy")

	@NtryAmtCcy.deleter
	def NtryAmtCcy(self):
		del self._NtryAmtCcy
		self._NtryAmtCcy = None

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
	def NtrySts(self):
		return self._NtrySts

	@NtrySts.setter
	def NtrySts(self, value):
		self._NtrySts = value if type(value) != auto else self.make_default("NtrySts")

	@NtrySts.deleter
	def NtrySts(self):
		del self._NtrySts
		self._NtrySts = None

	@property
	def NtryAmt(self):
		return self._NtryAmt

	@NtryAmt.setter
	def NtryAmt(self, value):
		self._NtryAmt = value if type(value) != auto else self.make_default("NtryAmt")

	@NtryAmt.deleter
	def NtryAmt(self):
		del self._NtryAmt
		self._NtryAmt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtryDt', type=DateAndDateTimeSearch3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtrySts', type=EntryStatus1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryAmt', type=ActiveOrHistoricAmountRange2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))

