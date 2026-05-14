# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Min1Max256Binary import Min1Max256Binary

class DeviceSendApplicationProtocolDataUnitCardReaderResponse1(base_types._BaseFieldType):

	__slots__ = ["_CardSts", "_Data"]
	@property
	def CardSts(self):
		return self._CardSts

	@CardSts.setter
	def CardSts(self, value):
		self._CardSts = value if type(value) != base_types.auto else self.make_default("CardSts")

	@CardSts.deleter
	def CardSts(self):
		del self._CardSts
		self._CardSts = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSts', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
	))