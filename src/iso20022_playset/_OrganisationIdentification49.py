from . import base_types
from ._CountryCode import CountryCode
from ._ExternalEntitySize1Code import ExternalEntitySize1Code
from ._ExternalEntityType1Code import ExternalEntityType1Code
from ._GenericOrganisationIdentification3 import GenericOrganisationIdentification3
from ._IndustrySector3Choice import IndustrySector3Choice
from ._LEIIdentifier import LEIIdentifier
from ._Max500Text import Max500Text
from ._NPIIdentifier import NPIIdentifier
from ._PartyName5 import PartyName5

class OrganisationIdentification49(base_types._BaseFieldType):

	__slots__ = ["_AltrnOrgId", "_LEI", "_NPI", "_NttySz", "_NttyTp", "_OrgNm", "_PrsnNm", "_RegdCtry", "_Sctr"]
	@property
	def AltrnOrgId(self):
		return self._AltrnOrgId

	@AltrnOrgId.setter
	def AltrnOrgId(self, value):
		self._AltrnOrgId = value if type(value) != base_types.auto else self.make_default("AltrnOrgId")

	@AltrnOrgId.deleter
	def AltrnOrgId(self):
		del self._AltrnOrgId
		self._AltrnOrgId = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def NPI(self):
		return self._NPI

	@NPI.setter
	def NPI(self, value):
		self._NPI = value if type(value) != base_types.auto else self.make_default("NPI")

	@NPI.deleter
	def NPI(self):
		del self._NPI
		self._NPI = None

	@property
	def NttySz(self):
		return self._NttySz

	@NttySz.setter
	def NttySz(self, value):
		self._NttySz = value if type(value) != base_types.auto else self.make_default("NttySz")

	@NttySz.deleter
	def NttySz(self):
		del self._NttySz
		self._NttySz = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != base_types.auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

	@property
	def OrgNm(self):
		return self._OrgNm

	@OrgNm.setter
	def OrgNm(self, value):
		self._OrgNm = value if type(value) != base_types.auto else self.make_default("OrgNm")

	@OrgNm.deleter
	def OrgNm(self):
		del self._OrgNm
		self._OrgNm = None

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if type(value) != base_types.auto else self.make_default("PrsnNm")

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = None

	@property
	def RegdCtry(self):
		return self._RegdCtry

	@RegdCtry.setter
	def RegdCtry(self, value):
		self._RegdCtry = value if type(value) != base_types.auto else self.make_default("RegdCtry")

	@RegdCtry.deleter
	def RegdCtry(self):
		del self._RegdCtry
		self._RegdCtry = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

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

