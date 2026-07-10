# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCADeactivationStatusAdviceV01 import AgentCADeactivationStatusAdviceV01

class SEEV_030_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.030.001.01"
		_docname = "seev.030.001.01"

		__slots__ = ["_AgtCADeactvtnStsAdvc"]
		@property
		def AgtCADeactvtnStsAdvc(self):
			return self._AgtCADeactvtnStsAdvc

		@AgtCADeactvtnStsAdvc.setter
		def AgtCADeactvtnStsAdvc(self, value):
			self._AgtCADeactvtnStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCADeactvtnStsAdvc")

		@AgtCADeactvtnStsAdvc.deleter
		def AgtCADeactvtnStsAdvc(self):
			del self._AgtCADeactvtnStsAdvc
			self._AgtCADeactvtnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnStsAdvc', type=AgentCADeactivationStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))