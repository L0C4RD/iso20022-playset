# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivationHeader3
from . import ActivationStatus3
from . import SupplementaryData1

class RequestToPayDebtorActivationStatusReportV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_OrgnlActvtnAndSts", "_SplmtryData"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', ActivationHeader3, False)

	@property
	def OrgnlActvtnAndSts(self):
		return self._OrgnlActvtnAndSts

	@OrgnlActvtnAndSts.setter
	def OrgnlActvtnAndSts(self, value):
		self._OrgnlActvtnAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlActvtnAndSts', ActivationStatus3, True)

	@OrgnlActvtnAndSts.deleter
	def OrgnlActvtnAndSts(self):
		del self._OrgnlActvtnAndSts
		self._OrgnlActvtnAndSts = base_types.UninitialisedField(self, 'OrgnlActvtnAndSts', ActivationStatus3, True)

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
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlActvtnAndSts', type=ActivationStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))