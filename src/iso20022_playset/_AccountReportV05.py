# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountReport36
from . import BranchAndFinancialInstitutionIdentification8
from . import Organisation42
from . import OrganisationIdentification39
from . import PartyAndSignature4
from . import References5
from . import SupplementaryData1

class AccountReportV05(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrId", "_DgtlSgntr", "_Fr", "_Org", "_Refs", "_Rpt", "_SplmtryData"]
	@property
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = base_types.UninitialisedField(self, 'AcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, True)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, True)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', OrganisationIdentification39, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', OrganisationIdentification39, False)

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if value is not None else base_types.UninitialisedField(self, 'Org', Organisation42, False)

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = base_types.UninitialisedField(self, 'Org', Organisation42, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', References5, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', References5, False)

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if value is not None else base_types.UninitialisedField(self, 'Rpt', AccountReport36, True)

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = base_types.UninitialisedField(self, 'Rpt', AccountReport36, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fr', type=OrganisationIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Org', type=Organisation42, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=AccountReport36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))