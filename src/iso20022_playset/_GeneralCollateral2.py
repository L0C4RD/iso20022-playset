# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class GeneralCollateral2(base_types._BaseFieldType):

	__slots__ = ["_ElgblFinInstrmId"]
	@property
	def ElgblFinInstrmId(self):
		return self._ElgblFinInstrmId

	@ElgblFinInstrmId.setter
	def ElgblFinInstrmId(self, value):
		self._ElgblFinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'ElgblFinInstrmId', Max35Text, True)

	@ElgblFinInstrmId.deleter
	def ElgblFinInstrmId(self):
		del self._ElgblFinInstrmId
		self._ElgblFinInstrmId = base_types.UninitialisedField(self, 'ElgblFinInstrmId', Max35Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblFinInstrmId', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
	))