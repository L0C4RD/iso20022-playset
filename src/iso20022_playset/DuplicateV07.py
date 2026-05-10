from . import base_types
import Case6
import SupplementaryData1
import ProprietaryData7
import CaseAssignment6

class DuplicateV07(base_types._BaseFieldType):

	__slots__ = ["_Case", "_Dplct", "_SplmtryData", "_Assgnmt"]
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
	def Dplct(self):
		return self._Dplct

	@Dplct.setter
	def Dplct(self, value):
		self._Dplct = value if type(value) != auto else self.make_default("Dplct")

	@Dplct.deleter
	def Dplct(self):
		del self._Dplct
		self._Dplct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dplct', type=ProprietaryData7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
	))

