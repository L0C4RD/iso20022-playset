# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactIdentification1
from . import PartyIdentification129Choice
from . import PostalAddress1

class PartyIdentification289(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_CtctPrsnAdr", "_PtyId"]
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
	def CtctPrsnAdr(self):
		return self._CtctPrsnAdr

	@CtctPrsnAdr.setter
	def CtctPrsnAdr(self, value):
		self._CtctPrsnAdr = value if value is not None else base_types.UninitialisedField(self, 'CtctPrsnAdr', PostalAddress1, False)

	@CtctPrsnAdr.deleter
	def CtctPrsnAdr(self):
		del self._CtctPrsnAdr
		self._CtctPrsnAdr = base_types.UninitialisedField(self, 'CtctPrsnAdr', PostalAddress1, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification129Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification129Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification129Choice, min=1, max=1, mutex_group=None, array=False),
	))