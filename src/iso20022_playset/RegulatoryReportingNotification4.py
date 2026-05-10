from . import base_types
import TransactionCertificate4
import PartyIdentification272
import Max35Text
import BranchAndFinancialInstitutionIdentification8

class RegulatoryReportingNotification4(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_TxCert", "_AcctSvcr", "_TxNtfctnId"]
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
	def TxCert(self):
		return self._TxCert

	@TxCert.setter
	def TxCert(self, value):
		self._TxCert = value if type(value) != auto else self.make_default("TxCert")

	@TxCert.deleter
	def TxCert(self):
		del self._TxCert
		self._TxCert = None

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
	def TxNtfctnId(self):
		return self._TxNtfctnId

	@TxNtfctnId.setter
	def TxNtfctnId(self, value):
		self._TxNtfctnId = value if type(value) != auto else self.make_default("TxNtfctnId")

	@TxNtfctnId.deleter
	def TxNtfctnId(self):
		del self._TxNtfctnId
		self._TxNtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCert', type=TransactionCertificate4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

