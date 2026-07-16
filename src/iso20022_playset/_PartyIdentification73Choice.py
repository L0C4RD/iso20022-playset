# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NameAndAddress8
from . import PartyIdentification44
from . import PartyIdentification59

class PartyIdentification73Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_NmAndAdr", "_PtyId"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', PartyIdentification44, False)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', PartyIdentification44, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress8, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress8, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification59, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification59, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=PartyIdentification44, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification59, min=0, max=1, mutex_group=1, array=False),
	))