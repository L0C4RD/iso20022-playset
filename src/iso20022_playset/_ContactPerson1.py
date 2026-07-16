# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification4
from . import PartyIdentification2Choice

class ContactPerson1(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_InstnId"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification4, False)

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = base_types.UninitialisedField(self, 'CtctPrsn', ContactIdentification4, False)

	@property
	def InstnId(self):
		return self._InstnId

	@InstnId.setter
	def InstnId(self, value):
		self._InstnId = value if value is not None else base_types.UninitialisedField(self, 'InstnId', PartyIdentification2Choice, False)

	@InstnId.deleter
	def InstnId(self):
		del self._InstnId
		self._InstnId = base_types.UninitialisedField(self, 'InstnId', PartyIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstnId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))