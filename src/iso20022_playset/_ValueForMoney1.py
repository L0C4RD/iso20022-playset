# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssessmentOfValueRequiredUnderCOLLUKType1Code
from . import EMTDataReportingVFMUKType1Code
from . import ISODate
from . import Max350Text
from . import OtherReviewRelatedToValueAndOrChargesUKType1Code
from . import OutcomeOfCOLLAssessmentOfValueUKType1Code
from . import OutcomeOfPRINValueAssessmentOrReviewUKType1Code

class ValueForMoney1(base_types._BaseFieldType):

	__slots__ = ["_AssmntOfValReqrdUdrCOLLUK", "_EMTDataRptgVFMUK", "_FrthrInfUK", "_OthrRvwRltdToValAndOrChrgsUK", "_OutcmOfCOLLAssmntOfValUK", "_OutcmOfPRINValAssmntOrRvwUK", "_RvwDtUK", "_RvwNxtDueUK"]
	@property
	def AssmntOfValReqrdUdrCOLLUK(self):
		return self._AssmntOfValReqrdUdrCOLLUK

	@AssmntOfValReqrdUdrCOLLUK.setter
	def AssmntOfValReqrdUdrCOLLUK(self, value):
		self._AssmntOfValReqrdUdrCOLLUK = value if value is not None else base_types.UninitialisedField(self, 'AssmntOfValReqrdUdrCOLLUK', AssessmentOfValueRequiredUnderCOLLUKType1Code, False)

	@AssmntOfValReqrdUdrCOLLUK.deleter
	def AssmntOfValReqrdUdrCOLLUK(self):
		del self._AssmntOfValReqrdUdrCOLLUK
		self._AssmntOfValReqrdUdrCOLLUK = base_types.UninitialisedField(self, 'AssmntOfValReqrdUdrCOLLUK', AssessmentOfValueRequiredUnderCOLLUKType1Code, False)

	@property
	def EMTDataRptgVFMUK(self):
		return self._EMTDataRptgVFMUK

	@EMTDataRptgVFMUK.setter
	def EMTDataRptgVFMUK(self, value):
		self._EMTDataRptgVFMUK = value if value is not None else base_types.UninitialisedField(self, 'EMTDataRptgVFMUK', EMTDataReportingVFMUKType1Code, False)

	@EMTDataRptgVFMUK.deleter
	def EMTDataRptgVFMUK(self):
		del self._EMTDataRptgVFMUK
		self._EMTDataRptgVFMUK = base_types.UninitialisedField(self, 'EMTDataRptgVFMUK', EMTDataReportingVFMUKType1Code, False)

	@property
	def FrthrInfUK(self):
		return self._FrthrInfUK

	@FrthrInfUK.setter
	def FrthrInfUK(self, value):
		self._FrthrInfUK = value if value is not None else base_types.UninitialisedField(self, 'FrthrInfUK', Max350Text, False)

	@FrthrInfUK.deleter
	def FrthrInfUK(self):
		del self._FrthrInfUK
		self._FrthrInfUK = base_types.UninitialisedField(self, 'FrthrInfUK', Max350Text, False)

	@property
	def OthrRvwRltdToValAndOrChrgsUK(self):
		return self._OthrRvwRltdToValAndOrChrgsUK

	@OthrRvwRltdToValAndOrChrgsUK.setter
	def OthrRvwRltdToValAndOrChrgsUK(self, value):
		self._OthrRvwRltdToValAndOrChrgsUK = value if value is not None else base_types.UninitialisedField(self, 'OthrRvwRltdToValAndOrChrgsUK', OtherReviewRelatedToValueAndOrChargesUKType1Code, False)

	@OthrRvwRltdToValAndOrChrgsUK.deleter
	def OthrRvwRltdToValAndOrChrgsUK(self):
		del self._OthrRvwRltdToValAndOrChrgsUK
		self._OthrRvwRltdToValAndOrChrgsUK = base_types.UninitialisedField(self, 'OthrRvwRltdToValAndOrChrgsUK', OtherReviewRelatedToValueAndOrChargesUKType1Code, False)

	@property
	def OutcmOfCOLLAssmntOfValUK(self):
		return self._OutcmOfCOLLAssmntOfValUK

	@OutcmOfCOLLAssmntOfValUK.setter
	def OutcmOfCOLLAssmntOfValUK(self, value):
		self._OutcmOfCOLLAssmntOfValUK = value if value is not None else base_types.UninitialisedField(self, 'OutcmOfCOLLAssmntOfValUK', OutcomeOfCOLLAssessmentOfValueUKType1Code, False)

	@OutcmOfCOLLAssmntOfValUK.deleter
	def OutcmOfCOLLAssmntOfValUK(self):
		del self._OutcmOfCOLLAssmntOfValUK
		self._OutcmOfCOLLAssmntOfValUK = base_types.UninitialisedField(self, 'OutcmOfCOLLAssmntOfValUK', OutcomeOfCOLLAssessmentOfValueUKType1Code, False)

	@property
	def OutcmOfPRINValAssmntOrRvwUK(self):
		return self._OutcmOfPRINValAssmntOrRvwUK

	@OutcmOfPRINValAssmntOrRvwUK.setter
	def OutcmOfPRINValAssmntOrRvwUK(self, value):
		self._OutcmOfPRINValAssmntOrRvwUK = value if value is not None else base_types.UninitialisedField(self, 'OutcmOfPRINValAssmntOrRvwUK', OutcomeOfPRINValueAssessmentOrReviewUKType1Code, False)

	@OutcmOfPRINValAssmntOrRvwUK.deleter
	def OutcmOfPRINValAssmntOrRvwUK(self):
		del self._OutcmOfPRINValAssmntOrRvwUK
		self._OutcmOfPRINValAssmntOrRvwUK = base_types.UninitialisedField(self, 'OutcmOfPRINValAssmntOrRvwUK', OutcomeOfPRINValueAssessmentOrReviewUKType1Code, False)

	@property
	def RvwDtUK(self):
		return self._RvwDtUK

	@RvwDtUK.setter
	def RvwDtUK(self, value):
		self._RvwDtUK = value if value is not None else base_types.UninitialisedField(self, 'RvwDtUK', ISODate, False)

	@RvwDtUK.deleter
	def RvwDtUK(self):
		del self._RvwDtUK
		self._RvwDtUK = base_types.UninitialisedField(self, 'RvwDtUK', ISODate, False)

	@property
	def RvwNxtDueUK(self):
		return self._RvwNxtDueUK

	@RvwNxtDueUK.setter
	def RvwNxtDueUK(self, value):
		self._RvwNxtDueUK = value if value is not None else base_types.UninitialisedField(self, 'RvwNxtDueUK', ISODate, False)

	@RvwNxtDueUK.deleter
	def RvwNxtDueUK(self):
		del self._RvwNxtDueUK
		self._RvwNxtDueUK = base_types.UninitialisedField(self, 'RvwNxtDueUK', ISODate, False)

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