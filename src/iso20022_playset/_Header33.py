from . import base_types
from ._ATMMessageFunction2 import ATMMessageFunction2
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._Max6Text import Max6Text
from ._Traceability4 import Traceability4

class Header33(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_InitgPty", "_MsgFctn", "_PrcStat", "_PrtcolVrsn", "_RcptPty", "_Tracblt", "_XchgId"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if type(value) != base_types.auto else self.make_default("MsgFctn")

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = None

	@property
	def PrcStat(self):
		return self._PrcStat

	@PrcStat.setter
	def PrcStat(self, value):
		self._PrcStat = value if type(value) != base_types.auto else self.make_default("PrcStat")

	@PrcStat.deleter
	def PrcStat(self):
		del self._PrcStat
		self._PrcStat = None

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if type(value) != base_types.auto else self.make_default("PrtcolVrsn")

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = None

	@property
	def RcptPty(self):
		return self._RcptPty

	@RcptPty.setter
	def RcptPty(self, value):
		self._RcptPty = value if type(value) != base_types.auto else self.make_default("RcptPty")

	@RcptPty.deleter
	def RcptPty(self):
		del self._RcptPty
		self._RcptPty = None

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if type(value) != base_types.auto else self.make_default("Tracblt")

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=ATMMessageFunction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcStat', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max6Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XchgId', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
	))

