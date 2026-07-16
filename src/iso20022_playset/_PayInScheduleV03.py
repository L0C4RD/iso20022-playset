# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceStatus2
from . import PartyIdentification73Choice
from . import PayInFactors1
from . import PayInScheduleItems1
from . import ReportData4
from . import SupplementaryData1

class PayInScheduleV03(base_types._BaseFieldType):

	__slots__ = ["_PayInFctrs", "_PayInSchdlItm", "_PayInSchdlLngBal", "_PtyId", "_RptData", "_SplmtryData"]
	@property
	def PayInFctrs(self):
		return self._PayInFctrs

	@PayInFctrs.setter
	def PayInFctrs(self, value):
		self._PayInFctrs = value if value is not None else base_types.UninitialisedField(self, 'PayInFctrs', PayInFactors1, False)

	@PayInFctrs.deleter
	def PayInFctrs(self):
		del self._PayInFctrs
		self._PayInFctrs = base_types.UninitialisedField(self, 'PayInFctrs', PayInFactors1, False)

	@property
	def PayInSchdlItm(self):
		return self._PayInSchdlItm

	@PayInSchdlItm.setter
	def PayInSchdlItm(self, value):
		self._PayInSchdlItm = value if value is not None else base_types.UninitialisedField(self, 'PayInSchdlItm', PayInScheduleItems1, True)

	@PayInSchdlItm.deleter
	def PayInSchdlItm(self):
		del self._PayInSchdlItm
		self._PayInSchdlItm = base_types.UninitialisedField(self, 'PayInSchdlItm', PayInScheduleItems1, True)

	@property
	def PayInSchdlLngBal(self):
		return self._PayInSchdlLngBal

	@PayInSchdlLngBal.setter
	def PayInSchdlLngBal(self, value):
		self._PayInSchdlLngBal = value if value is not None else base_types.UninitialisedField(self, 'PayInSchdlLngBal', BalanceStatus2, True)

	@PayInSchdlLngBal.deleter
	def PayInSchdlLngBal(self):
		del self._PayInSchdlLngBal
		self._PayInSchdlLngBal = base_types.UninitialisedField(self, 'PayInSchdlLngBal', BalanceStatus2, True)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification73Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification73Choice, False)

	@property
	def RptData(self):
		return self._RptData

	@RptData.setter
	def RptData(self, value):
		self._RptData = value if value is not None else base_types.UninitialisedField(self, 'RptData', ReportData4, False)

	@RptData.deleter
	def RptData(self):
		del self._RptData
		self._RptData = base_types.UninitialisedField(self, 'RptData', ReportData4, False)

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
		base_types.FieldEntry(name='PayInFctrs', type=PayInFactors1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PayInSchdlItm', type=PayInScheduleItems1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PayInSchdlLngBal', type=BalanceStatus2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification73Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptData', type=ReportData4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))