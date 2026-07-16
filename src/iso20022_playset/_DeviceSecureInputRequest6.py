# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number
from . import OnLinePIN11
from . import PINRequestType1Code
from . import TrueFalseIndicator

class DeviceSecureInputRequest6(base_types._BaseFieldType):

	__slots__ = ["_BeepKeyFlg", "_CrdhldrPIN", "_MaxWtgTm", "_PINReqTp", "_PINVrfctnMtd"]
	@property
	def BeepKeyFlg(self):
		return self._BeepKeyFlg

	@BeepKeyFlg.setter
	def BeepKeyFlg(self, value):
		self._BeepKeyFlg = value if value is not None else base_types.UninitialisedField(self, 'BeepKeyFlg', TrueFalseIndicator, False)

	@BeepKeyFlg.deleter
	def BeepKeyFlg(self):
		del self._BeepKeyFlg
		self._BeepKeyFlg = base_types.UninitialisedField(self, 'BeepKeyFlg', TrueFalseIndicator, False)

	@property
	def CrdhldrPIN(self):
		return self._CrdhldrPIN

	@CrdhldrPIN.setter
	def CrdhldrPIN(self, value):
		self._CrdhldrPIN = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrPIN', OnLinePIN11, False)

	@CrdhldrPIN.deleter
	def CrdhldrPIN(self):
		del self._CrdhldrPIN
		self._CrdhldrPIN = base_types.UninitialisedField(self, 'CrdhldrPIN', OnLinePIN11, False)

	@property
	def MaxWtgTm(self):
		return self._MaxWtgTm

	@MaxWtgTm.setter
	def MaxWtgTm(self, value):
		self._MaxWtgTm = value if value is not None else base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@MaxWtgTm.deleter
	def MaxWtgTm(self):
		del self._MaxWtgTm
		self._MaxWtgTm = base_types.UninitialisedField(self, 'MaxWtgTm', Number, False)

	@property
	def PINReqTp(self):
		return self._PINReqTp

	@PINReqTp.setter
	def PINReqTp(self, value):
		self._PINReqTp = value if value is not None else base_types.UninitialisedField(self, 'PINReqTp', PINRequestType1Code, False)

	@PINReqTp.deleter
	def PINReqTp(self):
		del self._PINReqTp
		self._PINReqTp = base_types.UninitialisedField(self, 'PINReqTp', PINRequestType1Code, False)

	@property
	def PINVrfctnMtd(self):
		return self._PINVrfctnMtd

	@PINVrfctnMtd.setter
	def PINVrfctnMtd(self, value):
		self._PINVrfctnMtd = value if value is not None else base_types.UninitialisedField(self, 'PINVrfctnMtd', Max35Text, False)

	@PINVrfctnMtd.deleter
	def PINVrfctnMtd(self):
		del self._PINVrfctnMtd
		self._PINVrfctnMtd = base_types.UninitialisedField(self, 'PINVrfctnMtd', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BeepKeyFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrPIN', type=OnLinePIN11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINReqTp', type=PINRequestType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PINVrfctnMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))