# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification1
from . import MICIdentifier
from . import PartyIdentification129Choice

class MeetingContactPerson3(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_EmplngPty", "_PlcOfListg"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification1, False)

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification1, False)

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
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if value is not None else base_types.UninitialisedField(self, 'PlcOfListg', MICIdentifier, False)

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = base_types.UninitialisedField(self, 'PlcOfListg', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmplngPty', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))