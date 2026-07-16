# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import Max35Text

class ProprietaryAgent5(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_Tp"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if value is not None else base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))