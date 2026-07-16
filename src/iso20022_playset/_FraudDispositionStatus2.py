# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionTaken1Code
from . import AdditionalInformation30
from . import Max256Text
from . import Max35Text

class FraudDispositionStatus2(base_types._BaseFieldType):

	__slots__ = ["_ActnTaken", "_AddtlInf", "_ErrData", "_OthrActnTaken", "_WrngData"]
	@property
	def ActnTaken(self):
		return self._ActnTaken

	@ActnTaken.setter
	def ActnTaken(self, value):
		self._ActnTaken = value if value is not None else base_types.UninitialisedField(self, 'ActnTaken', ActionTaken1Code, False)

	@ActnTaken.deleter
	def ActnTaken(self):
		del self._ActnTaken
		self._ActnTaken = base_types.UninitialisedField(self, 'ActnTaken', ActionTaken1Code, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation30, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation30, True)

	@property
	def ErrData(self):
		return self._ErrData

	@ErrData.setter
	def ErrData(self, value):
		self._ErrData = value if value is not None else base_types.UninitialisedField(self, 'ErrData', Max256Text, True)

	@ErrData.deleter
	def ErrData(self):
		del self._ErrData
		self._ErrData = base_types.UninitialisedField(self, 'ErrData', Max256Text, True)

	@property
	def OthrActnTaken(self):
		return self._OthrActnTaken

	@OthrActnTaken.setter
	def OthrActnTaken(self, value):
		self._OthrActnTaken = value if value is not None else base_types.UninitialisedField(self, 'OthrActnTaken', Max35Text, False)

	@OthrActnTaken.deleter
	def OthrActnTaken(self):
		del self._OthrActnTaken
		self._OthrActnTaken = base_types.UninitialisedField(self, 'OthrActnTaken', Max35Text, False)

	@property
	def WrngData(self):
		return self._WrngData

	@WrngData.setter
	def WrngData(self, value):
		self._WrngData = value if value is not None else base_types.UninitialisedField(self, 'WrngData', Max256Text, True)

	@WrngData.deleter
	def WrngData(self):
		del self._WrngData
		self._WrngData = base_types.UninitialisedField(self, 'WrngData', Max256Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTaken', type=ActionTaken1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ErrData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrActnTaken', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrngData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
	))