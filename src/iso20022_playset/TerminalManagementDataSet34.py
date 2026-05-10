from . import base_types
from .ManagementPlanContent13 import ManagementPlanContent13
from .Max9NumericText import Max9NumericText
from .TrueFalseIndicator import TrueFalseIndicator
from .DataSetIdentification11 import DataSetIdentification11

class TerminalManagementDataSet34(base_types._BaseFieldType):

	__slots__ = ["_LastSeq", "_SeqCntr", "_Cntt", "_Id"]
	@property
	def LastSeq(self):
		return self._LastSeq

	@LastSeq.setter
	def LastSeq(self, value):
		self._LastSeq = value if type(value) != base_types.auto else self.make_default("LastSeq")

	@LastSeq.deleter
	def LastSeq(self):
		del self._LastSeq
		self._LastSeq = None

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if type(value) != base_types.auto else self.make_default("SeqCntr")

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = None

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if type(value) != base_types.auto else self.make_default("Cntt")

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastSeq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=ManagementPlanContent13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
	))

