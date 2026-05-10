from . import base_types
import QueryType2Code
import CurrencyCriteriaDefinition1Choice

class CurrencyQueryDefinition3(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_CcyCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def CcyCrit(self):
		return self._CcyCrit

	@CcyCrit.setter
	def CcyCrit(self, value):
		self._CcyCrit = value if type(value) != auto else self.make_default("CcyCrit")

	@CcyCrit.deleter
	def CcyCrit(self):
		del self._CcyCrit
		self._CcyCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyCrit', type=CurrencyCriteriaDefinition1Choice, min=0, max=1, mutex_group=None, array=False),
	))

