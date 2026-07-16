# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import KEK9
from . import KEKIdentifier7
from . import KeyTransport10

class Recipient15Choice(base_types._BaseFieldType):

	__slots__ = ["_KEK", "_KeyIdr", "_KeyTrnsprt"]
	@property
	def KEK(self):
		return self._KEK

	@KEK.setter
	def KEK(self, value):
		self._KEK = value if value is not None else base_types.UninitialisedField(self, 'KEK', KEK9, False)

	@KEK.deleter
	def KEK(self):
		del self._KEK
		self._KEK = base_types.UninitialisedField(self, 'KEK', KEK9, False)

	@property
	def KeyIdr(self):
		return self._KeyIdr

	@KeyIdr.setter
	def KeyIdr(self, value):
		self._KeyIdr = value if value is not None else base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier7, False)

	@KeyIdr.deleter
	def KeyIdr(self):
		del self._KeyIdr
		self._KeyIdr = base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier7, False)

	@property
	def KeyTrnsprt(self):
		return self._KeyTrnsprt

	@KeyTrnsprt.setter
	def KeyTrnsprt(self, value):
		self._KeyTrnsprt = value if value is not None else base_types.UninitialisedField(self, 'KeyTrnsprt', KeyTransport10, False)

	@KeyTrnsprt.deleter
	def KeyTrnsprt(self):
		del self._KeyTrnsprt
		self._KeyTrnsprt = base_types.UninitialisedField(self, 'KeyTrnsprt', KeyTransport10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='KEK', type=KEK9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyTrnsprt', type=KeyTransport10, min=0, max=1, mutex_group=1, array=False),
	))