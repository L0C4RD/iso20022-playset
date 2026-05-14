# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification32 import GenericIdentification32
from ._ISODateTime import ISODateTime
from ._Max3NumericText import Max3NumericText
from ._Max6Text import Max6Text
from ._Number import Number

class Header23(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_FrmtVrsn", "_InitgPty", "_MsgSeqNb", "_RcptPty", "_XchgId"]
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
	def FrmtVrsn(self):
		return self._FrmtVrsn

	@FrmtVrsn.setter
	def FrmtVrsn(self, value):
		self._FrmtVrsn = value if type(value) != base_types.auto else self.make_default("FrmtVrsn")

	@FrmtVrsn.deleter
	def FrmtVrsn(self):
		del self._FrmtVrsn
		self._FrmtVrsn = None

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
	def MsgSeqNb(self):
		return self._MsgSeqNb

	@MsgSeqNb.setter
	def MsgSeqNb(self, value):
		self._MsgSeqNb = value if type(value) != base_types.auto else self.make_default("MsgSeqNb")

	@MsgSeqNb.deleter
	def MsgSeqNb(self):
		del self._MsgSeqNb
		self._MsgSeqNb = None

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
		base_types.FieldEntry(name='FrmtVrsn', type=Max6Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPty', type=GenericIdentification32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))