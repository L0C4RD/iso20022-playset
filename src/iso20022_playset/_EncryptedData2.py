# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EncryptedDataElement2
from . import Exact1HexBinaryText
from . import Max2NumericText
from . import Max32HexBinaryText
from . import Max4NumericText
from . import Max5NumericText
from . import Max8NumericText

class EncryptedData2(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Ctrl", "_DrvdInf", "_KeyIndx", "_KeyLngth", "_KeyPrtcn", "_KeySetIdr", "_NcrptdElmt", "_NcrptdFrmt", "_PddgMtd"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if value is not None else base_types.UninitialisedField(self, 'Algo', Max2NumericText, False)

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = base_types.UninitialisedField(self, 'Algo', Max2NumericText, False)

	@property
	def Ctrl(self):
		return self._Ctrl

	@Ctrl.setter
	def Ctrl(self, value):
		self._Ctrl = value if value is not None else base_types.UninitialisedField(self, 'Ctrl', Exact1HexBinaryText, False)

	@Ctrl.deleter
	def Ctrl(self):
		del self._Ctrl
		self._Ctrl = base_types.UninitialisedField(self, 'Ctrl', Exact1HexBinaryText, False)

	@property
	def DrvdInf(self):
		return self._DrvdInf

	@DrvdInf.setter
	def DrvdInf(self, value):
		self._DrvdInf = value if value is not None else base_types.UninitialisedField(self, 'DrvdInf', Max32HexBinaryText, False)

	@DrvdInf.deleter
	def DrvdInf(self):
		del self._DrvdInf
		self._DrvdInf = base_types.UninitialisedField(self, 'DrvdInf', Max32HexBinaryText, False)

	@property
	def KeyIndx(self):
		return self._KeyIndx

	@KeyIndx.setter
	def KeyIndx(self, value):
		self._KeyIndx = value if value is not None else base_types.UninitialisedField(self, 'KeyIndx', Max5NumericText, False)

	@KeyIndx.deleter
	def KeyIndx(self):
		del self._KeyIndx
		self._KeyIndx = base_types.UninitialisedField(self, 'KeyIndx', Max5NumericText, False)

	@property
	def KeyLngth(self):
		return self._KeyLngth

	@KeyLngth.setter
	def KeyLngth(self, value):
		self._KeyLngth = value if value is not None else base_types.UninitialisedField(self, 'KeyLngth', Max4NumericText, False)

	@KeyLngth.deleter
	def KeyLngth(self):
		del self._KeyLngth
		self._KeyLngth = base_types.UninitialisedField(self, 'KeyLngth', Max4NumericText, False)

	@property
	def KeyPrtcn(self):
		return self._KeyPrtcn

	@KeyPrtcn.setter
	def KeyPrtcn(self, value):
		self._KeyPrtcn = value if value is not None else base_types.UninitialisedField(self, 'KeyPrtcn', Max2NumericText, False)

	@KeyPrtcn.deleter
	def KeyPrtcn(self):
		del self._KeyPrtcn
		self._KeyPrtcn = base_types.UninitialisedField(self, 'KeyPrtcn', Max2NumericText, False)

	@property
	def KeySetIdr(self):
		return self._KeySetIdr

	@KeySetIdr.setter
	def KeySetIdr(self, value):
		self._KeySetIdr = value if value is not None else base_types.UninitialisedField(self, 'KeySetIdr', Max8NumericText, False)

	@KeySetIdr.deleter
	def KeySetIdr(self):
		del self._KeySetIdr
		self._KeySetIdr = base_types.UninitialisedField(self, 'KeySetIdr', Max8NumericText, False)

	@property
	def NcrptdElmt(self):
		return self._NcrptdElmt

	@NcrptdElmt.setter
	def NcrptdElmt(self, value):
		self._NcrptdElmt = value if value is not None else base_types.UninitialisedField(self, 'NcrptdElmt', EncryptedDataElement2, True)

	@NcrptdElmt.deleter
	def NcrptdElmt(self):
		del self._NcrptdElmt
		self._NcrptdElmt = base_types.UninitialisedField(self, 'NcrptdElmt', EncryptedDataElement2, True)

	@property
	def NcrptdFrmt(self):
		return self._NcrptdFrmt

	@NcrptdFrmt.setter
	def NcrptdFrmt(self, value):
		self._NcrptdFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcrptdFrmt', Max2NumericText, False)

	@NcrptdFrmt.deleter
	def NcrptdFrmt(self):
		del self._NcrptdFrmt
		self._NcrptdFrmt = base_types.UninitialisedField(self, 'NcrptdFrmt', Max2NumericText, False)

	@property
	def PddgMtd(self):
		return self._PddgMtd

	@PddgMtd.setter
	def PddgMtd(self, value):
		self._PddgMtd = value if value is not None else base_types.UninitialisedField(self, 'PddgMtd', Max2NumericText, False)

	@PddgMtd.deleter
	def PddgMtd(self):
		del self._PddgMtd
		self._PddgMtd = base_types.UninitialisedField(self, 'PddgMtd', Max2NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctrl', type=Exact1HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvdInf', type=Max32HexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyIndx', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyLngth', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyPrtcn', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeySetIdr', type=Max8NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdElmt', type=EncryptedDataElement2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NcrptdFrmt', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PddgMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))