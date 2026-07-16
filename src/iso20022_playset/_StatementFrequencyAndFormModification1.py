# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Modification1Code
from . import StatementFrequencyAndForm1

class StatementFrequencyAndFormModification1(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_StmtFrqcyAndForm"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@property
	def StmtFrqcyAndForm(self):
		return self._StmtFrqcyAndForm

	@StmtFrqcyAndForm.setter
	def StmtFrqcyAndForm(self, value):
		self._StmtFrqcyAndForm = value if value is not None else base_types.UninitialisedField(self, 'StmtFrqcyAndForm', StatementFrequencyAndForm1, False)

	@StmtFrqcyAndForm.deleter
	def StmtFrqcyAndForm(self):
		del self._StmtFrqcyAndForm
		self._StmtFrqcyAndForm = base_types.UninitialisedField(self, 'StmtFrqcyAndForm', StatementFrequencyAndForm1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtFrqcyAndForm', type=StatementFrequencyAndForm1, min=1, max=1, mutex_group=None, array=False),
	))