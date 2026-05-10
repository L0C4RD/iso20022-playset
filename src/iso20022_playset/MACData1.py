from . import base_types
from .Max2NumericText import Max2NumericText
from .Max5NumericText import Max5NumericText
from .Max4NumericText import Max4NumericText
from .Exact1HexBinaryText import Exact1HexBinaryText
from .Max32HexBinaryText import Max32HexBinaryText
from .Max8NumericText import Max8NumericText

class MACData1(base_types._BaseFieldType):

	__slots__ = ["_PddgMtd", "_KeyLngth", "_Ctrl", "_KeySetIdr", "_InitlstnVctr", "_KeyIndx", "_Algo", "_DrvdInf", "_KeyPrtcn"]
	@property
	def PddgMtd(self):
		return self._PddgMtd

	@PddgMtd.setter
	def PddgMtd(self, value):
		self._PddgMtd = value if type(value) != auto else self.make_default("PddgMtd")

	@PddgMtd.deleter
	def PddgMtd(self):
		del self._PddgMtd
		self._PddgMtd = None

	@property
	def KeyLngth(self):
		return self._KeyLngth

	@KeyLngth.setter
	def KeyLngth(self, value):
		self._KeyLngth = value if type(value) != auto else self.make_default("KeyLngth")

	@KeyLngth.deleter
	def KeyLngth(self):
		del self._KeyLngth
		self._KeyLngth = None

	@property
	def Ctrl(self):
		return self._Ctrl

	@Ctrl.setter
	def Ctrl(self, value):
		self._Ctrl = value if type(value) != auto else self.make_default("Ctrl")

	@Ctrl.deleter
	def Ctrl(self):
		del self._Ctrl
		self._Ctrl = None

	@property
	def KeySetIdr(self):
		return self._KeySetIdr

	@KeySetIdr.setter
	def KeySetIdr(self, value):
		self._KeySetIdr = value if type(value) != auto else self.make_default("KeySetIdr")

	@KeySetIdr.deleter
	def KeySetIdr(self):
		del self._KeySetIdr
		self._KeySetIdr = None

	@property
	def InitlstnVctr(self):
		return self._InitlstnVctr

	@InitlstnVctr.setter
	def InitlstnVctr(self, value):
		self._InitlstnVctr = value if type(value) != auto else self.make_default("InitlstnVctr")

	@InitlstnVctr.deleter
	def InitlstnVctr(self):
		del self._InitlstnVctr
		self._InitlstnVctr = None

	@property
	def KeyIndx(self):
		return self._KeyIndx

	@KeyIndx.setter
	def KeyIndx(self, value):
		self._KeyIndx = value if type(value) != auto else self.make_default("KeyIndx")

	@KeyIndx.deleter
	def KeyIndx(self):
		del self._KeyIndx
		self._KeyIndx = None

	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def DrvdInf(self):
		return self._DrvdInf

	@DrvdInf.setter
	def DrvdInf(self, value):
		self._DrvdInf = value if type(value) != auto else self.make_default("DrvdInf")

	@DrvdInf.deleter
	def DrvdInf(self):
		del self._DrvdInf
		self._DrvdInf = None

	@property
	def KeyPrtcn(self):
		return self._KeyPrtcn

	@KeyPrtcn.setter
	def KeyPrtcn(self, value):
		self._KeyPrtcn = value if type(value) != auto else self.make_default("KeyPrtcn")

	@KeyPrtcn.deleter
	def KeyPrtcn(self):
		del self._KeyPrtcn
		self._KeyPrtcn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PddgMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyLngth', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrl', type=Exact1HexBinaryText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeySetIdr', type=Max8NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlstnVctr', type=Max32HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyIndx', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Algo', type=Max2NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvdInf', type=Max32HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyPrtcn', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

