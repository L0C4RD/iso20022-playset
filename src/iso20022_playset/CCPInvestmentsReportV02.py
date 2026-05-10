import base_types
import SupplementaryData1
import Investment2Choice

class CCPInvestmentsReportV02(base_types._BaseFieldType):

	__slots__ = ["_Invstmt", "_SplmtryData"]
	@property
	def Invstmt(self):
		return self._Invstmt

	@Invstmt.setter
	def Invstmt(self, value):
		self._Invstmt = value if type(value) != auto else self.make_default("Invstmt")

	@Invstmt.deleter
	def Invstmt(self):
		del self._Invstmt
		self._Invstmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstmt', type=Investment2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

