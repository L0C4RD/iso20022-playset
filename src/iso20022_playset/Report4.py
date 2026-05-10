import base_types
import StatementBasis6Choice
import Frequency8Choice
import YesNoIndicator
import DatePeriodDetails
import UpdateType4Choice
import Max35Text
import DateAndDateTimeChoice
import StatementSource1Choice
import Max5NumericText

class Report4(base_types._BaseFieldType):

	__slots__ = ["_QryRef", "_RptDtTm", "_ActvtyInd", "_RptId", "_CreDtTm", "_RptBsis", "_RptSrc", "_Frqcy", "_UpdTp", "_AudtdInd", "_RptPrd", "_PrvsRptDtTm", "_RptNb"]
	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if type(value) != auto else self.make_default("RptDtTm")

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = None

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
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def RptBsis(self):
		return self._RptBsis

	@RptBsis.setter
	def RptBsis(self, value):
		self._RptBsis = value if type(value) != auto else self.make_default("RptBsis")

	@RptBsis.deleter
	def RptBsis(self):
		del self._RptBsis
		self._RptBsis = None

	@property
	def RptSrc(self):
		return self._RptSrc

	@RptSrc.setter
	def RptSrc(self, value):
		self._RptSrc = value if type(value) != auto else self.make_default("RptSrc")

	@RptSrc.deleter
	def RptSrc(self):
		del self._RptSrc
		self._RptSrc = None

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
	def AudtdInd(self):
		return self._AudtdInd

	@AudtdInd.setter
	def AudtdInd(self, value):
		self._AudtdInd = value if type(value) != auto else self.make_default("AudtdInd")

	@AudtdInd.deleter
	def AudtdInd(self):
		del self._AudtdInd
		self._AudtdInd = None

	@property
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if type(value) != auto else self.make_default("RptPrd")

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = None

	@property
	def PrvsRptDtTm(self):
		return self._PrvsRptDtTm

	@PrvsRptDtTm.setter
	def PrvsRptDtTm(self, value):
		self._PrvsRptDtTm = value if type(value) != auto else self.make_default("PrvsRptDtTm")

	@PrvsRptDtTm.deleter
	def PrvsRptDtTm(self):
		del self._PrvsRptDtTm
		self._PrvsRptDtTm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptBsis', type=StatementBasis6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSrc', type=StatementSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AudtdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=DatePeriodDetails, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRptDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
	))

