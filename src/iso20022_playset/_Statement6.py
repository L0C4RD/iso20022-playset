# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import FrequencyCodeAndDSSCode1Choice
from . import Max35Text
from . import Max5NumericText
from . import StatementBasisCodeAndDSSCodeChoice
from . import StatementUpdateTypeCodeAndDSSCodeChoice
from . import YesNoIndicator

class Statement6(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_AudtdInd", "_CreDtTm", "_Frqcy", "_Ref", "_RptNb", "_StmtBsis", "_StmtDtTm", "_UpdTp"]
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
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', FrequencyCodeAndDSSCode1Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', FrequencyCodeAndDSSCode1Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

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
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if value is not None else base_types.UninitialisedField(self, 'StmtBsis', StatementBasisCodeAndDSSCodeChoice, False)

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = base_types.UninitialisedField(self, 'StmtBsis', StatementBasisCodeAndDSSCodeChoice, False)

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTimeChoice, False)

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTimeChoice, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', StatementUpdateTypeCodeAndDSSCodeChoice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', StatementUpdateTypeCodeAndDSSCodeChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AudtdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=FrequencyCodeAndDSSCode1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasisCodeAndDSSCodeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateTypeCodeAndDSSCodeChoice, min=1, max=1, mutex_group=None, array=False),
	))