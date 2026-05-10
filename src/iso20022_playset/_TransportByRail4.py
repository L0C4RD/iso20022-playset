from . import base_types
from ._CountryCode import CountryCode
from ._Max70Text import Max70Text
from ._Max35Text import Max35Text

class TransportByRail4(base_types._BaseFieldType):

	__slots__ = ["_RailCrrierCtry", "_PlcOfDlvry", "_PlcOfRct", "_CrrierAgtCtry", "_CrrierAgtNm", "_RailCrrierNm"]
	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if type(value) != base_types.auto else self.make_default("CrrierAgtCtry")

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = None

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if type(value) != base_types.auto else self.make_default("CrrierAgtNm")

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = None

	@property
	def PlcOfDlvry(self):
		return self._PlcOfDlvry

	@PlcOfDlvry.setter
	def PlcOfDlvry(self, value):
		self._PlcOfDlvry = value if type(value) != base_types.auto else self.make_default("PlcOfDlvry")

	@PlcOfDlvry.deleter
	def PlcOfDlvry(self):
		del self._PlcOfDlvry
		self._PlcOfDlvry = None

	@property
	def PlcOfRct(self):
		return self._PlcOfRct

	@PlcOfRct.setter
	def PlcOfRct(self, value):
		self._PlcOfRct = value if type(value) != base_types.auto else self.make_default("PlcOfRct")

	@PlcOfRct.deleter
	def PlcOfRct(self):
		del self._PlcOfRct
		self._PlcOfRct = None

	@property
	def RailCrrierCtry(self):
		return self._RailCrrierCtry

	@RailCrrierCtry.setter
	def RailCrrierCtry(self, value):
		self._RailCrrierCtry = value if type(value) != base_types.auto else self.make_default("RailCrrierCtry")

	@RailCrrierCtry.deleter
	def RailCrrierCtry(self):
		del self._RailCrrierCtry
		self._RailCrrierCtry = None

	@property
	def RailCrrierNm(self):
		return self._RailCrrierNm

	@RailCrrierNm.setter
	def RailCrrierNm(self, value):
		self._RailCrrierNm = value if type(value) != base_types.auto else self.make_default("RailCrrierNm")

	@RailCrrierNm.deleter
	def RailCrrierNm(self):
		del self._RailCrrierNm
		self._RailCrrierNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfDlvry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfRct', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RailCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RailCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

