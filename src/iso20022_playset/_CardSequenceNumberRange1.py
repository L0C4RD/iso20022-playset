# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class CardSequenceNumberRange1(base_types._BaseFieldType):

	__slots__ = ["_FrstTx", "_LastTx"]
	@property
	def FrstTx(self):
		return self._FrstTx

	@FrstTx.setter
	def FrstTx(self, value):
		self._FrstTx = value if type(value) != base_types.auto else self.make_default("FrstTx")

	@FrstTx.deleter
	def FrstTx(self):
		del self._FrstTx
		self._FrstTx = None

	@property
	def LastTx(self):
		return self._LastTx

	@LastTx.setter
	def LastTx(self, value):
		self._LastTx = value if type(value) != base_types.auto else self.make_default("LastTx")

	@LastTx.deleter
	def LastTx(self):
		del self._LastTx
		self._LastTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstTx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))