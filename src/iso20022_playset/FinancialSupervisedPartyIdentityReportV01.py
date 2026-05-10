from . import base_types
import SupplementaryData1
import PartyReport1Choice

class FinancialSupervisedPartyIdentityReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_PtyData"]
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
	def PtyData(self):
		return self._PtyData

	@PtyData.setter
	def PtyData(self, value):
		self._PtyData = value if type(value) != auto else self.make_default("PtyData")

	@PtyData.deleter
	def PtyData(self):
		del self._PtyData
		self._PtyData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyData', type=PartyReport1Choice, min=1, max=None, mutex_group=None, array=True),
	))

