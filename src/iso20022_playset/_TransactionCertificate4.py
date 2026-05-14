# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashAccount40 import CashAccount40
from ._CountryCode import CountryCode
from ._DocumentAmendment1 import DocumentAmendment1
from ._DocumentIdentification28 import DocumentIdentification28
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionCertificateRecord2 import TransactionCertificateRecord2

class TransactionCertificate4(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Amdmnt", "_BkAcctDmcltnCtry", "_Cert", "_CertRcrd", "_SplmtryData", "_TxId"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != base_types.auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

	@property
	def BkAcctDmcltnCtry(self):
		return self._BkAcctDmcltnCtry

	@BkAcctDmcltnCtry.setter
	def BkAcctDmcltnCtry(self, value):
		self._BkAcctDmcltnCtry = value if type(value) != base_types.auto else self.make_default("BkAcctDmcltnCtry")

	@BkAcctDmcltnCtry.deleter
	def BkAcctDmcltnCtry(self):
		del self._BkAcctDmcltnCtry
		self._BkAcctDmcltnCtry = None

	@property
	def Cert(self):
		return self._Cert

	@Cert.setter
	def Cert(self, value):
		self._Cert = value if type(value) != base_types.auto else self.make_default("Cert")

	@Cert.deleter
	def Cert(self):
		del self._Cert
		self._Cert = None

	@property
	def CertRcrd(self):
		return self._CertRcrd

	@CertRcrd.setter
	def CertRcrd(self, value):
		self._CertRcrd = value if type(value) != base_types.auto else self.make_default("CertRcrd")

	@CertRcrd.deleter
	def CertRcrd(self):
		del self._CertRcrd
		self._CertRcrd = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=DocumentAmendment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkAcctDmcltnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertRcrd', type=TransactionCertificateRecord2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))