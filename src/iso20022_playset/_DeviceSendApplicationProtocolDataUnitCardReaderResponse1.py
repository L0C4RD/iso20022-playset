# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Min1Max256Binary

class DeviceSendApplicationProtocolDataUnitCardReaderResponse1(base_types._BaseFieldType):

	__slots__ = ["_CardSts", "_Data"]
	@property
	def CardSts(self):
		return self._CardSts

	@CardSts.setter
	def CardSts(self, value):
		self._CardSts = value if value is not None else base_types.UninitialisedField(self, 'CardSts', Min1Max256Binary, False)

	@CardSts.deleter
	def CardSts(self):
		del self._CardSts
		self._CardSts = base_types.UninitialisedField(self, 'CardSts', Min1Max256Binary, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', Min1Max256Binary, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', Min1Max256Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSts', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
	))