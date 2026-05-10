from . import base_types
from ._GroupHeader101 import GroupHeader101
from ._OriginalGroupHeader17 import OriginalGroupHeader17
from ._PaymentTransaction130 import PaymentTransaction130
from ._SupplementaryData1 import SupplementaryData1

class FIToFIPaymentStatusReportV12(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlGrpInfAndSts", "_SplmtryData", "_TxInfAndSts"]
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
	def OrgnlGrpInfAndSts(self):
		return self._OrgnlGrpInfAndSts

	@OrgnlGrpInfAndSts.setter
	def OrgnlGrpInfAndSts(self, value):
		self._OrgnlGrpInfAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInfAndSts")

	@OrgnlGrpInfAndSts.deleter
	def OrgnlGrpInfAndSts(self):
		del self._OrgnlGrpInfAndSts
		self._OrgnlGrpInfAndSts = None

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
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if type(value) != base_types.auto else self.make_default("TxInfAndSts")

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader101, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInfAndSts', type=OriginalGroupHeader17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction130, min=0, max=None, mutex_group=None, array=True),
	))

