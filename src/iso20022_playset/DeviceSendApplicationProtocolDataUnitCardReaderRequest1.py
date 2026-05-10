from . import base_types
from .Min1Max256Binary import Min1Max256Binary

class DeviceSendApplicationProtocolDataUnitCardReaderRequest1(base_types._BaseFieldType):

	__slots__ = ["_Instr", "_XpctdLngth", "_Param2", "_Data", "_Clss", "_Param1"]
	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if type(value) != auto else self.make_default("Instr")

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = None

	@property
	def XpctdLngth(self):
		return self._XpctdLngth

	@XpctdLngth.setter
	def XpctdLngth(self, value):
		self._XpctdLngth = value if type(value) != auto else self.make_default("XpctdLngth")

	@XpctdLngth.deleter
	def XpctdLngth(self):
		del self._XpctdLngth
		self._XpctdLngth = None

	@property
	def Param2(self):
		return self._Param2

	@Param2.setter
	def Param2(self, value):
		self._Param2 = value if type(value) != auto else self.make_default("Param2")

	@Param2.deleter
	def Param2(self):
		del self._Param2
		self._Param2 = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if type(value) != auto else self.make_default("Clss")

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = None

	@property
	def Param1(self):
		return self._Param1

	@Param1.setter
	def Param1(self, value):
		self._Param1 = value if type(value) != auto else self.make_default("Param1")

	@Param1.deleter
	def Param1(self):
		del self._Param1
		self._Param1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Instr', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdLngth', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param2', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=Min1Max256Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clss', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param1', type=Min1Max256Binary, min=1, max=1, mutex_group=None, array=False),
	))

