# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class CardSequenceNumberRange1(base_types._BaseFieldType):

	__slots__ = ["_FrstTx", "_LastTx"]
	@property
	def FrstTx(self):
		return self._FrstTx

	@FrstTx.setter
	def FrstTx(self, value):
		self._FrstTx = value if value is not None else base_types.UninitialisedField(self, 'FrstTx', Max35Text, False)

	@FrstTx.deleter
	def FrstTx(self):
		del self._FrstTx
		self._FrstTx = base_types.UninitialisedField(self, 'FrstTx', Max35Text, False)

	@property
	def LastTx(self):
		return self._LastTx

	@LastTx.setter
	def LastTx(self, value):
		self._LastTx = value if value is not None else base_types.UninitialisedField(self, 'LastTx', Max35Text, False)

	@LastTx.deleter
	def LastTx(self):
		del self._LastTx
		self._LastTx = base_types.UninitialisedField(self, 'LastTx', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstTx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))