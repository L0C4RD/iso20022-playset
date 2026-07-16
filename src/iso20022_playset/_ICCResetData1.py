# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Binary
from . import Max35Binary

class ICCResetData1(base_types._BaseFieldType):

	__slots__ = ["_ATRVal", "_CardSts"]
	@property
	def ATRVal(self):
		return self._ATRVal

	@ATRVal.setter
	def ATRVal(self, value):
		self._ATRVal = value if value is not None else base_types.UninitialisedField(self, 'ATRVal', Max140Binary, False)

	@ATRVal.deleter
	def ATRVal(self):
		del self._ATRVal
		self._ATRVal = base_types.UninitialisedField(self, 'ATRVal', Max140Binary, False)

	@property
	def CardSts(self):
		return self._CardSts

	@CardSts.setter
	def CardSts(self, value):
		self._CardSts = value if value is not None else base_types.UninitialisedField(self, 'CardSts', Max35Binary, False)

	@CardSts.deleter
	def CardSts(self):
		del self._CardSts
		self._CardSts = base_types.UninitialisedField(self, 'CardSts', Max35Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATRVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSts', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
	))