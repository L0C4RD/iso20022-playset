# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Case6
from . import CaseAssignment6
from . import InstructionForAssignee1
from . import RequestedModification11
from . import SupplementaryData1
from . import UnderlyingTransaction8Choice

class RequestToModifyPaymentV09(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_Case", "_InstrForAssgne", "_Mod", "_SplmtryData", "_Undrlyg"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if value is not None else base_types.UninitialisedField(self, 'Assgnmt', CaseAssignment6, False)

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = base_types.UninitialisedField(self, 'Assgnmt', CaseAssignment6, False)

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if value is not None else base_types.UninitialisedField(self, 'Case', Case6, False)

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = base_types.UninitialisedField(self, 'Case', Case6, False)

	@property
	def InstrForAssgne(self):
		return self._InstrForAssgne

	@InstrForAssgne.setter
	def InstrForAssgne(self, value):
		self._InstrForAssgne = value if value is not None else base_types.UninitialisedField(self, 'InstrForAssgne', InstructionForAssignee1, False)

	@InstrForAssgne.deleter
	def InstrForAssgne(self):
		del self._InstrForAssgne
		self._InstrForAssgne = base_types.UninitialisedField(self, 'InstrForAssgne', InstructionForAssignee1, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', RequestedModification11, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', RequestedModification11, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if value is not None else base_types.UninitialisedField(self, 'Undrlyg', UnderlyingTransaction8Choice, False)

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = base_types.UninitialisedField(self, 'Undrlyg', UnderlyingTransaction8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForAssgne', type=InstructionForAssignee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=RequestedModification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Undrlyg', type=UnderlyingTransaction8Choice, min=1, max=1, mutex_group=None, array=False),
	))