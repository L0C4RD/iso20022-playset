from . import base_types
import InstructionForAssignee1
import RequestedModification11
import Case6
import SupplementaryData1
import UnderlyingTransaction8Choice
import CaseAssignment6

class RequestToModifyPaymentV09(base_types._BaseFieldType):

	__slots__ = ["_InstrForAssgne", "_Case", "_Mod", "_Assgnmt", "_SplmtryData", "_Undrlyg"]
	@property
	def InstrForAssgne(self):
		return self._InstrForAssgne

	@InstrForAssgne.setter
	def InstrForAssgne(self, value):
		self._InstrForAssgne = value if type(value) != auto else self.make_default("InstrForAssgne")

	@InstrForAssgne.deleter
	def InstrForAssgne(self):
		del self._InstrForAssgne
		self._InstrForAssgne = None

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
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

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
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if type(value) != auto else self.make_default("Undrlyg")

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrForAssgne', type=InstructionForAssignee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=RequestedModification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Undrlyg', type=UnderlyingTransaction8Choice, min=1, max=1, mutex_group=None, array=False),
	))

