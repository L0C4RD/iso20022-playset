# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MACData1
from . import Max8HexBinaryText

class ContentInformationType41(base_types._BaseFieldType):

	__slots__ = ["_MAC", "_MACData"]
	@property
	def MAC(self):
		return self._MAC

	@MAC.setter
	def MAC(self, value):
		self._MAC = value if value is not None else base_types.UninitialisedField(self, 'MAC', Max8HexBinaryText, False)

	@MAC.deleter
	def MAC(self):
		del self._MAC
		self._MAC = base_types.UninitialisedField(self, 'MAC', Max8HexBinaryText, False)

	@property
	def MACData(self):
		return self._MACData

	@MACData.setter
	def MACData(self, value):
		self._MACData = value if value is not None else base_types.UninitialisedField(self, 'MACData', MACData1, False)

	@MACData.deleter
	def MACData(self):
		del self._MACData
		self._MACData = base_types.UninitialisedField(self, 'MACData', MACData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MAC', type=Max8HexBinaryText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MACData', type=MACData1, min=1, max=1, mutex_group=None, array=False),
	))