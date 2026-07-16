# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorEnrolmentCancellation3
from . import EnrolmentHeader3
from . import SupplementaryData1

class RequestToPayCreditorEnrolmentCancellationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_CxlData", "_Hdr", "_SplmtryData"]
	@property
	def CxlData(self):
		return self._CxlData

	@CxlData.setter
	def CxlData(self, value):
		self._CxlData = value if value is not None else base_types.UninitialisedField(self, 'CxlData', CreditorEnrolmentCancellation3, True)

	@CxlData.deleter
	def CxlData(self):
		del self._CxlData
		self._CxlData = base_types.UninitialisedField(self, 'CxlData', CreditorEnrolmentCancellation3, True)

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
		base_types.FieldEntry(name='CxlData', type=CreditorEnrolmentCancellation3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=EnrolmentHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))