# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GeneralBusinessInformationCriteriaDefinition1Choice
from . import QueryType2Code

class BusinessInformationQueryDefinition3(base_types._BaseFieldType):

	__slots__ = ["_GnlBizInfCrit", "_QryTp"]
	@property
	def GnlBizInfCrit(self):
		return self._GnlBizInfCrit

	@GnlBizInfCrit.setter
	def GnlBizInfCrit(self, value):
		self._GnlBizInfCrit = value if value is not None else base_types.UninitialisedField(self, 'GnlBizInfCrit', GeneralBusinessInformationCriteriaDefinition1Choice, False)

	@GnlBizInfCrit.deleter
	def GnlBizInfCrit(self):
		del self._GnlBizInfCrit
		self._GnlBizInfCrit = base_types.UninitialisedField(self, 'GnlBizInfCrit', GeneralBusinessInformationCriteriaDefinition1Choice, False)

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
		base_types.FieldEntry(name='GnlBizInfCrit', type=GeneralBusinessInformationCriteriaDefinition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
	))