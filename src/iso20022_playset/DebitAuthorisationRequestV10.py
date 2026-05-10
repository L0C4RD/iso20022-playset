from . import base_types
from .UnderlyingTransaction8Choice import UnderlyingTransaction8Choice
from .SupplementaryData1 import SupplementaryData1
from .DebitAuthorisation2 import DebitAuthorisation2
from .CaseAssignment6 import CaseAssignment6
from .Case6 import Case6

class DebitAuthorisationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_Undrlyg", "_Case", "_SplmtryData", "_Dtl", "_Assgnmt"]
	@property
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if type(value) != auto else self.make_default("Undrlyg")

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = None

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if type(value) != auto else self.make_default("Dtl")

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = None

	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Undrlyg', type=UnderlyingTransaction8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dtl', type=DebitAuthorisation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
	))

