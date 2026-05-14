# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ContractDocument1 import ContractDocument1
from ._CustomerAccount4 import CustomerAccount4
from ._OrganisationIdentification39 import OrganisationIdentification39
from ._PartyAndSignature4 import PartyAndSignature4
from ._References3 import References3
from ._SupplementaryData1 import SupplementaryData1

class AccountOpeningAdditionalInformationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctSvcrId", "_DgtlSgntr", "_Fr", "_OrgId", "_Refs", "_SplmtryData", "_UndrlygMstrAgrmt"]
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
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if type(value) != base_types.auto else self.make_default("AcctSvcrId")

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != base_types.auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != base_types.auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

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
	def UndrlygMstrAgrmt(self):
		return self._UndrlygMstrAgrmt

	@UndrlygMstrAgrmt.setter
	def UndrlygMstrAgrmt(self, value):
		self._UndrlygMstrAgrmt = value if type(value) != base_types.auto else self.make_default("UndrlygMstrAgrmt")

	@UndrlygMstrAgrmt.deleter
	def UndrlygMstrAgrmt(self):
		del self._UndrlygMstrAgrmt
		self._UndrlygMstrAgrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CustomerAccount4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fr', type=OrganisationIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygMstrAgrmt', type=ContractDocument1, min=0, max=1, mutex_group=None, array=False),
	))