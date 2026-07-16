# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import CountryCode
from . import DocumentAmendment1
from . import DocumentIdentification28
from . import Max35Text
from . import SupplementaryData1
from . import TransactionCertificateRecord2

class TransactionCertificate4(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Amdmnt", "_BkAcctDmcltnCtry", "_Cert", "_CertRcrd", "_SplmtryData", "_TxId"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if value is not None else base_types.UninitialisedField(self, 'Amdmnt', DocumentAmendment1, False)

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = base_types.UninitialisedField(self, 'Amdmnt', DocumentAmendment1, False)

	@property
	def BkAcctDmcltnCtry(self):
		return self._BkAcctDmcltnCtry

	@BkAcctDmcltnCtry.setter
	def BkAcctDmcltnCtry(self, value):
		self._BkAcctDmcltnCtry = value if value is not None else base_types.UninitialisedField(self, 'BkAcctDmcltnCtry', CountryCode, False)

	@BkAcctDmcltnCtry.deleter
	def BkAcctDmcltnCtry(self):
		del self._BkAcctDmcltnCtry
		self._BkAcctDmcltnCtry = base_types.UninitialisedField(self, 'BkAcctDmcltnCtry', CountryCode, False)

	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if value is not None else base_types.UninitialisedField(self, 'Cert', DocumentIdentification28, False)

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = base_types.UninitialisedField(self, 'Cert', DocumentIdentification28, False)

	@property
	def CertRcrd(self):
		return self._CertRcrd

	@CertRcrd.setter
	def CertRcrd(self, value):
		self._CertRcrd = value if value is not None else base_types.UninitialisedField(self, 'CertRcrd', TransactionCertificateRecord2, True)

	@CertRcrd.deleter
	def CertRcrd(self):
		del self._CertRcrd
		self._CertRcrd = base_types.UninitialisedField(self, 'CertRcrd', TransactionCertificateRecord2, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=DocumentAmendment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkAcctDmcltnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertRcrd', type=TransactionCertificateRecord2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))