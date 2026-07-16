# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination1
from . import PartyIdentification253Choice
from . import Report7
from . import ReportParameters8
from . import SecuritiesAccount19
from . import SettlementParties37Choice
from . import SupplementaryData1

class SettlementObligationReportV04(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_ClrSgmt", "_DlvryAcct", "_Pgntn", "_RptDtls", "_RptParams", "_SplmtryData", "_SttlmPties"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if value is not None else base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification253Choice, False)

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if value is not None else base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = base_types.UninitialisedField(self, 'DlvryAcct', SecuritiesAccount19, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if value is not None else base_types.UninitialisedField(self, 'RptDtls', Report7, True)

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = base_types.UninitialisedField(self, 'RptDtls', Report7, True)

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if value is not None else base_types.UninitialisedField(self, 'RptParams', ReportParameters8, False)

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = base_types.UninitialisedField(self, 'RptParams', ReportParameters8, False)

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

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if value is not None else base_types.UninitialisedField(self, 'SttlmPties', SettlementParties37Choice, False)

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = base_types.UninitialisedField(self, 'SttlmPties', SettlementParties37Choice, False)

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