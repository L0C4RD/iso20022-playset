from . import base_types
from .RequestedIndicator import RequestedIndicator
from .OrganisationIdentificationSchemeName1Choice import OrganisationIdentificationSchemeName1Choice

class GenericOrganisationType1(base_types._BaseFieldType):

	__slots__ = ["_Reqd", "_SchmeNm"]
	@property
	def Reqd(self):
		return self._Reqd

	@Reqd.setter
	def Reqd(self, value):
		self._Reqd = value if type(value) != base_types.auto else self.make_default("Reqd")

	@Reqd.deleter
	def Reqd(self):
		del self._Reqd
		self._Reqd = None

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if type(value) != base_types.auto else self.make_default("SchmeNm")

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Reqd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=OrganisationIdentificationSchemeName1Choice, min=1, max=1, mutex_group=None, array=False),
	))

