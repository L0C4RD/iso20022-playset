# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ContractRegistrationReference2Choice
from . import DocumentAmendment1
from . import DocumentIdentification28
from . import Max35Text
from . import PartyIdentification272
from . import SupplementaryData1
from . import SupportingDocumentEntry2

class SupportingDocument4(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Amdmnt", "_Cert", "_CtrctRef", "_Ntry", "_OrgnlReqId", "_SplmtryData", "_SpprtgDocId"]
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
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if value is not None else base_types.UninitialisedField(self, 'CtrctRef', ContractRegistrationReference2Choice, False)

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = base_types.UninitialisedField(self, 'CtrctRef', ContractRegistrationReference2Choice, False)

	@property
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if value is not None else base_types.UninitialisedField(self, 'Ntry', SupportingDocumentEntry2, True)

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = base_types.UninitialisedField(self, 'Ntry', SupportingDocumentEntry2, True)

	@property
	def OrgnlReqId(self):
		return self._OrgnlReqId

	@OrgnlReqId.setter
	def OrgnlReqId(self, value):
		self._OrgnlReqId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlReqId', Max35Text, False)

	@OrgnlReqId.deleter
	def OrgnlReqId(self):
		del self._OrgnlReqId
		self._OrgnlReqId = base_types.UninitialisedField(self, 'OrgnlReqId', Max35Text, False)

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
	def SpprtgDocId(self):
		return self._SpprtgDocId

	@SpprtgDocId.setter
	def SpprtgDocId(self, value):
		self._SpprtgDocId = value if value is not None else base_types.UninitialisedField(self, 'SpprtgDocId', Max35Text, False)

	@SpprtgDocId.deleter
	def SpprtgDocId(self):
		del self._SpprtgDocId
		self._SpprtgDocId = base_types.UninitialisedField(self, 'SpprtgDocId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amdmnt', type=DocumentAmendment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cert', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRef', type=ContractRegistrationReference2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntry', type=SupportingDocumentEntry2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpprtgDocId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))