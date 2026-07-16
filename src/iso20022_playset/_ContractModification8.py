# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionOperationType11Code

class ContractModification8(base_types._BaseFieldType):

	__slots__ = ["_ActnTp"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType11Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TransactionOperationType11Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType11Code, min=1, max=1, mutex_group=None, array=False),
	))