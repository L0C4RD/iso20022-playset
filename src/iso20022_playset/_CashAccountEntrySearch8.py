# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationSearchCriteria2Choice
from . import ActiveOrHistoricAmountRange2Choice
from . import ActiveOrHistoricCurrencyCode
from . import BranchAndFinancialInstitutionIdentification8
from . import CreditDebitCode
from . import DateAndDateTimeSearch3Choice
from . import EntryStatus1Code
from . import PartyIdentification272

class CashAccountEntrySearch8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_AcctSvcr", "_CdtDbtInd", "_NtryAmt", "_NtryAmtCcy", "_NtryDt", "_NtrySts"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentificationSearchCriteria2Choice, True)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentificationSearchCriteria2Choice, True)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification272, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification272, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def NtryAmt(self):
		return self._NtryAmt

	@NtryAmt.setter
	def NtryAmt(self, value):
		self._NtryAmt = value if value is not None else base_types.UninitialisedField(self, 'NtryAmt', ActiveOrHistoricAmountRange2Choice, True)

	@NtryAmt.deleter
	def NtryAmt(self):
		del self._NtryAmt
		self._NtryAmt = base_types.UninitialisedField(self, 'NtryAmt', ActiveOrHistoricAmountRange2Choice, True)

	@property
	def NtryAmtCcy(self):
		return self._NtryAmtCcy

	@NtryAmtCcy.setter
	def NtryAmtCcy(self, value):
		self._NtryAmtCcy = value if value is not None else base_types.UninitialisedField(self, 'NtryAmtCcy', ActiveOrHistoricCurrencyCode, True)

	@NtryAmtCcy.deleter
	def NtryAmtCcy(self):
		del self._NtryAmtCcy
		self._NtryAmtCcy = base_types.UninitialisedField(self, 'NtryAmtCcy', ActiveOrHistoricCurrencyCode, True)

	@property
	def NtryDt(self):
		return self._NtryDt

	@NtryDt.setter
	def NtryDt(self, value):
		self._NtryDt = value if value is not None else base_types.UninitialisedField(self, 'NtryDt', DateAndDateTimeSearch3Choice, True)

	@NtryDt.deleter
	def NtryDt(self):
		del self._NtryDt
		self._NtryDt = base_types.UninitialisedField(self, 'NtryDt', DateAndDateTimeSearch3Choice, True)

	@property
	def NtrySts(self):
		return self._NtrySts

	@NtrySts.setter
	def NtrySts(self, value):
		self._NtrySts = value if value is not None else base_types.UninitialisedField(self, 'NtrySts', EntryStatus1Code, True)

	@NtrySts.deleter
	def NtrySts(self):
		del self._NtrySts
		self._NtrySts = base_types.UninitialisedField(self, 'NtrySts', EntryStatus1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryAmt', type=ActiveOrHistoricAmountRange2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryDt', type=DateAndDateTimeSearch3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtrySts', type=EntryStatus1Code, min=0, max=None, mutex_group=None, array=True),
	))