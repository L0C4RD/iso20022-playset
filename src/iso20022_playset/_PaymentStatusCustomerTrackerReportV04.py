# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._TrackerHeader5 import TrackerHeader5
from ._TrackerStatusAndTransaction21 import TrackerStatusAndTransaction21

class PaymentStatusCustomerTrackerReportV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_TrckrStsAndTx"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

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

	@property
	def TrckrStsAndTx(self):
		return self._TrckrStsAndTx

	@TrckrStsAndTx.setter
	def TrckrStsAndTx(self, value):
		self._TrckrStsAndTx = value if type(value) != base_types.auto else self.make_default("TrckrStsAndTx")

	@TrckrStsAndTx.deleter
	def TrckrStsAndTx(self):
		del self._TrckrStsAndTx
		self._TrckrStsAndTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=TrackerHeader5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrckrStsAndTx', type=TrackerStatusAndTransaction21, min=1, max=None, mutex_group=None, array=True),
	))