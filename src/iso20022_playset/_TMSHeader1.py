# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification176
from . import GenericIdentification177
from . import ISODateTime
from . import Max6Text
from . import Number
from . import Traceability8
from . import TrueFalseIndicator

class TMSHeader1(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_DwnldTrf", "_FrmtVrsn", "_InitgPty", "_RcptPty", "_Tracblt", "_XchgId"]
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
	def DwnldTrf(self):
		return self._DwnldTrf

	@DwnldTrf.setter
	def DwnldTrf(self, value):
		self._DwnldTrf = value if value is not None else base_types.UninitialisedField(self, 'DwnldTrf', TrueFalseIndicator, False)

	@DwnldTrf.deleter
	def DwnldTrf(self):
		del self._DwnldTrf
		self._DwnldTrf = base_types.UninitialisedField(self, 'DwnldTrf', TrueFalseIndicator, False)

	@property
	def FrmtVrsn(self):
		return self._FrmtVrsn

	@FrmtVrsn.setter
	def FrmtVrsn(self, value):
		self._FrmtVrsn = value if value is not None else base_types.UninitialisedField(self, 'FrmtVrsn', Max6Text, False)

	@FrmtVrsn.deleter
	def FrmtVrsn(self):
		del self._FrmtVrsn
		self._FrmtVrsn = base_types.UninitialisedField(self, 'FrmtVrsn', Max6Text, False)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', GenericIdentification176, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', GenericIdentification176, False)

	@property
	def RcptPty(self):
		return self._RcptPty

	@RcptPty.setter
	def RcptPty(self, value):
		self._RcptPty = value if value is not None else base_types.UninitialisedField(self, 'RcptPty', GenericIdentification177, False)

	@RcptPty.deleter
	def RcptPty(self):
		del self._RcptPty
		self._RcptPty = base_types.UninitialisedField(self, 'RcptPty', GenericIdentification177, False)

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if value is not None else base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Number, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DwnldTrf', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmtVrsn', type=Max6Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPty', type=GenericIdentification177, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XchgId', type=Number, min=1, max=1, mutex_group=None, array=False),
	))