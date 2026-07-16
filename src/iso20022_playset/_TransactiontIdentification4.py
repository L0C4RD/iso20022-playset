# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class TransactiontIdentification4(base_types._BaseFieldType):

	__slots__ = ["_TxId"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))