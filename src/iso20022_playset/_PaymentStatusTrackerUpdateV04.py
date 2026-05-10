from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._TrackerHeader6 import TrackerHeader6
from ._TrackerStatusAndTransaction19 import TrackerStatusAndTransaction19

class PaymentStatusTrackerUpdateV04(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_GrpHdr", "_TrckrStsAndTx"]
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
		base_types.FieldEntry(name='GrpHdr', type=TrackerHeader6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrckrStsAndTx', type=TrackerStatusAndTransaction19, min=1, max=None, mutex_group=None, array=True),
	))

