import base_types
import ProprietaryStatusAndReason7
import FailingStatus12Choice
import PendingStatus50Choice

class SettlementStatus22Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdg", "_Flng", "_Prtry"]
	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Flng(self):
		return self._Flng

	@Flng.setter
	def Flng(self, value):
		self._Flng = value if type(value) != auto else self.make_default("Flng")

	@Flng.deleter
	def Flng(self):
		del self._Flng
		self._Flng = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdg', type=PendingStatus50Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Flng', type=FailingStatus12Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
	))

