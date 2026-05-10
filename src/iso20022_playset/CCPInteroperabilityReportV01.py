import base_types
import SupplementaryData1
import InteroperabilityCCP1

class CCPInteroperabilityReportV01(base_types._BaseFieldType):

	__slots__ = ["_IntrprbltyCCP", "_SplmtryData"]
	@property
	def IntrprbltyCCP(self):
		return self._IntrprbltyCCP

	@IntrprbltyCCP.setter
	def IntrprbltyCCP(self, value):
		self._IntrprbltyCCP = value if type(value) != auto else self.make_default("IntrprbltyCCP")

	@IntrprbltyCCP.deleter
	def IntrprbltyCCP(self):
		del self._IntrprbltyCCP
		self._IntrprbltyCCP = None

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
		base_types.FieldEntry(name='IntrprbltyCCP', type=InteroperabilityCCP1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

