# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ExternalEntitySize1Code
from . import ExternalEntityType1Code
from . import GenericOrganisationIdentification3
from . import IndustrySector3Choice
from . import LEIIdentifier
from . import Max500Text
from . import NPIIdentifier
from . import PartyName5

class OrganisationIdentification49(base_types._BaseFieldType):

	__slots__ = ["_AltrnOrgId", "_LEI", "_NPI", "_NttySz", "_NttyTp", "_OrgNm", "_PrsnNm", "_RegdCtry", "_Sctr"]
	@property
	def AltrnOrgId(self):
		return self._AltrnOrgId

	@AltrnOrgId.setter
	def AltrnOrgId(self, value):
		self._AltrnOrgId = value if value is not None else base_types.UninitialisedField(self, 'AltrnOrgId', GenericOrganisationIdentification3, True)

	@AltrnOrgId.deleter
	def AltrnOrgId(self):
		del self._AltrnOrgId
		self._AltrnOrgId = base_types.UninitialisedField(self, 'AltrnOrgId', GenericOrganisationIdentification3, True)

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def NPI(self):
		return self._NPI

	@NPI.setter
	def NPI(self, value):
		self._NPI = value if value is not None else base_types.UninitialisedField(self, 'NPI', NPIIdentifier, False)

	@NPI.deleter
	def NPI(self):
		del self._NPI
		self._NPI = base_types.UninitialisedField(self, 'NPI', NPIIdentifier, False)

	@property
	def NttySz(self):
		return self._NttySz

	@NttySz.setter
	def NttySz(self, value):
		self._NttySz = value if value is not None else base_types.UninitialisedField(self, 'NttySz', ExternalEntitySize1Code, False)

	@NttySz.deleter
	def NttySz(self):
		del self._NttySz
		self._NttySz = base_types.UninitialisedField(self, 'NttySz', ExternalEntitySize1Code, False)

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', ExternalEntityType1Code, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', ExternalEntityType1Code, False)

	@property
	def OrgNm(self):
		return self._OrgNm

	@OrgNm.setter
	def OrgNm(self, value):
		self._OrgNm = value if value is not None else base_types.UninitialisedField(self, 'OrgNm', PartyName5, True)

	@OrgNm.deleter
	def OrgNm(self):
		del self._OrgNm
		self._OrgNm = base_types.UninitialisedField(self, 'OrgNm', PartyName5, True)

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if value is not None else base_types.UninitialisedField(self, 'PrsnNm', Max500Text, True)

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = base_types.UninitialisedField(self, 'PrsnNm', Max500Text, True)

	@property
	def RegdCtry(self):
		return self._RegdCtry

	@RegdCtry.setter
	def RegdCtry(self, value):
		self._RegdCtry = value if value is not None else base_types.UninitialisedField(self, 'RegdCtry', CountryCode, False)

	@RegdCtry.deleter
	def RegdCtry(self):
		del self._RegdCtry
		self._RegdCtry = base_types.UninitialisedField(self, 'RegdCtry', CountryCode, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', IndustrySector3Choice, True)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', IndustrySector3Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnOrgId', type=GenericOrganisationIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NPI', type=NPIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttySz', type=ExternalEntitySize1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=ExternalEntityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgNm', type=PartyName5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrsnNm', type=Max500Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=IndustrySector3Choice, min=0, max=None, mutex_group=None, array=True),
	))