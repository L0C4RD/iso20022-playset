# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Exact1HexBinaryText import Exact1HexBinaryText
from ._Max2NumericText import Max2NumericText
from ._Max32HexBinaryText import Max32HexBinaryText
from ._Max4NumericText import Max4NumericText
from ._Max5NumericText import Max5NumericText
from ._Max8NumericText import Max8NumericText
from ._Max9999HexBinaryText import Max9999HexBinaryText

class KeyExchangeData1(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Ctrl", "_DrvdInf", "_KeyChcksmVal", "_KeyIndx", "_KeyLngth", "_KeyPrtcn", "_KeySetIdr", "_NcrptdData"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != base_types.auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def Ctrl(self):
		return self._Ctrl

	@Ctrl.setter
	def Ctrl(self, value):
		self._Ctrl = value if type(value) != base_types.auto else self.make_default("Ctrl")

	@Ctrl.deleter
	def Ctrl(self):
		del self._Ctrl
		self._Ctrl = None

	@property
	def DrvdInf(self):
		return self._DrvdInf

	@DrvdInf.setter
	def DrvdInf(self, value):
		self._DrvdInf = value if type(value) != base_types.auto else self.make_default("DrvdInf")

	@DrvdInf.deleter
	def DrvdInf(self):
		del self._DrvdInf
		self._DrvdInf = None

	@property
	def KeyChcksmVal(self):
		return self._KeyChcksmVal

	@KeyChcksmVal.setter
	def KeyChcksmVal(self, value):
		self._KeyChcksmVal = value if type(value) != base_types.auto else self.make_default("KeyChcksmVal")

	@KeyChcksmVal.deleter
	def KeyChcksmVal(self):
		del self._KeyChcksmVal
		self._KeyChcksmVal = None

	@property
	def KeyIndx(self):
		return self._KeyIndx

	@KeyIndx.setter
	def KeyIndx(self, value):
		self._KeyIndx = value if type(value) != base_types.auto else self.make_default("KeyIndx")

	@KeyIndx.deleter
	def KeyIndx(self):
		del self._KeyIndx
		self._KeyIndx = None

	@property
	def KeyLngth(self):
		return self._KeyLngth

	@KeyLngth.setter
	def KeyLngth(self, value):
		self._KeyLngth = value if type(value) != base_types.auto else self.make_default("KeyLngth")

	@KeyLngth.deleter
	def KeyLngth(self):
		del self._KeyLngth
		self._KeyLngth = None

	@property
	def KeyPrtcn(self):
		return self._KeyPrtcn

	@KeyPrtcn.setter
	def KeyPrtcn(self, value):
		self._KeyPrtcn = value if type(value) != base_types.auto else self.make_default("KeyPrtcn")

	@KeyPrtcn.deleter
	def KeyPrtcn(self):
		del self._KeyPrtcn
		self._KeyPrtcn = None

	@property
	def KeySetIdr(self):
		return self._KeySetIdr

	@KeySetIdr.setter
	def KeySetIdr(self, value):
		self._KeySetIdr = value if type(value) != base_types.auto else self.make_default("KeySetIdr")

	@KeySetIdr.deleter
	def KeySetIdr(self):
		del self._KeySetIdr
		self._KeySetIdr = None

	@property
	def NcrptdData(self):
		return self._NcrptdData

	@NcrptdData.setter
	def NcrptdData(self, value):
		self._NcrptdData = value if type(value) != base_types.auto else self.make_default("NcrptdData")

	@NcrptdData.deleter
	def NcrptdData(self):
		del self._NcrptdData
		self._NcrptdData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrl', type=Exact1HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvdInf', type=Max32HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyChcksmVal', type=Max9999HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyIndx', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyLngth', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyPrtcn', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeySetIdr', type=Max8NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdData', type=Max9999HexBinaryText, min=0, max=1, mutex_group=None, array=False),
	))