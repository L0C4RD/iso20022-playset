# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification221
from . import PartyRole3Code

class ThirdPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_LglPrsnId", "_Role"]
	@property
	def LglPrsnId(self):
		return self._LglPrsnId

	@LglPrsnId.setter
	def LglPrsnId(self, value):
		self._LglPrsnId = value if value is not None else base_types.UninitialisedField(self, 'LglPrsnId', PartyIdentification221, False)

	@LglPrsnId.deleter
	def LglPrsnId(self):
		del self._LglPrsnId
		self._LglPrsnId = base_types.UninitialisedField(self, 'LglPrsnId', PartyIdentification221, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', PartyRole3Code, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', PartyRole3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglPrsnId', type=PartyIdentification221, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PartyRole3Code, min=1, max=1, mutex_group=None, array=False),
	))