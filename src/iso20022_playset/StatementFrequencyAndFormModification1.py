from . import base_types
from .StatementFrequencyAndForm1 import StatementFrequencyAndForm1
from .Modification1Code import Modification1Code

class StatementFrequencyAndFormModification1(base_types._BaseFieldType):

	__slots__ = ["_StmtFrqcyAndForm", "_ModCd"]
	@property
	def StmtFrqcyAndForm(self):
		return self._StmtFrqcyAndForm

	@StmtFrqcyAndForm.setter
	def StmtFrqcyAndForm(self, value):
		self._StmtFrqcyAndForm = value if type(value) != base_types.auto else self.make_default("StmtFrqcyAndForm")

	@StmtFrqcyAndForm.deleter
	def StmtFrqcyAndForm(self):
		del self._StmtFrqcyAndForm
		self._StmtFrqcyAndForm = None

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != base_types.auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtFrqcyAndForm', type=StatementFrequencyAndForm1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))

