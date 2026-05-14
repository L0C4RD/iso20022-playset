# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class GeneralCollateral2(base_types._BaseFieldType):

	__slots__ = ["_ElgblFinInstrmId"]
	@property
	def ElgblFinInstrmId(self):
		return self._ElgblFinInstrmId

	@ElgblFinInstrmId.setter
	def ElgblFinInstrmId(self, value):
		self._ElgblFinInstrmId = value if type(value) != base_types.auto else self.make_default("ElgblFinInstrmId")

	@ElgblFinInstrmId.deleter
	def ElgblFinInstrmId(self):
		del self._ElgblFinInstrmId
		self._ElgblFinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblFinInstrmId', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
	))