from . import base_types
from ._ISODate import ISODate
from ._AssessmentOfValueRequiredUnderCOLLUKType1Code import AssessmentOfValueRequiredUnderCOLLUKType1Code
from ._OutcomeOfPRINValueAssessmentOrReviewUKType1Code import OutcomeOfPRINValueAssessmentOrReviewUKType1Code
from ._EMTDataReportingVFMUKType1Code import EMTDataReportingVFMUKType1Code
from ._Max350Text import Max350Text
from ._OtherReviewRelatedToValueAndOrChargesUKType1Code import OtherReviewRelatedToValueAndOrChargesUKType1Code
from ._OutcomeOfCOLLAssessmentOfValueUKType1Code import OutcomeOfCOLLAssessmentOfValueUKType1Code

class ValueForMoney1(base_types._BaseFieldType):

	__slots__ = ["_RvwDtUK", "_AssmntOfValReqrdUdrCOLLUK", "_FrthrInfUK", "_EMTDataRptgVFMUK", "_OutcmOfCOLLAssmntOfValUK", "_OutcmOfPRINValAssmntOrRvwUK", "_RvwNxtDueUK", "_OthrRvwRltdToValAndOrChrgsUK"]
	@property
	def AssmntOfValReqrdUdrCOLLUK(self):
		return self._AssmntOfValReqrdUdrCOLLUK

	@AssmntOfValReqrdUdrCOLLUK.setter
	def AssmntOfValReqrdUdrCOLLUK(self, value):
		self._AssmntOfValReqrdUdrCOLLUK = value if type(value) != base_types.auto else self.make_default("AssmntOfValReqrdUdrCOLLUK")

	@AssmntOfValReqrdUdrCOLLUK.deleter
	def AssmntOfValReqrdUdrCOLLUK(self):
		del self._AssmntOfValReqrdUdrCOLLUK
		self._AssmntOfValReqrdUdrCOLLUK = None

	@property
	def EMTDataRptgVFMUK(self):
		return self._EMTDataRptgVFMUK

	@EMTDataRptgVFMUK.setter
	def EMTDataRptgVFMUK(self, value):
		self._EMTDataRptgVFMUK = value if type(value) != base_types.auto else self.make_default("EMTDataRptgVFMUK")

	@EMTDataRptgVFMUK.deleter
	def EMTDataRptgVFMUK(self):
		del self._EMTDataRptgVFMUK
		self._EMTDataRptgVFMUK = None

	@property
	def FrthrInfUK(self):
		return self._FrthrInfUK

	@FrthrInfUK.setter
	def FrthrInfUK(self, value):
		self._FrthrInfUK = value if type(value) != base_types.auto else self.make_default("FrthrInfUK")

	@FrthrInfUK.deleter
	def FrthrInfUK(self):
		del self._FrthrInfUK
		self._FrthrInfUK = None

	@property
	def OthrRvwRltdToValAndOrChrgsUK(self):
		return self._OthrRvwRltdToValAndOrChrgsUK

	@OthrRvwRltdToValAndOrChrgsUK.setter
	def OthrRvwRltdToValAndOrChrgsUK(self, value):
		self._OthrRvwRltdToValAndOrChrgsUK = value if type(value) != base_types.auto else self.make_default("OthrRvwRltdToValAndOrChrgsUK")

	@OthrRvwRltdToValAndOrChrgsUK.deleter
	def OthrRvwRltdToValAndOrChrgsUK(self):
		del self._OthrRvwRltdToValAndOrChrgsUK
		self._OthrRvwRltdToValAndOrChrgsUK = None

	@property
	def OutcmOfCOLLAssmntOfValUK(self):
		return self._OutcmOfCOLLAssmntOfValUK

	@OutcmOfCOLLAssmntOfValUK.setter
	def OutcmOfCOLLAssmntOfValUK(self, value):
		self._OutcmOfCOLLAssmntOfValUK = value if type(value) != base_types.auto else self.make_default("OutcmOfCOLLAssmntOfValUK")

	@OutcmOfCOLLAssmntOfValUK.deleter
	def OutcmOfCOLLAssmntOfValUK(self):
		del self._OutcmOfCOLLAssmntOfValUK
		self._OutcmOfCOLLAssmntOfValUK = None

	@property
	def OutcmOfPRINValAssmntOrRvwUK(self):
		return self._OutcmOfPRINValAssmntOrRvwUK

	@OutcmOfPRINValAssmntOrRvwUK.setter
	def OutcmOfPRINValAssmntOrRvwUK(self, value):
		self._OutcmOfPRINValAssmntOrRvwUK = value if type(value) != base_types.auto else self.make_default("OutcmOfPRINValAssmntOrRvwUK")

	@OutcmOfPRINValAssmntOrRvwUK.deleter
	def OutcmOfPRINValAssmntOrRvwUK(self):
		del self._OutcmOfPRINValAssmntOrRvwUK
		self._OutcmOfPRINValAssmntOrRvwUK = None

	@property
	def RvwDtUK(self):
		return self._RvwDtUK

	@RvwDtUK.setter
	def RvwDtUK(self, value):
		self._RvwDtUK = value if type(value) != base_types.auto else self.make_default("RvwDtUK")

	@RvwDtUK.deleter
	def RvwDtUK(self):
		del self._RvwDtUK
		self._RvwDtUK = None

	@property
	def RvwNxtDueUK(self):
		return self._RvwNxtDueUK

	@RvwNxtDueUK.setter
	def RvwNxtDueUK(self, value):
		self._RvwNxtDueUK = value if type(value) != base_types.auto else self.make_default("RvwNxtDueUK")

	@RvwNxtDueUK.deleter
	def RvwNxtDueUK(self):
		del self._RvwNxtDueUK
		self._RvwNxtDueUK = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssmntOfValReqrdUdrCOLLUK', type=AssessmentOfValueRequiredUnderCOLLUKType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EMTDataRptgVFMUK', type=EMTDataReportingVFMUKType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrthrInfUK', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRvwRltdToValAndOrChrgsUK', type=OtherReviewRelatedToValueAndOrChargesUKType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutcmOfCOLLAssmntOfValUK', type=OutcomeOfCOLLAssessmentOfValueUKType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutcmOfPRINValAssmntOrRvwUK', type=OutcomeOfPRINValueAssessmentOrReviewUKType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvwDtUK', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvwNxtDueUK', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

