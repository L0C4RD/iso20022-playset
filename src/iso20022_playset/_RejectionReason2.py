from . import base_types
from ._ISODateTime import ISODateTime
from ._Max20000Text import Max20000Text
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text

class RejectionReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_ErrLctn", "_RjctgPtyRsn", "_RjctnDtTm", "_RsnDesc"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def ErrLctn(self):
		return self._ErrLctn

	@ErrLctn.setter
	def ErrLctn(self, value):
		self._ErrLctn = value if type(value) != base_types.auto else self.make_default("ErrLctn")

	@ErrLctn.deleter
	def ErrLctn(self):
		del self._ErrLctn
		self._ErrLctn = None

	@property
	def RjctgPtyRsn(self):
		return self._RjctgPtyRsn

	@RjctgPtyRsn.setter
	def RjctgPtyRsn(self, value):
		self._RjctgPtyRsn = value if type(value) != base_types.auto else self.make_default("RjctgPtyRsn")

	@RjctgPtyRsn.deleter
	def RjctgPtyRsn(self):
		del self._RjctgPtyRsn
		self._RjctgPtyRsn = None

	@property
	def RjctnDtTm(self):
		return self._RjctnDtTm

	@RjctnDtTm.setter
	def RjctnDtTm(self, value):
		self._RjctnDtTm = value if type(value) != base_types.auto else self.make_default("RjctnDtTm")

	@RjctnDtTm.deleter
	def RjctnDtTm(self):
		del self._RjctnDtTm
		self._RjctnDtTm = None

	@property
	def RsnDesc(self):
		return self._RsnDesc

	@RsnDesc.setter
	def RsnDesc(self, value):
		self._RsnDesc = value if type(value) != base_types.auto else self.make_default("RsnDesc")

	@RsnDesc.deleter
	def RsnDesc(self):
		del self._RsnDesc
		self._RsnDesc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrLctn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctgPtyRsn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

