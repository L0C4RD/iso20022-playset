from . import base_types
from ._NetworkParameters7 import NetworkParameters7
from ._Max100KBinary import Max100KBinary
from ._Number import Number

class DeviceTransmitMessageRequest2(base_types._BaseFieldType):

	__slots__ = ["_MaxTrnsmssnTm", "_DstnAdr", "_MsgToSnd", "_MaxWtgTm"]
	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if type(value) != base_types.auto else self.make_default("DstnAdr")

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = None

	@property
	def MaxTrnsmssnTm(self):
		return self._MaxTrnsmssnTm

	@MaxTrnsmssnTm.setter
	def MaxTrnsmssnTm(self, value):
		self._MaxTrnsmssnTm = value if type(value) != base_types.auto else self.make_default("MaxTrnsmssnTm")

	@MaxTrnsmssnTm.deleter
	def MaxTrnsmssnTm(self):
		del self._MaxTrnsmssnTm
		self._MaxTrnsmssnTm = None

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
	def MsgToSnd(self):
		return self._MsgToSnd

	@MsgToSnd.setter
	def MsgToSnd(self, value):
		self._MsgToSnd = value if type(value) != base_types.auto else self.make_default("MsgToSnd")

	@MsgToSnd.deleter
	def MsgToSnd(self):
		del self._MsgToSnd
		self._MsgToSnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DstnAdr', type=NetworkParameters7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxTrnsmssnTm', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToSnd', type=Max100KBinary, min=1, max=1, mutex_group=None, array=False),
	))

