# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class Addition2(base_types._BaseFieldType):

	__slots__ = ["_PropsdVal"]
	@property
	def PropsdVal(self):
		return self._PropsdVal

	@PropsdVal.setter
	def PropsdVal(self, value):
		self._PropsdVal = value if value is not None else base_types.UninitialisedField(self, 'PropsdVal', Max350Text, False)

	@PropsdVal.deleter
	def PropsdVal(self):
		del self._PropsdVal
		self._PropsdVal = base_types.UninitialisedField(self, 'PropsdVal', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PropsdVal', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))