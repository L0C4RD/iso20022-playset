# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification242Choice
from . import PartyIdentification60

class FundIdentification5(base_types._BaseFieldType):

	__slots__ = ["_AcctIdWthCtdn", "_CtdnId", "_FndId"]
	@property
	def AcctIdWthCtdn(self):
		return self._AcctIdWthCtdn

	@AcctIdWthCtdn.setter
	def AcctIdWthCtdn(self, value):
		self._AcctIdWthCtdn = value if value is not None else base_types.UninitialisedField(self, 'AcctIdWthCtdn', Max35Text, False)

	@AcctIdWthCtdn.deleter
	def AcctIdWthCtdn(self):
		del self._AcctIdWthCtdn
		self._AcctIdWthCtdn = base_types.UninitialisedField(self, 'AcctIdWthCtdn', Max35Text, False)

	@property
	def CtdnId(self):
		return self._CtdnId

	@CtdnId.setter
	def CtdnId(self, value):
		self._CtdnId = value if value is not None else base_types.UninitialisedField(self, 'CtdnId', PartyIdentification242Choice, False)

	@CtdnId.deleter
	def CtdnId(self):
		del self._CtdnId
		self._CtdnId = base_types.UninitialisedField(self, 'CtdnId', PartyIdentification242Choice, False)

	@property
	def FndId(self):
		return self._FndId

	@FndId.setter
	def FndId(self, value):
		self._FndId = value if value is not None else base_types.UninitialisedField(self, 'FndId', PartyIdentification60, False)

	@FndId.deleter
	def FndId(self):
		del self._FndId
		self._FndId = base_types.UninitialisedField(self, 'FndId', PartyIdentification60, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdWthCtdn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtdnId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndId', type=PartyIdentification60, min=1, max=1, mutex_group=None, array=False),
	))