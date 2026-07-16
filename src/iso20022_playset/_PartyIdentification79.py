# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification76
from . import PersonOrOrganisation2Choice

class PartyIdentification79(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_DcsnMakr"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification76, True)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification76, True)

	@property
	def DcsnMakr(self):
		return self._DcsnMakr

	@DcsnMakr.setter
	def DcsnMakr(self, value):
		self._DcsnMakr = value if value is not None else base_types.UninitialisedField(self, 'DcsnMakr', PersonOrOrganisation2Choice, True)

	@DcsnMakr.deleter
	def DcsnMakr(self):
		del self._DcsnMakr
		self._DcsnMakr = base_types.UninitialisedField(self, 'DcsnMakr', PersonOrOrganisation2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification76, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DcsnMakr', type=PersonOrOrganisation2Choice, min=0, max=None, mutex_group=None, array=True),
	))