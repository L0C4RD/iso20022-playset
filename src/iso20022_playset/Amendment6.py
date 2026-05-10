from . import base_types
import Max2000Text
import UndertakingAmendmentMessage1
import Max35Text

class Amendment6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApplcntRefNb", "_UdrtkgAmdmntMsg"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if type(value) != auto else self.make_default("ApplcntRefNb")

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = None

	@property
	def UdrtkgAmdmntMsg(self):
		return self._UdrtkgAmdmntMsg

	@UdrtkgAmdmntMsg.setter
	def UdrtkgAmdmntMsg(self, value):
		self._UdrtkgAmdmntMsg = value if type(value) != auto else self.make_default("UdrtkgAmdmntMsg")

	@UdrtkgAmdmntMsg.deleter
	def UdrtkgAmdmntMsg(self):
		del self._UdrtkgAmdmntMsg
		self._UdrtkgAmdmntMsg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntMsg', type=UndertakingAmendmentMessage1, min=1, max=1, mutex_group=None, array=False),
	))

