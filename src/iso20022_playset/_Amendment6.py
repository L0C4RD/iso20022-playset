# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2000Text
from . import Max35Text
from . import UndertakingAmendmentMessage1

class Amendment6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApplcntRefNb", "_UdrtkgAmdmntMsg"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if value is not None else base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

	@property
	def UdrtkgAmdmntMsg(self):
		return self._UdrtkgAmdmntMsg

	@UdrtkgAmdmntMsg.setter
	def UdrtkgAmdmntMsg(self, value):
		self._UdrtkgAmdmntMsg = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntMsg', UndertakingAmendmentMessage1, False)

	@UdrtkgAmdmntMsg.deleter
	def UdrtkgAmdmntMsg(self):
		del self._UdrtkgAmdmntMsg
		self._UdrtkgAmdmntMsg = base_types.UninitialisedField(self, 'UdrtkgAmdmntMsg', UndertakingAmendmentMessage1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntMsg', type=UndertakingAmendmentMessage1, min=1, max=1, mutex_group=None, array=False),
	))