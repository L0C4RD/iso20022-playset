# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Frequency26Choice
from . import Number3Choice
from . import RestrictedFINXMax16Text
from . import StatementBasis9Choice
from . import UpdateType16Choice
from . import YesNoIndicator

class Statement76(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_AudtdInd", "_Frqcy", "_QryRef", "_RptNb", "_SctyIntrstOrSetOff", "_StmtBsis", "_StmtDtTm", "_StmtId", "_SubAcctInd", "_TaxLotInd", "_UpdTp"]
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
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', RestrictedFINXMax16Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', RestrictedFINXMax16Text, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@property
	def SctyIntrstOrSetOff(self):
		return self._SctyIntrstOrSetOff

	@SctyIntrstOrSetOff.setter
	def SctyIntrstOrSetOff(self, value):
		self._SctyIntrstOrSetOff = value if value is not None else base_types.UninitialisedField(self, 'SctyIntrstOrSetOff', YesNoIndicator, False)

	@SctyIntrstOrSetOff.deleter
	def SctyIntrstOrSetOff(self):
		del self._SctyIntrstOrSetOff
		self._SctyIntrstOrSetOff = base_types.UninitialisedField(self, 'SctyIntrstOrSetOff', YesNoIndicator, False)

	@property
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if value is not None else base_types.UninitialisedField(self, 'StmtBsis', StatementBasis9Choice, False)

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = base_types.UninitialisedField(self, 'StmtBsis', StatementBasis9Choice, False)

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
	def SubAcctInd(self):
		return self._SubAcctInd

	@SubAcctInd.setter
	def SubAcctInd(self, value):
		self._SubAcctInd = value if value is not None else base_types.UninitialisedField(self, 'SubAcctInd', YesNoIndicator, False)

	@SubAcctInd.deleter
	def SubAcctInd(self):
		del self._SubAcctInd
		self._SubAcctInd = base_types.UninitialisedField(self, 'SubAcctInd', YesNoIndicator, False)

	@property
	def TaxLotInd(self):
		return self._TaxLotInd

	@TaxLotInd.setter
	def TaxLotInd(self, value):
		self._TaxLotInd = value if value is not None else base_types.UninitialisedField(self, 'TaxLotInd', YesNoIndicator, False)

	@TaxLotInd.deleter
	def TaxLotInd(self):
		del self._TaxLotInd
		self._TaxLotInd = base_types.UninitialisedField(self, 'TaxLotInd', YesNoIndicator, False)

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
		base_types.FieldEntry(name='AudtdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency26Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyIntrstOrSetOff', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxLotInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType16Choice, min=1, max=1, mutex_group=None, array=False),
	))