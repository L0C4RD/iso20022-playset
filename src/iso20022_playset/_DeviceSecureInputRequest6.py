from . import base_types
from ._Max35Text import Max35Text
from ._Number import Number
from ._OnLinePIN11 import OnLinePIN11
from ._PINRequestType1Code import PINRequestType1Code
from ._TrueFalseIndicator import TrueFalseIndicator

class DeviceSecureInputRequest6(base_types._BaseFieldType):

	__slots__ = ["_BeepKeyFlg", "_CrdhldrPIN", "_MaxWtgTm", "_PINReqTp", "_PINVrfctnMtd"]
	@property
	def BeepKeyFlg(self):
		return self._BeepKeyFlg

	@BeepKeyFlg.setter
	def BeepKeyFlg(self, value):
		self._BeepKeyFlg = value if type(value) != base_types.auto else self.make_default("BeepKeyFlg")

	@BeepKeyFlg.deleter
	def BeepKeyFlg(self):
		del self._BeepKeyFlg
		self._BeepKeyFlg = None

	@property
	def CrdhldrPIN(self):
		return self._CrdhldrPIN

	@CrdhldrPIN.setter
	def CrdhldrPIN(self, value):
		self._CrdhldrPIN = value if type(value) != base_types.auto else self.make_default("CrdhldrPIN")

	@CrdhldrPIN.deleter
	def CrdhldrPIN(self):
		del self._CrdhldrPIN
		self._CrdhldrPIN = None

	@property
	def MaxWtgTm(self):
		return self._MaxWtgTm

	@MaxWtgTm.setter
	def MaxWtgTm(self, value):
		self._MaxWtgTm = value if type(value) != base_types.auto else self.make_default("MaxWtgTm")

	@MaxWtgTm.deleter
	def MaxWtgTm(self):
		del self._MaxWtgTm
		self._MaxWtgTm = None

	@property
	def PINReqTp(self):
		return self._PINReqTp

	@PINReqTp.setter
	def PINReqTp(self, value):
		self._PINReqTp = value if type(value) != base_types.auto else self.make_default("PINReqTp")

	@PINReqTp.deleter
	def PINReqTp(self):
		del self._PINReqTp
		self._PINReqTp = None

	@property
	def PINVrfctnMtd(self):
		return self._PINVrfctnMtd

	@PINVrfctnMtd.setter
	def PINVrfctnMtd(self, value):
		self._PINVrfctnMtd = value if type(value) != base_types.auto else self.make_default("PINVrfctnMtd")

	@PINVrfctnMtd.deleter
	def PINVrfctnMtd(self):
		del self._PINVrfctnMtd
		self._PINVrfctnMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BeepKeyFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINReqTp', type=PINRequestType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINVrfctnMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

