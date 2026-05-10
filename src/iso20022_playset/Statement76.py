import base_types
import UpdateType16Choice
import RestrictedFINXMax16Text
import Number3Choice
import YesNoIndicator
import StatementBasis9Choice
import Frequency26Choice
import DateAndDateTime2Choice

class Statement76(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_StmtBsis", "_RptNb", "_AudtdInd", "_SubAcctInd", "_QryRef", "_TaxLotInd", "_UpdTp", "_Frqcy", "_SctyIntrstOrSetOff", "_StmtId", "_StmtDtTm"]
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
	def StmtBsis(self):
		return self._StmtBsis

	@StmtBsis.setter
	def StmtBsis(self, value):
		self._StmtBsis = value if type(value) != auto else self.make_default("StmtBsis")

	@StmtBsis.deleter
	def StmtBsis(self):
		del self._StmtBsis
		self._StmtBsis = None

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
	def SubAcctInd(self):
		return self._SubAcctInd

	@SubAcctInd.setter
	def SubAcctInd(self, value):
		self._SubAcctInd = value if type(value) != auto else self.make_default("SubAcctInd")

	@SubAcctInd.deleter
	def SubAcctInd(self):
		del self._SubAcctInd
		self._SubAcctInd = None

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
	def TaxLotInd(self):
		return self._TaxLotInd

	@TaxLotInd.setter
	def TaxLotInd(self, value):
		self._TaxLotInd = value if type(value) != auto else self.make_default("TaxLotInd")

	@TaxLotInd.deleter
	def TaxLotInd(self):
		del self._TaxLotInd
		self._TaxLotInd = None

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
	def SctyIntrstOrSetOff(self):
		return self._SctyIntrstOrSetOff

	@SctyIntrstOrSetOff.setter
	def SctyIntrstOrSetOff(self, value):
		self._SctyIntrstOrSetOff = value if type(value) != auto else self.make_default("SctyIntrstOrSetOff")

	@SctyIntrstOrSetOff.deleter
	def SctyIntrstOrSetOff(self):
		del self._SctyIntrstOrSetOff
		self._SctyIntrstOrSetOff = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasis9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AudtdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxLotInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency26Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyIntrstOrSetOff', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

