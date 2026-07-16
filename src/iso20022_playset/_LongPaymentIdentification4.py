# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import EntryTypeIdentifier
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import PaymentOrigin1Choice
from . import UUIDv4Identifier

class LongPaymentIdentification4(base_types._BaseFieldType):

	__slots__ = ["_EndToEndId", "_InstdAgt", "_InstgAgt", "_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_NtryTp", "_PmtMtd", "_TxId", "_UETR"]
	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if value is not None else base_types.UninitialisedField(self, 'EndToEndId', Max35Text, False)

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = base_types.UninitialisedField(self, 'EndToEndId', Max35Text, False)

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ImpliedCurrencyAndAmount, False)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ImpliedCurrencyAndAmount, False)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@property
	def NtryTp(self):
		return self._NtryTp

	@NtryTp.setter
	def NtryTp(self, value):
		self._NtryTp = value if value is not None else base_types.UninitialisedField(self, 'NtryTp', EntryTypeIdentifier, False)

	@NtryTp.deleter
	def NtryTp(self):
		del self._NtryTp
		self._NtryTp = base_types.UninitialisedField(self, 'NtryTp', EntryTypeIdentifier, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryTp', type=EntryTypeIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))