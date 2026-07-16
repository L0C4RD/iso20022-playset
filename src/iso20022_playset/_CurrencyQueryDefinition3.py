# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyCriteriaDefinition1Choice
from . import QueryType2Code

class CurrencyQueryDefinition3(base_types._BaseFieldType):

	__slots__ = ["_CcyCrit", "_QryTp"]
	@property
	def CcyCrit(self):
		return self._CcyCrit

	@CcyCrit.setter
	def CcyCrit(self, value):
		self._CcyCrit = value if value is not None else base_types.UninitialisedField(self, 'CcyCrit', CurrencyCriteriaDefinition1Choice, False)

	@CcyCrit.deleter
	def CcyCrit(self):
		del self._CcyCrit
		self._CcyCrit = base_types.UninitialisedField(self, 'CcyCrit', CurrencyCriteriaDefinition1Choice, False)

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyCrit', type=CurrencyCriteriaDefinition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))