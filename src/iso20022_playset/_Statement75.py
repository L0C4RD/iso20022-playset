# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionStatementReportingType1Code
from . import CorporateActionStatementType2Code
from . import DateAndDateTime2Choice
from . import DateOrDateTimePeriod1Choice
from . import DatePeriod2
from . import Frequency26Choice
from . import Max5NumericText
from . import RestrictedFINXMax16Text
from . import UpdateType16Choice
from . import YesNoIndicator

class Statement75(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_InstrAggtnPrd", "_NtfctnDdlnPrd", "_RptNb", "_RptgTp", "_StmtDtTm", "_StmtId", "_StmtTp", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency26Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency26Choice, False)

	@property
	def InstrAggtnPrd(self):
		return self._InstrAggtnPrd

	@InstrAggtnPrd.setter
	def InstrAggtnPrd(self, value):
		self._InstrAggtnPrd = value if value is not None else base_types.UninitialisedField(self, 'InstrAggtnPrd', DatePeriod2, False)

	@InstrAggtnPrd.deleter
	def InstrAggtnPrd(self):
		del self._InstrAggtnPrd
		self._InstrAggtnPrd = base_types.UninitialisedField(self, 'InstrAggtnPrd', DatePeriod2, False)

	@property
	def NtfctnDdlnPrd(self):
		return self._NtfctnDdlnPrd

	@NtfctnDdlnPrd.setter
	def NtfctnDdlnPrd(self, value):
		self._NtfctnDdlnPrd = value if value is not None else base_types.UninitialisedField(self, 'NtfctnDdlnPrd', DateOrDateTimePeriod1Choice, False)

	@NtfctnDdlnPrd.deleter
	def NtfctnDdlnPrd(self):
		del self._NtfctnDdlnPrd
		self._NtfctnDdlnPrd = base_types.UninitialisedField(self, 'NtfctnDdlnPrd', DateOrDateTimePeriod1Choice, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Max5NumericText, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Max5NumericText, False)

	@property
	def RptgTp(self):
		return self._RptgTp

	@RptgTp.setter
	def RptgTp(self, value):
		self._RptgTp = value if value is not None else base_types.UninitialisedField(self, 'RptgTp', CorporateActionStatementReportingType1Code, False)

	@RptgTp.deleter
	def RptgTp(self):
		del self._RptgTp
		self._RptgTp = base_types.UninitialisedField(self, 'RptgTp', CorporateActionStatementReportingType1Code, False)

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTime2Choice, False)

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTime2Choice, False)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', RestrictedFINXMax16Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', RestrictedFINXMax16Text, False)

	@property
	def StmtTp(self):
		return self._StmtTp

	@StmtTp.setter
	def StmtTp(self, value):
		self._StmtTp = value if value is not None else base_types.UninitialisedField(self, 'StmtTp', CorporateActionStatementType2Code, False)

	@StmtTp.deleter
	def StmtTp(self):
		del self._StmtTp
		self._StmtTp = base_types.UninitialisedField(self, 'StmtTp', CorporateActionStatementType2Code, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType16Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType16Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency26Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrAggtnPrd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnDdlnPrd', type=DateOrDateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTp', type=CorporateActionStatementReportingType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=CorporateActionStatementType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType16Choice, min=1, max=1, mutex_group=None, array=False),
	))