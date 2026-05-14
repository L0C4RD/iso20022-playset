# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyCriteriaDefinition1Choice import CurrencyCriteriaDefinition1Choice
from ._QueryType2Code import QueryType2Code

class CurrencyQueryDefinition3(base_types._BaseFieldType):

	__slots__ = ["_CcyCrit", "_QryTp"]
	@property
	def CcyCrit(self):
		return self._CcyCrit

	@CcyCrit.setter
	def CcyCrit(self, value):
		self._CcyCrit = value if type(value) != base_types.auto else self.make_default("CcyCrit")

	@CcyCrit.deleter
	def CcyCrit(self):
		del self._CcyCrit
		self._CcyCrit = None

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != base_types.auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyCrit', type=CurrencyCriteriaDefinition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))