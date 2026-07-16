# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import OrganisationIdentification5

class PartyAdditionalIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_RegnId"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if value is not None else base_types.UninitialisedField(self, 'RegnId', OrganisationIdentification5, False)

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = base_types.UninitialisedField(self, 'RegnId', OrganisationIdentification5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegnId', type=OrganisationIdentification5, min=0, max=1, mutex_group=1, array=False),
	))