# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NameAndAddress10
from . import PostalAddress6

class AddressOrParty1Choice(base_types._BaseFieldType):

	__slots__ = ["_NewAdr", "_NewBnfcry"]
	@property
	def NewAdr(self):
		return self._NewAdr

	@NewAdr.setter
	def NewAdr(self, value):
		self._NewAdr = value if value is not None else base_types.UninitialisedField(self, 'NewAdr', PostalAddress6, False)

	@NewAdr.deleter
	def NewAdr(self):
		del self._NewAdr
		self._NewAdr = base_types.UninitialisedField(self, 'NewAdr', PostalAddress6, False)

	@property
	def NewBnfcry(self):
		return self._NewBnfcry

	@NewBnfcry.setter
	def NewBnfcry(self, value):
		self._NewBnfcry = value if value is not None else base_types.UninitialisedField(self, 'NewBnfcry', NameAndAddress10, False)

	@NewBnfcry.deleter
	def NewBnfcry(self):
		del self._NewBnfcry
		self._NewBnfcry = base_types.UninitialisedField(self, 'NewBnfcry', NameAndAddress10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewAdr', type=PostalAddress6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NewBnfcry', type=NameAndAddress10, min=0, max=1, mutex_group=1, array=False),
	))