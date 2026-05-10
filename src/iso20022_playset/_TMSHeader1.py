from . import base_types
from .Number import Number
from .GenericIdentification176 import GenericIdentification176
from .TrueFalseIndicator import TrueFalseIndicator
from .Traceability8 import Traceability8
from .ISODateTime import ISODateTime
from .GenericIdentification177 import GenericIdentification177
from .Max6Text import Max6Text

class TMSHeader1(base_types._BaseFieldType):

	__slots__ = ["_InitgPty", "_CreDtTm", "_DwnldTrf", "_Tracblt", "_XchgId", "_RcptPty", "_FrmtVrsn"]
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
	def DwnldTrf(self):
		return self._DwnldTrf

	@DwnldTrf.setter
	def DwnldTrf(self, value):
		self._DwnldTrf = value if type(value) != base_types.auto else self.make_default("DwnldTrf")

	@DwnldTrf.deleter
	def DwnldTrf(self):
		del self._DwnldTrf
		self._DwnldTrf = None

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
	def FrmtVrsn(self):
		return self._FrmtVrsn

	@FrmtVrsn.setter
	def FrmtVrsn(self, value):
		self._FrmtVrsn = value if type(value) != base_types.auto else self.make_default("FrmtVrsn")

	@FrmtVrsn.deleter
	def FrmtVrsn(self):
		del self._FrmtVrsn
		self._FrmtVrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DwnldTrf', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XchgId', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPty', type=GenericIdentification177, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmtVrsn', type=Max6Text, min=1, max=1, mutex_group=None, array=False),
	))

