import base_types
import Max35Text
import CountryCode
import Max70Text

class TransportByRoad4(base_types._BaseFieldType):

	__slots__ = ["_PlcOfDlvry", "_RoadCrrierNm", "_RoadCrrierCtry", "_CrrierAgtNm", "_CrrierAgtCtry", "_PlcOfRct"]
	@property
	def PlcOfDlvry(self):
		return self._PlcOfDlvry

	@PlcOfDlvry.setter
	def PlcOfDlvry(self, value):
		self._PlcOfDlvry = value if type(value) != auto else self.make_default("PlcOfDlvry")

	@PlcOfDlvry.deleter
	def PlcOfDlvry(self):
		del self._PlcOfDlvry
		self._PlcOfDlvry = None

	@property
	def RoadCrrierNm(self):
		return self._RoadCrrierNm

	@RoadCrrierNm.setter
	def RoadCrrierNm(self, value):
		self._RoadCrrierNm = value if type(value) != auto else self.make_default("RoadCrrierNm")

	@RoadCrrierNm.deleter
	def RoadCrrierNm(self):
		del self._RoadCrrierNm
		self._RoadCrrierNm = None

	@property
	def RoadCrrierCtry(self):
		return self._RoadCrrierCtry

	@RoadCrrierCtry.setter
	def RoadCrrierCtry(self, value):
		self._RoadCrrierCtry = value if type(value) != auto else self.make_default("RoadCrrierCtry")

	@RoadCrrierCtry.deleter
	def RoadCrrierCtry(self):
		del self._RoadCrrierCtry
		self._RoadCrrierCtry = None

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if type(value) != auto else self.make_default("CrrierAgtNm")

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = None

	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if type(value) != auto else self.make_default("CrrierAgtCtry")

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = None

	@property
	def PlcOfRct(self):
		return self._PlcOfRct

	@PlcOfRct.setter
	def PlcOfRct(self, value):
		self._PlcOfRct = value if type(value) != auto else self.make_default("PlcOfRct")

	@PlcOfRct.deleter
	def PlcOfRct(self):
		del self._PlcOfRct
		self._PlcOfRct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoadCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RoadCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

