# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import KEK6
from . import KEKIdentifier6
from . import KeyTransport6

class Recipient7Choice(base_types._BaseFieldType):

	__slots__ = ["_KEK", "_KeyIdr", "_KeyTrnsprt"]
	@property
	def KEK(self):
		return self._KEK

	@KEK.setter
	def KEK(self, value):
		self._KEK = value if value is not None else base_types.UninitialisedField(self, 'KEK', KEK6, False)

	@KEK.deleter
	def KEK(self):
		del self._KEK
		self._KEK = base_types.UninitialisedField(self, 'KEK', KEK6, False)

	@property
	def KeyIdr(self):
		return self._KeyIdr

	@KeyIdr.setter
	def KeyIdr(self, value):
		self._KeyIdr = value if value is not None else base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier6, False)

	@KeyIdr.deleter
	def KeyIdr(self):
		del self._KeyIdr
		self._KeyIdr = base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier6, False)

	@property
	def KeyTrnsprt(self):
		return self._KeyTrnsprt

	@KeyTrnsprt.setter
	def KeyTrnsprt(self, value):
		self._KeyTrnsprt = value if value is not None else base_types.UninitialisedField(self, 'KeyTrnsprt', KeyTransport6, False)

	@KeyTrnsprt.deleter
	def KeyTrnsprt(self):
		del self._KeyTrnsprt
		self._KeyTrnsprt = base_types.UninitialisedField(self, 'KeyTrnsprt', KeyTransport6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='KEK', type=KEK6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyTrnsprt', type=KeyTransport6, min=0, max=1, mutex_group=1, array=False),
	))