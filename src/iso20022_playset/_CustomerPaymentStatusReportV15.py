# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader128
from . import OriginalGroupHeader22
from . import OriginalPaymentInstruction56
from . import SupplementaryData1

class CustomerPaymentStatusReportV15(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlGrpInfAndSts", "_OrgnlPmtInfAndSts", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader128, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader128, False)

	@property
	def OrgnlGrpInfAndSts(self):
		return self._OrgnlGrpInfAndSts

	@OrgnlGrpInfAndSts.setter
	def OrgnlGrpInfAndSts(self, value):
		self._OrgnlGrpInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInfAndSts', OriginalGroupHeader22, False)

	@OrgnlGrpInfAndSts.deleter
	def OrgnlGrpInfAndSts(self):
		del self._OrgnlGrpInfAndSts
		self._OrgnlGrpInfAndSts = base_types.UninitialisedField(self, 'OrgnlGrpInfAndSts', OriginalGroupHeader22, False)

	@property
	def OrgnlPmtInfAndSts(self):
		return self._OrgnlPmtInfAndSts

	@OrgnlPmtInfAndSts.setter
	def OrgnlPmtInfAndSts(self, value):
		self._OrgnlPmtInfAndSts = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInfAndSts', OriginalPaymentInstruction56, True)

	@OrgnlPmtInfAndSts.deleter
	def OrgnlPmtInfAndSts(self):
		del self._OrgnlPmtInfAndSts
		self._OrgnlPmtInfAndSts = base_types.UninitialisedField(self, 'OrgnlPmtInfAndSts', OriginalPaymentInstruction56, True)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader128, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInfAndSts', type=OriginalGroupHeader22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndSts', type=OriginalPaymentInstruction56, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))