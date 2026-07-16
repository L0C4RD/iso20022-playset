# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import YesNoIndicator

class DeMinimusApplicable1(base_types._BaseFieldType):

	__slots__ = ["_NewIssePrmssn", "_Pctg"]
	@property
	def NewIssePrmssn(self):
		return self._NewIssePrmssn

	@NewIssePrmssn.setter
	def NewIssePrmssn(self, value):
		self._NewIssePrmssn = value if value is not None else base_types.UninitialisedField(self, 'NewIssePrmssn', YesNoIndicator, False)

	@NewIssePrmssn.deleter
	def NewIssePrmssn(self):
		del self._NewIssePrmssn
		self._NewIssePrmssn = base_types.UninitialisedField(self, 'NewIssePrmssn', YesNoIndicator, False)

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if value is not None else base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewIssePrmssn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))