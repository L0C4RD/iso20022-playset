# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class Deletion2(base_types._BaseFieldType):

	__slots__ = ["_DeltdVal"]
	@property
	def DeltdVal(self):
		return self._DeltdVal

	@DeltdVal.setter
	def DeltdVal(self, value):
		self._DeltdVal = value if value is not None else base_types.UninitialisedField(self, 'DeltdVal', Max350Text, False)

	@DeltdVal.deleter
	def DeltdVal(self):
		del self._DeltdVal
		self._DeltdVal = base_types.UninitialisedField(self, 'DeltdVal', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeltdVal', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))