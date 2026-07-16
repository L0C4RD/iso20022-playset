# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification1
from . import PartyIdentification8

class PartyIdentificationAndContactInformation1(base_types._BaseFieldType):

	__slots__ = ["_CtctInf", "_PtyId"]
	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if value is not None else base_types.UninitialisedField(self, 'CtctInf', ContactIdentification1, False)

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = base_types.UninitialisedField(self, 'CtctInf', ContactIdentification1, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification8, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctInf', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification8, min=1, max=1, mutex_group=None, array=False),
	))