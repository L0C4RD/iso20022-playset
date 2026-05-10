from . import base_types
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SupplementaryData1 import SupplementaryData1
from ._SettlementParties37Choice import SettlementParties37Choice
from ._Pagination1 import Pagination1
from ._ReportParameters8 import ReportParameters8
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._Report7 import Report7

class SettlementObligationReportV04(base_types._BaseFieldType):

	__slots__ = ["_SttlmPties", "_RptParams", "_DlvryAcct", "_ClrMmb", "_Pgntn", "_ClrSgmt", "_RptDtls", "_SplmtryData"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != base_types.auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if type(value) != base_types.auto else self.make_default("DlvryAcct")

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if type(value) != base_types.auto else self.make_default("RptDtls")

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = None

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if type(value) != base_types.auto else self.make_default("RptParams")

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = None

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
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if type(value) != base_types.auto else self.make_default("SttlmPties")

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtls', type=Report7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptParams', type=ReportParameters8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties37Choice, min=0, max=1, mutex_group=None, array=False),
	))

