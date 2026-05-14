# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._KEK6 import KEK6
from ._KEKIdentifier6 import KEKIdentifier6
from ._KeyTransport6 import KeyTransport6

class Recipient7Choice(base_types._BaseFieldType):

	__slots__ = ["_KEK", "_KeyIdr", "_KeyTrnsprt"]
	@property
	def KEK(self):
		return self._KEK

	@KEK.setter
	def KEK(self, value):
		self._KEK = value if type(value) != base_types.auto else self.make_default("KEK")

	@KEK.deleter
	def KEK(self):
		del self._KEK
		self._KEK = None

	@property
	def KeyIdr(self):
		return self._KeyIdr

	@KeyIdr.setter
	def KeyIdr(self, value):
		self._KeyIdr = value if type(value) != base_types.auto else self.make_default("KeyIdr")

	@KeyIdr.deleter
	def KeyIdr(self):
		del self._KeyIdr
		self._KeyIdr = None

	@property
	def KeyTrnsprt(self):
		return self._KeyTrnsprt

	@KeyTrnsprt.setter
	def KeyTrnsprt(self, value):
		self._KeyTrnsprt = value if type(value) != base_types.auto else self.make_default("KeyTrnsprt")

	@KeyTrnsprt.deleter
	def KeyTrnsprt(self):
		del self._KeyTrnsprt
		self._KeyTrnsprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KEK', type=KEK6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyTrnsprt', type=KeyTransport6, min=0, max=1, mutex_group=1, array=False),
	))