# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SupplementaryData1
from . import TrackerHeader5
from . import TrackerStatusAndTransaction18

class PaymentStatusCustomerTrackerReportV03(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_TrckrStsAndTx"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', TrackerHeader5, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', TrackerHeader5, False)

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

	@property
	def TrckrStsAndTx(self):
		return self._TrckrStsAndTx

	@TrckrStsAndTx.setter
	def TrckrStsAndTx(self, value):
		self._TrckrStsAndTx = value if value is not None else base_types.UninitialisedField(self, 'TrckrStsAndTx', TrackerStatusAndTransaction18, True)

	@TrckrStsAndTx.deleter
	def TrckrStsAndTx(self):
		del self._TrckrStsAndTx
		self._TrckrStsAndTx = base_types.UninitialisedField(self, 'TrckrStsAndTx', TrackerStatusAndTransaction18, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=TrackerHeader5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrckrStsAndTx', type=TrackerStatusAndTransaction18, min=1, max=None, mutex_group=None, array=True),
	))