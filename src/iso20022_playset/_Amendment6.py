from . import base_types
from .Max35Text import Max35Text
from .UndertakingAmendmentMessage1 import UndertakingAmendmentMessage1
from .Max2000Text import Max2000Text

class Amendment6(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntMsg", "_AddtlInf", "_ApplcntRefNb"]
	@property
	def UdrtkgAmdmntMsg(self):
		return self._UdrtkgAmdmntMsg

	@UdrtkgAmdmntMsg.setter
	def UdrtkgAmdmntMsg(self, value):
		self._UdrtkgAmdmntMsg = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntMsg")

	@UdrtkgAmdmntMsg.deleter
	def UdrtkgAmdmntMsg(self):
		del self._UdrtkgAmdmntMsg
		self._UdrtkgAmdmntMsg = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if type(value) != base_types.auto else self.make_default("ApplcntRefNb")

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntMsg', type=UndertakingAmendmentMessage1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

