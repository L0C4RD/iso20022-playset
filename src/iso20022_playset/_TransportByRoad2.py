# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class TransportByRoad2(base_types._BaseFieldType):

	__slots__ = ["_PlcOfDlvry", "_PlcOfRct", "_RoadCrrierNm"]
	@property
	def PlcOfDlvry(self):
		return self._PlcOfDlvry

	@PlcOfDlvry.setter
	def PlcOfDlvry(self, value):
		self._PlcOfDlvry = value if value is not None else base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, False)

	@PlcOfDlvry.deleter
	def PlcOfDlvry(self):
		del self._PlcOfDlvry
		self._PlcOfDlvry = base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, False)

	@property
	def PlcOfRct(self):
		return self._PlcOfRct

	@PlcOfRct.setter
	def PlcOfRct(self, value):
		self._PlcOfRct = value if value is not None else base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, False)

	@PlcOfRct.deleter
	def PlcOfRct(self):
		del self._PlcOfRct
		self._PlcOfRct = base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, False)

	@property
	def RoadCrrierNm(self):
		return self._RoadCrrierNm

	@RoadCrrierNm.setter
	def RoadCrrierNm(self, value):
		self._RoadCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'RoadCrrierNm', Max35Text, False)

	@RoadCrrierNm.deleter
	def RoadCrrierNm(self):
		del self._RoadCrrierNm
		self._RoadCrrierNm = base_types.UninitialisedField(self, 'RoadCrrierNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoadCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))