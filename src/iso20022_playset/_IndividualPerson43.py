# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification129Choice
from . import PartyIdentification232Choice

class IndividualPerson43(base_types._BaseFieldType):

	__slots__ = ["_EmplngPty", "_PrssgndPrxy"]
	@property
	def EmplngPty(self):
		return self._EmplngPty

	@EmplngPty.setter
	def EmplngPty(self, value):
		self._EmplngPty = value if value is not None else base_types.UninitialisedField(self, 'EmplngPty', PartyIdentification129Choice, False)

	@EmplngPty.deleter
	def EmplngPty(self):
		del self._EmplngPty
		self._EmplngPty = base_types.UninitialisedField(self, 'EmplngPty', PartyIdentification129Choice, False)

	@property
	def PrssgndPrxy(self):
		return self._PrssgndPrxy

	@PrssgndPrxy.setter
	def PrssgndPrxy(self, value):
		self._PrssgndPrxy = value if value is not None else base_types.UninitialisedField(self, 'PrssgndPrxy', PartyIdentification232Choice, False)

	@PrssgndPrxy.deleter
	def PrssgndPrxy(self):
		del self._PrssgndPrxy
		self._PrssgndPrxy = base_types.UninitialisedField(self, 'PrssgndPrxy', PartyIdentification232Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrssgndPrxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
	))