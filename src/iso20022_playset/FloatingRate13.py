import base_types
import InterestComputationMethodFormat7
import ResetDateAndValue1
import Max350Text
import SecuritiesTransactionPrice20Choice
import InterestRateFrequency3Choice
import FloatingRateIdentification8Choice
import ISINOct2015Identifier
import InterestRateContractTerm4

class FloatingRate13(base_types._BaseFieldType):

	__slots__ = ["_PmtFrqcy", "_DayCnt", "_RstFrqcy", "_RefPrd", "_NxtFltgRst", "_Rate", "_Id", "_Nm", "_Sprd", "_LastFltgRst"]
	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def DayCnt(self):
		return self._DayCnt

	@DayCnt.setter
	def DayCnt(self, value):
		self._DayCnt = value if type(value) != auto else self.make_default("DayCnt")

	@DayCnt.deleter
	def DayCnt(self):
		del self._DayCnt
		self._DayCnt = None

	@property
	def RstFrqcy(self):
		return self._RstFrqcy

	@RstFrqcy.setter
	def RstFrqcy(self, value):
		self._RstFrqcy = value if type(value) != auto else self.make_default("RstFrqcy")

	@RstFrqcy.deleter
	def RstFrqcy(self):
		del self._RstFrqcy
		self._RstFrqcy = None

	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if type(value) != auto else self.make_default("RefPrd")

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = None

	@property
	def NxtFltgRst(self):
		return self._NxtFltgRst

	@NxtFltgRst.setter
	def NxtFltgRst(self, value):
		self._NxtFltgRst = value if type(value) != auto else self.make_default("NxtFltgRst")

	@NxtFltgRst.deleter
	def NxtFltgRst(self):
		del self._NxtFltgRst
		self._NxtFltgRst = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def LastFltgRst(self):
		return self._LastFltgRst

	@LastFltgRst.setter
	def LastFltgRst(self, value):
		self._LastFltgRst = value if type(value) != auto else self.make_default("LastFltgRst")

	@LastFltgRst.deleter
	def LastFltgRst(self):
		del self._LastFltgRst
		self._LastFltgRst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCnt', type=InterestComputationMethodFormat7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPrd', type=InterestRateContractTerm4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFltgRst', type=ResetDateAndValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=FloatingRateIdentification8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastFltgRst', type=ResetDateAndValue1, min=0, max=1, mutex_group=None, array=False),
	))

