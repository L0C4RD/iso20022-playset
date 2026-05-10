import base_types
import IntraDayMarginCall1
import EndOfDayRequirement2
import DefaultFundRequirement1
import SupplementaryData1
import IntraDayRequirement1

class CCPMemberRequirementsReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_DfltFndRqrmnt", "_EndOfDayRqrmnt", "_IntraDayRqrmntAmt", "_IntraDayMrgnCall"]
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
	def DfltFndRqrmnt(self):
		return self._DfltFndRqrmnt

	@DfltFndRqrmnt.setter
	def DfltFndRqrmnt(self, value):
		self._DfltFndRqrmnt = value if type(value) != auto else self.make_default("DfltFndRqrmnt")

	@DfltFndRqrmnt.deleter
	def DfltFndRqrmnt(self):
		del self._DfltFndRqrmnt
		self._DfltFndRqrmnt = None

	@property
	def EndOfDayRqrmnt(self):
		return self._EndOfDayRqrmnt

	@EndOfDayRqrmnt.setter
	def EndOfDayRqrmnt(self, value):
		self._EndOfDayRqrmnt = value if type(value) != auto else self.make_default("EndOfDayRqrmnt")

	@EndOfDayRqrmnt.deleter
	def EndOfDayRqrmnt(self):
		del self._EndOfDayRqrmnt
		self._EndOfDayRqrmnt = None

	@property
	def IntraDayRqrmntAmt(self):
		return self._IntraDayRqrmntAmt

	@IntraDayRqrmntAmt.setter
	def IntraDayRqrmntAmt(self, value):
		self._IntraDayRqrmntAmt = value if type(value) != auto else self.make_default("IntraDayRqrmntAmt")

	@IntraDayRqrmntAmt.deleter
	def IntraDayRqrmntAmt(self):
		del self._IntraDayRqrmntAmt
		self._IntraDayRqrmntAmt = None

	@property
	def IntraDayMrgnCall(self):
		return self._IntraDayMrgnCall

	@IntraDayMrgnCall.setter
	def IntraDayMrgnCall(self, value):
		self._IntraDayMrgnCall = value if type(value) != auto else self.make_default("IntraDayMrgnCall")

	@IntraDayMrgnCall.deleter
	def IntraDayMrgnCall(self):
		del self._IntraDayMrgnCall
		self._IntraDayMrgnCall = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltFndRqrmnt', type=DefaultFundRequirement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndOfDayRqrmnt', type=EndOfDayRequirement2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntraDayRqrmntAmt', type=IntraDayRequirement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntraDayMrgnCall', type=IntraDayMarginCall1, min=0, max=None, mutex_group=None, array=True),
	))

