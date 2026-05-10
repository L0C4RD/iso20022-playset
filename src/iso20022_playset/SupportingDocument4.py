from . import base_types
from .ContractRegistrationReference2Choice import ContractRegistrationReference2Choice
from .SupplementaryData1 import SupplementaryData1
from .PartyIdentification272 import PartyIdentification272
from .DocumentAmendment1 import DocumentAmendment1
from .Max35Text import Max35Text
from .SupportingDocumentEntry2 import SupportingDocumentEntry2
from .DocumentIdentification28 import DocumentIdentification28
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class SupportingDocument4(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_AcctSvcr", "_Ntry", "_SpprtgDocId", "_AcctOwnr", "_OrgnlReqId", "_CtrctRef", "_Cert", "_Amdmnt"]
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
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if type(value) != base_types.auto else self.make_default("Ntry")

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = None

	@property
	def SpprtgDocId(self):
		return self._SpprtgDocId

	@SpprtgDocId.setter
	def SpprtgDocId(self, value):
		self._SpprtgDocId = value if type(value) != base_types.auto else self.make_default("SpprtgDocId")

	@SpprtgDocId.deleter
	def SpprtgDocId(self):
		del self._SpprtgDocId
		self._SpprtgDocId = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def OrgnlReqId(self):
		return self._OrgnlReqId

	@OrgnlReqId.setter
	def OrgnlReqId(self, value):
		self._OrgnlReqId = value if type(value) != base_types.auto else self.make_default("OrgnlReqId")

	@OrgnlReqId.deleter
	def OrgnlReqId(self):
		del self._OrgnlReqId
		self._OrgnlReqId = None

	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if type(value) != base_types.auto else self.make_default("CtrctRef")

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = None

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
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != base_types.auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntry', type=SupportingDocumentEntry2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpprtgDocId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRef', type=ContractRegistrationReference2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=DocumentAmendment1, min=0, max=1, mutex_group=None, array=False),
	))

