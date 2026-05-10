import base_types
import Frequency25Choice
import YesNoIndicator
import DatePeriod2
import DateAndDateTime2Choice
import DateOrDateTimePeriod1Choice
import CorporateActionStatementType2Code
import UpdateType15Choice
import Max35Text
import Max5NumericText
import CorporateActionStatementReportingType1Code

class Statement72(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_RptNb", "_NtfctnDdlnPrd", "_InstrAggtnPrd", "_UpdTp", "_Frqcy", "_StmtTp", "_StmtId", "_StmtDtTm", "_RptgTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def NtfctnDdlnPrd(self):
		return self._NtfctnDdlnPrd

	@NtfctnDdlnPrd.setter
	def NtfctnDdlnPrd(self, value):
		self._NtfctnDdlnPrd = value if type(value) != auto else self.make_default("NtfctnDdlnPrd")

	@NtfctnDdlnPrd.deleter
	def NtfctnDdlnPrd(self):
		del self._NtfctnDdlnPrd
		self._NtfctnDdlnPrd = None

	@property
	def InstrAggtnPrd(self):
		return self._InstrAggtnPrd

	@InstrAggtnPrd.setter
	def InstrAggtnPrd(self, value):
		self._InstrAggtnPrd = value if type(value) != auto else self.make_default("InstrAggtnPrd")

	@InstrAggtnPrd.deleter
	def InstrAggtnPrd(self):
		del self._InstrAggtnPrd
		self._InstrAggtnPrd = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def StmtTp(self):
		return self._StmtTp

	@StmtTp.setter
	def StmtTp(self, value):
		self._StmtTp = value if type(value) != auto else self.make_default("StmtTp")

	@StmtTp.deleter
	def StmtTp(self):
		del self._StmtTp
		self._StmtTp = None

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if type(value) != auto else self.make_default("StmtDtTm")

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = None

	@property
	def RptgTp(self):
		return self._RptgTp

	@RptgTp.setter
	def RptgTp(self, value):
		self._RptgTp = value if type(value) != auto else self.make_default("RptgTp")

	@RptgTp.deleter
	def RptgTp(self):
		del self._RptgTp
		self._RptgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnDdlnPrd', type=DateOrDateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrAggtnPrd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtTp', type=CorporateActionStatementType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTp', type=CorporateActionStatementReportingType1Code, min=1, max=1, mutex_group=None, array=False),
	))

