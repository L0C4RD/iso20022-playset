# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EnrolmentHeader3
from . import EnrolmentStatus3
from . import SupplementaryData1

class RequestToPayCreditorEnrolmentStatusReportV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_OrgnlEnrlmntAndSts", "_SplmtryData"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', EnrolmentHeader3, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', EnrolmentHeader3, False)

	@property
	def OrgnlEnrlmntAndSts(self):
		return self._OrgnlEnrlmntAndSts

	@OrgnlEnrlmntAndSts.setter
	def OrgnlEnrlmntAndSts(self, value):
		self._OrgnlEnrlmntAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEnrlmntAndSts', EnrolmentStatus3, True)

	@OrgnlEnrlmntAndSts.deleter
	def OrgnlEnrlmntAndSts(self):
		del self._OrgnlEnrlmntAndSts
		self._OrgnlEnrlmntAndSts = base_types.UninitialisedField(self, 'OrgnlEnrlmntAndSts', EnrolmentStatus3, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=EnrolmentHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmntAndSts', type=EnrolmentStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))