from . import base_types
from ._OrganisationType2 import OrganisationType2
from ._PersonType2 import PersonType2
from ._RequestedIndicator import RequestedIndicator

class CustomerTypeRequest2(base_types._BaseFieldType):

	__slots__ = ["_Reqd", "_OrgTp", "_PrvtTp"]
	@property
	def OrgTp(self):
		return self._OrgTp

	@OrgTp.setter
	def OrgTp(self, value):
		self._OrgTp = value if type(value) != base_types.auto else self.make_default("OrgTp")

	@OrgTp.deleter
	def OrgTp(self):
		del self._OrgTp
		self._OrgTp = None

	@property
	def PrvtTp(self):
		return self._PrvtTp

	@PrvtTp.setter
	def PrvtTp(self, value):
		self._PrvtTp = value if type(value) != base_types.auto else self.make_default("PrvtTp")

	@PrvtTp.deleter
	def PrvtTp(self):
		del self._PrvtTp
		self._PrvtTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgTp', type=OrganisationType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtTp', type=PersonType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reqd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))

