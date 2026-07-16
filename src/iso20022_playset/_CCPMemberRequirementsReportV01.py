# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DefaultFundRequirement1
from . import EndOfDayRequirement2
from . import IntraDayMarginCall1
from . import IntraDayRequirement1
from . import SupplementaryData1

class CCPMemberRequirementsReportV01(base_types._BaseFieldType):

	__slots__ = ["_DfltFndRqrmnt", "_EndOfDayRqrmnt", "_IntraDayMrgnCall", "_IntraDayRqrmntAmt", "_SplmtryData"]
	@property
	def DfltFndRqrmnt(self):
		return self._DfltFndRqrmnt

	@DfltFndRqrmnt.setter
	def DfltFndRqrmnt(self, value):
		self._DfltFndRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'DfltFndRqrmnt', DefaultFundRequirement1, True)

	@DfltFndRqrmnt.deleter
	def DfltFndRqrmnt(self):
		del self._DfltFndRqrmnt
		self._DfltFndRqrmnt = base_types.UninitialisedField(self, 'DfltFndRqrmnt', DefaultFundRequirement1, True)

	@property
	def EndOfDayRqrmnt(self):
		return self._EndOfDayRqrmnt

	@EndOfDayRqrmnt.setter
	def EndOfDayRqrmnt(self, value):
		self._EndOfDayRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayRqrmnt', EndOfDayRequirement2, True)

	@EndOfDayRqrmnt.deleter
	def EndOfDayRqrmnt(self):
		del self._EndOfDayRqrmnt
		self._EndOfDayRqrmnt = base_types.UninitialisedField(self, 'EndOfDayRqrmnt', EndOfDayRequirement2, True)

	@property
	def IntraDayMrgnCall(self):
		return self._IntraDayMrgnCall

	@IntraDayMrgnCall.setter
	def IntraDayMrgnCall(self, value):
		self._IntraDayMrgnCall = value if value is not None else base_types.UninitialisedField(self, 'IntraDayMrgnCall', IntraDayMarginCall1, True)

	@IntraDayMrgnCall.deleter
	def IntraDayMrgnCall(self):
		del self._IntraDayMrgnCall
		self._IntraDayMrgnCall = base_types.UninitialisedField(self, 'IntraDayMrgnCall', IntraDayMarginCall1, True)

	@property
	def IntraDayRqrmntAmt(self):
		return self._IntraDayRqrmntAmt

	@IntraDayRqrmntAmt.setter
	def IntraDayRqrmntAmt(self, value):
		self._IntraDayRqrmntAmt = value if value is not None else base_types.UninitialisedField(self, 'IntraDayRqrmntAmt', IntraDayRequirement1, True)

	@IntraDayRqrmntAmt.deleter
	def IntraDayRqrmntAmt(self):
		del self._IntraDayRqrmntAmt
		self._IntraDayRqrmntAmt = base_types.UninitialisedField(self, 'IntraDayRqrmntAmt', IntraDayRequirement1, True)

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
		base_types.FieldEntry(name='DfltFndRqrmnt', type=DefaultFundRequirement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndOfDayRqrmnt', type=EndOfDayRequirement2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntraDayMrgnCall', type=IntraDayMarginCall1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntraDayRqrmntAmt', type=IntraDayRequirement1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))