# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FloatingRateIdentification8Choice
from . import ISINOct2015Identifier
from . import InterestComputationMethodFormat7
from . import InterestRateContractTerm4
from . import InterestRateFrequency3Choice
from . import Max350Text
from . import ResetDateAndValue1
from . import SecuritiesTransactionPrice20Choice

class FloatingRate13(base_types._BaseFieldType):

	__slots__ = ["_DayCnt", "_Id", "_LastFltgRst", "_Nm", "_NxtFltgRst", "_PmtFrqcy", "_Rate", "_RefPrd", "_RstFrqcy", "_Sprd"]
	@property
	def DayCnt(self):
		return self._DayCnt

	@DayCnt.setter
	def DayCnt(self, value):
		self._DayCnt = value if value is not None else base_types.UninitialisedField(self, 'DayCnt', InterestComputationMethodFormat7, False)

	@DayCnt.deleter
	def DayCnt(self):
		del self._DayCnt
		self._DayCnt = base_types.UninitialisedField(self, 'DayCnt', InterestComputationMethodFormat7, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def LastFltgRst(self):
		return self._LastFltgRst

	@LastFltgRst.setter
	def LastFltgRst(self, value):
		self._LastFltgRst = value if value is not None else base_types.UninitialisedField(self, 'LastFltgRst', ResetDateAndValue1, False)

	@LastFltgRst.deleter
	def LastFltgRst(self):
		del self._LastFltgRst
		self._LastFltgRst = base_types.UninitialisedField(self, 'LastFltgRst', ResetDateAndValue1, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def NxtFltgRst(self):
		return self._NxtFltgRst

	@NxtFltgRst.setter
	def NxtFltgRst(self, value):
		self._NxtFltgRst = value if value is not None else base_types.UninitialisedField(self, 'NxtFltgRst', ResetDateAndValue1, False)

	@NxtFltgRst.deleter
	def NxtFltgRst(self):
		del self._NxtFltgRst
		self._NxtFltgRst = base_types.UninitialisedField(self, 'NxtFltgRst', ResetDateAndValue1, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateFrequency3Choice, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateFrequency3Choice, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', FloatingRateIdentification8Choice, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', FloatingRateIdentification8Choice, False)

	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if value is not None else base_types.UninitialisedField(self, 'RefPrd', InterestRateContractTerm4, False)

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = base_types.UninitialisedField(self, 'RefPrd', InterestRateContractTerm4, False)

	@property
	def RstFrqcy(self):
		return self._RstFrqcy

	@RstFrqcy.setter
	def RstFrqcy(self, value):
		self._RstFrqcy = value if value is not None else base_types.UninitialisedField(self, 'RstFrqcy', InterestRateFrequency3Choice, False)

	@RstFrqcy.deleter
	def RstFrqcy(self):
		del self._RstFrqcy
		self._RstFrqcy = base_types.UninitialisedField(self, 'RstFrqcy', InterestRateFrequency3Choice, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice20Choice, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice20Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCnt', type=InterestComputationMethodFormat7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastFltgRst', type=ResetDateAndValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFltgRst', type=ResetDateAndValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=FloatingRateIdentification8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPrd', type=InterestRateContractTerm4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstFrqcy', type=InterestRateFrequency3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice20Choice, min=0, max=1, mutex_group=None, array=False),
	))