import base_types
import SupplementaryData1
import Case6
import InvestigationRejectionJustification1
import CaseAssignment6

class RejectInvestigationV07(base_types._BaseFieldType):

	__slots__ = ["_Justfn", "_SplmtryData", "_Assgnmt", "_Case"]
	@property
	def Justfn(self):
		return self._Justfn

	@Justfn.setter
	def Justfn(self, value):
		self._Justfn = value if type(value) != auto else self.make_default("Justfn")

	@Justfn.deleter
	def Justfn(self):
		del self._Justfn
		self._Justfn = None

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
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Justfn', type=InvestigationRejectionJustification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
	))

