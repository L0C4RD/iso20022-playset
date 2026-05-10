from . import base_types
from ._Max350Text import Max350Text
from ._OrganisationIdentification39 import OrganisationIdentification39

class Organisation44(base_types._BaseFieldType):

	__slots__ = ["_OrgId", "_FullLglNm"]
	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if type(value) != base_types.auto else self.make_default("FullLglNm")

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=1, max=1, mutex_group=None, array=False),
	))

