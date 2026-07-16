# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrganisationType2
from . import PersonType2
from . import RequestedIndicator

class CustomerTypeRequest2(base_types._BaseFieldType):

	__slots__ = ["_OrgTp", "_PrvtTp", "_Reqd"]
	@property
	def OrgTp(self):
		return self._OrgTp

	@OrgTp.setter
	def OrgTp(self, value):
		self._OrgTp = value if value is not None else base_types.UninitialisedField(self, 'OrgTp', OrganisationType2, False)

	@OrgTp.deleter
	def OrgTp(self):
		del self._OrgTp
		self._OrgTp = base_types.UninitialisedField(self, 'OrgTp', OrganisationType2, False)

	@property
	def PrvtTp(self):
		return self._PrvtTp

	@PrvtTp.setter
	def PrvtTp(self, value):
		self._PrvtTp = value if value is not None else base_types.UninitialisedField(self, 'PrvtTp', PersonType2, False)

	@PrvtTp.deleter
	def PrvtTp(self):
		del self._PrvtTp
		self._PrvtTp = base_types.UninitialisedField(self, 'PrvtTp', PersonType2, False)

	@property
	def Reqd(self):
		return self._Reqd

	@Reqd.setter
	def Reqd(self, value):
		self._Reqd = value if value is not None else base_types.UninitialisedField(self, 'Reqd', RequestedIndicator, False)

	@Reqd.deleter
	def Reqd(self):
		del self._Reqd
		self._Reqd = base_types.UninitialisedField(self, 'Reqd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgTp', type=OrganisationType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtTp', type=PersonType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reqd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))