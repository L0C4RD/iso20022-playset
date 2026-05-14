# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionOperationType11Code import TransactionOperationType11Code

class ContractModification8(base_types._BaseFieldType):

	__slots__ = ["_ActnTp"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TransactionOperationType11Code, min=1, max=1, mutex_group=None, array=False),
	))