# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInformation1 import CorporateActionInformation1
from ._DocumentIdentification8 import DocumentIdentification8
from ._GlobalDistributionRequest1 import GlobalDistributionRequest1

class AgentCAGlobalDistributionAuthorisationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_GblDstrbtnDtls", "_Id"]
	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def GblDstrbtnDtls(self):
		return self._GblDstrbtnDtls

	@GblDstrbtnDtls.setter
	def GblDstrbtnDtls(self, value):
		self._GblDstrbtnDtls = value if type(value) != base_types.auto else self.make_default("GblDstrbtnDtls")

	@GblDstrbtnDtls.deleter
	def GblDstrbtnDtls(self):
		del self._GblDstrbtnDtls
		self._GblDstrbtnDtls = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblDstrbtnDtls', type=GlobalDistributionRequest1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))