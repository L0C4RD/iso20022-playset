import base_types
import Max35Text
import AdditionalInformation30
import ActionTaken1Code
import Max256Text

class FraudDispositionStatus2(base_types._BaseFieldType):

	__slots__ = ["_OthrActnTaken", "_WrngData", "_ActnTaken", "_AddtlInf", "_ErrData"]
	@property
	def OthrActnTaken(self):
		return self._OthrActnTaken

	@OthrActnTaken.setter
	def OthrActnTaken(self, value):
		self._OthrActnTaken = value if type(value) != auto else self.make_default("OthrActnTaken")

	@OthrActnTaken.deleter
	def OthrActnTaken(self):
		del self._OthrActnTaken
		self._OthrActnTaken = None

	@property
	def WrngData(self):
		return self._WrngData

	@WrngData.setter
	def WrngData(self, value):
		self._WrngData = value if type(value) != auto else self.make_default("WrngData")

	@WrngData.deleter
	def WrngData(self):
		del self._WrngData
		self._WrngData = None

	@property
	def ActnTaken(self):
		return self._ActnTaken

	@ActnTaken.setter
	def ActnTaken(self, value):
		self._ActnTaken = value if type(value) != auto else self.make_default("ActnTaken")

	@ActnTaken.deleter
	def ActnTaken(self):
		del self._ActnTaken
		self._ActnTaken = None

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
	def ErrData(self):
		return self._ErrData

	@ErrData.setter
	def ErrData(self, value):
		self._ErrData = value if type(value) != auto else self.make_default("ErrData")

	@ErrData.deleter
	def ErrData(self):
		del self._ErrData
		self._ErrData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrActnTaken', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrngData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnTaken', type=ActionTaken1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ErrData', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
	))

