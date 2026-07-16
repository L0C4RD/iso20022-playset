# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import PersonOrOrganisation1Choice

class PartyIdentification76(base_types._BaseFieldType):

	__slots__ = ["_CtryOfBrnch", "_Id"]
	@property
	def CtryOfBrnch(self):
		return self._CtryOfBrnch

	@CtryOfBrnch.setter
	def CtryOfBrnch(self, value):
		self._CtryOfBrnch = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@CtryOfBrnch.deleter
	def CtryOfBrnch(self):
		del self._CtryOfBrnch
		self._CtryOfBrnch = base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PersonOrOrganisation1Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PersonOrOrganisation1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryOfBrnch', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PersonOrOrganisation1Choice, min=1, max=1, mutex_group=None, array=False),
	))