# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max35Text
from . import Max70Text

class TransportByRoad5(base_types._BaseFieldType):

	__slots__ = ["_CrrierAgtCtry", "_CrrierAgtNm", "_PlcOfDlvry", "_PlcOfRct", "_RoadCrrierCtry", "_RoadCrrierNm"]
	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@property
	def PlcOfDlvry(self):
		return self._PlcOfDlvry

	@PlcOfDlvry.setter
	def PlcOfDlvry(self, value):
		self._PlcOfDlvry = value if value is not None else base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, True)

	@PlcOfDlvry.deleter
	def PlcOfDlvry(self):
		del self._PlcOfDlvry
		self._PlcOfDlvry = base_types.UninitialisedField(self, 'PlcOfDlvry', Max35Text, True)

	@property
	def PlcOfRct(self):
		return self._PlcOfRct

	@PlcOfRct.setter
	def PlcOfRct(self, value):
		self._PlcOfRct = value if value is not None else base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, True)

	@PlcOfRct.deleter
	def PlcOfRct(self):
		del self._PlcOfRct
		self._PlcOfRct = base_types.UninitialisedField(self, 'PlcOfRct', Max35Text, True)

	@property
	def RoadCrrierCtry(self):
		return self._RoadCrrierCtry

	@RoadCrrierCtry.setter
	def RoadCrrierCtry(self, value):
		self._RoadCrrierCtry = value if value is not None else base_types.UninitialisedField(self, 'RoadCrrierCtry', CountryCode, False)

	@RoadCrrierCtry.deleter
	def RoadCrrierCtry(self):
		del self._RoadCrrierCtry
		self._RoadCrrierCtry = base_types.UninitialisedField(self, 'RoadCrrierCtry', CountryCode, False)

	@property
	def RoadCrrierNm(self):
		return self._RoadCrrierNm

	@RoadCrrierNm.setter
	def RoadCrrierNm(self, value):
		self._RoadCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'RoadCrrierNm', Max70Text, False)

	@RoadCrrierNm.deleter
	def RoadCrrierNm(self):
		del self._RoadCrrierNm
		self._RoadCrrierNm = base_types.UninitialisedField(self, 'RoadCrrierNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RoadCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoadCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))