from . import base_types
from .QueryType2Code import QueryType2Code
from .GeneralBusinessInformationCriteriaDefinition1Choice import GeneralBusinessInformationCriteriaDefinition1Choice

class BusinessInformationQueryDefinition3(base_types._BaseFieldType):

	__slots__ = ["_GnlBizInfCrit", "_QryTp"]
	@property
	def GnlBizInfCrit(self):
		return self._GnlBizInfCrit

	@GnlBizInfCrit.setter
	def GnlBizInfCrit(self, value):
		self._GnlBizInfCrit = value if type(value) != auto else self.make_default("GnlBizInfCrit")

	@GnlBizInfCrit.deleter
	def GnlBizInfCrit(self):
		del self._GnlBizInfCrit
		self._GnlBizInfCrit = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GnlBizInfCrit', type=GeneralBusinessInformationCriteriaDefinition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))

