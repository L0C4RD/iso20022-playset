import base_types
import Max35Text

class TransportByRail2(base_types._BaseFieldType):

	__slots__ = ["_RailCrrierNm", "_PlcOfDlvry", "_PlcOfRct"]
	@property
	def RailCrrierNm(self):
		return self._RailCrrierNm

	@RailCrrierNm.setter
	def RailCrrierNm(self, value):
		self._RailCrrierNm = value if type(value) != auto else self.make_default("RailCrrierNm")

	@RailCrrierNm.deleter
	def RailCrrierNm(self):
		del self._RailCrrierNm
		self._RailCrrierNm = None

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
		base_types.FieldEntry(name='RailCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

