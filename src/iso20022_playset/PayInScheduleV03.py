import base_types
import BalanceStatus2
import SupplementaryData1
import PartyIdentification73Choice
import PayInFactors1
import ReportData4
import PayInScheduleItems1

class PayInScheduleV03(base_types._BaseFieldType):

	__slots__ = ["_RptData", "_SplmtryData", "_PayInSchdlLngBal", "_PtyId", "_PayInFctrs", "_PayInSchdlItm"]
	@property
	def RptData(self):
		return self._RptData

	@RptData.setter
	def RptData(self, value):
		self._RptData = value if type(value) != auto else self.make_default("RptData")

	@RptData.deleter
	def RptData(self):
		del self._RptData
		self._RptData = None

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
	def PayInSchdlLngBal(self):
		return self._PayInSchdlLngBal

	@PayInSchdlLngBal.setter
	def PayInSchdlLngBal(self, value):
		self._PayInSchdlLngBal = value if type(value) != auto else self.make_default("PayInSchdlLngBal")

	@PayInSchdlLngBal.deleter
	def PayInSchdlLngBal(self):
		del self._PayInSchdlLngBal
		self._PayInSchdlLngBal = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def PayInFctrs(self):
		return self._PayInFctrs

	@PayInFctrs.setter
	def PayInFctrs(self, value):
		self._PayInFctrs = value if type(value) != auto else self.make_default("PayInFctrs")

	@PayInFctrs.deleter
	def PayInFctrs(self):
		del self._PayInFctrs
		self._PayInFctrs = None

	@property
	def PayInSchdlItm(self):
		return self._PayInSchdlItm

	@PayInSchdlItm.setter
	def PayInSchdlItm(self, value):
		self._PayInSchdlItm = value if type(value) != auto else self.make_default("PayInSchdlItm")

	@PayInSchdlItm.deleter
	def PayInSchdlItm(self):
		del self._PayInSchdlItm
		self._PayInSchdlItm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptData', type=ReportData4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PayInSchdlLngBal', type=BalanceStatus2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification73Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PayInFctrs', type=PayInFactors1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PayInSchdlItm', type=PayInScheduleItems1, min=0, max=None, mutex_group=None, array=True),
	))

