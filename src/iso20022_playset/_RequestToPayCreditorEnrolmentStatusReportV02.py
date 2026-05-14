# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EnrolmentHeader3 import EnrolmentHeader3
from ._EnrolmentStatus3 import EnrolmentStatus3
from ._SupplementaryData1 import SupplementaryData1

class RequestToPayCreditorEnrolmentStatusReportV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_OrgnlEnrlmntAndSts", "_SplmtryData"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def OrgnlEnrlmntAndSts(self):
		return self._OrgnlEnrlmntAndSts

	@OrgnlEnrlmntAndSts.setter
	def OrgnlEnrlmntAndSts(self, value):
		self._OrgnlEnrlmntAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlEnrlmntAndSts")

	@OrgnlEnrlmntAndSts.deleter
	def OrgnlEnrlmntAndSts(self):
		del self._OrgnlEnrlmntAndSts
		self._OrgnlEnrlmntAndSts = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=EnrolmentHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmntAndSts', type=EnrolmentStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))