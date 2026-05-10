from . import base_types
import OriginalPaymentInstruction51
import OriginalGroupHeader22
import SupplementaryData1
import GroupHeader128

class CustomerPaymentStatusReportV14(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlPmtInfAndSts", "_SplmtryData", "_OrgnlGrpInfAndSts"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def OrgnlPmtInfAndSts(self):
		return self._OrgnlPmtInfAndSts

	@OrgnlPmtInfAndSts.setter
	def OrgnlPmtInfAndSts(self, value):
		self._OrgnlPmtInfAndSts = value if type(value) != auto else self.make_default("OrgnlPmtInfAndSts")

	@OrgnlPmtInfAndSts.deleter
	def OrgnlPmtInfAndSts(self):
		del self._OrgnlPmtInfAndSts
		self._OrgnlPmtInfAndSts = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def OrgnlGrpInfAndSts(self):
		return self._OrgnlGrpInfAndSts

	@OrgnlGrpInfAndSts.setter
	def OrgnlGrpInfAndSts(self, value):
		self._OrgnlGrpInfAndSts = value if type(value) != auto else self.make_default("OrgnlGrpInfAndSts")

	@OrgnlGrpInfAndSts.deleter
	def OrgnlGrpInfAndSts(self):
		del self._OrgnlGrpInfAndSts
		self._OrgnlGrpInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader128, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndSts', type=OriginalPaymentInstruction51, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlGrpInfAndSts', type=OriginalGroupHeader22, min=1, max=1, mutex_group=None, array=False),
	))

