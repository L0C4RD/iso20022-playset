# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMessageFunction2
from . import ISODateTime
from . import Max35Text
from . import Max3NumericText
from . import Max6Text
from . import Traceability4

class Header33(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_InitgPty", "_MsgFctn", "_PrcStat", "_PrtcolVrsn", "_RcptPty", "_Tracblt", "_XchgId"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', Max35Text, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', Max35Text, False)

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if value is not None else base_types.UninitialisedField(self, 'MsgFctn', ATMMessageFunction2, False)

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = base_types.UninitialisedField(self, 'MsgFctn', ATMMessageFunction2, False)

	@property
	def PrcStat(self):
		return self._PrcStat

	@PrcStat.setter
	def PrcStat(self, value):
		self._PrcStat = value if value is not None else base_types.UninitialisedField(self, 'PrcStat', Max35Text, False)

	@PrcStat.deleter
	def PrcStat(self):
		del self._PrcStat
		self._PrcStat = base_types.UninitialisedField(self, 'PrcStat', Max35Text, False)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max6Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max6Text, False)

	@property
	def RcptPty(self):
		return self._RcptPty

	@RcptPty.setter
	def RcptPty(self, value):
		self._RcptPty = value if value is not None else base_types.UninitialisedField(self, 'RcptPty', Max35Text, False)

	@RcptPty.deleter
	def RcptPty(self):
		del self._RcptPty
		self._RcptPty = base_types.UninitialisedField(self, 'RcptPty', Max35Text, False)

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if value is not None else base_types.UninitialisedField(self, 'Tracblt', Traceability4, True)

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = base_types.UninitialisedField(self, 'Tracblt', Traceability4, True)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max3NumericText, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max3NumericText, False)

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