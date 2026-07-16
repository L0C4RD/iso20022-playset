# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import DatePeriodDetails
from . import Frequency8Choice
from . import Max35Text
from . import Max5NumericText
from . import StatementBasis6Choice
from . import StatementSource1Choice
from . import UpdateType4Choice
from . import YesNoIndicator

class Report4(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_AudtdInd", "_CreDtTm", "_Frqcy", "_PrvsRptDtTm", "_QryRef", "_RptBsis", "_RptDtTm", "_RptId", "_RptNb", "_RptPrd", "_RptSrc", "_UpdTp"]
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
	def AudtdInd(self):
		return self._AudtdInd

	@AudtdInd.setter
	def AudtdInd(self, value):
		self._AudtdInd = value if value is not None else base_types.UninitialisedField(self, 'AudtdInd', YesNoIndicator, False)

	@AudtdInd.deleter
	def AudtdInd(self):
		del self._AudtdInd
		self._AudtdInd = base_types.UninitialisedField(self, 'AudtdInd', YesNoIndicator, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTimeChoice, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTimeChoice, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency8Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency8Choice, False)

	@property
	def PrvsRptDtTm(self):
		return self._PrvsRptDtTm

	@PrvsRptDtTm.setter
	def PrvsRptDtTm(self, value):
		self._PrvsRptDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrvsRptDtTm', DateAndDateTimeChoice, False)

	@PrvsRptDtTm.deleter
	def PrvsRptDtTm(self):
		del self._PrvsRptDtTm
		self._PrvsRptDtTm = base_types.UninitialisedField(self, 'PrvsRptDtTm', DateAndDateTimeChoice, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@property
	def RptBsis(self):
		return self._RptBsis

	@RptBsis.setter
	def RptBsis(self, value):
		self._RptBsis = value if value is not None else base_types.UninitialisedField(self, 'RptBsis', StatementBasis6Choice, False)

	@RptBsis.deleter
	def RptBsis(self):
		del self._RptBsis
		self._RptBsis = base_types.UninitialisedField(self, 'RptBsis', StatementBasis6Choice, False)

	@property
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTimeChoice, False)

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTimeChoice, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max35Text, False)

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
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if value is not None else base_types.UninitialisedField(self, 'RptPrd', DatePeriodDetails, False)

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = base_types.UninitialisedField(self, 'RptPrd', DatePeriodDetails, False)

	@property
	def RptSrc(self):
		return self._RptSrc

	@RptSrc.setter
	def RptSrc(self, value):
		self._RptSrc = value if value is not None else base_types.UninitialisedField(self, 'RptSrc', StatementSource1Choice, False)

	@RptSrc.deleter
	def RptSrc(self):
		del self._RptSrc
		self._RptSrc = base_types.UninitialisedField(self, 'RptSrc', StatementSource1Choice, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType4Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AudtdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRptDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptBsis', type=StatementBasis6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=DatePeriodDetails, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSrc', type=StatementSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType4Choice, min=1, max=1, mutex_group=None, array=False),
	))