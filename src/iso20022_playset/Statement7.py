import base_types
import FrequencyCodeAndDSSCode1Choice
import DateAndDateTimeChoice
import Max35Text
import Max5NumericText
import YesNoIndicator
import StatementBasisCodeAndDSSCodeChoice
import StatementUpdateTypeCodeAndDSSCodeChoice

class Statement7(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_StmtBsis", "_StmtDtTm", "_RptNb", "_UpdTp", "_CreDtTm", "_Frqcy", "_Ref"]
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
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtBsis', type=StatementBasisCodeAndDSSCodeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateTypeCodeAndDSSCodeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=FrequencyCodeAndDSSCode1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

