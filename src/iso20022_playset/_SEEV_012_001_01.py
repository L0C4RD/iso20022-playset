# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAElectionAdviceV01 import AgentCAElectionAdviceV01

class SEEV_012_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.012.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AgtCAElctnAdvc"]
		@property
		def AgtCAElctnAdvc(self):
			return self._AgtCAElctnAdvc

		@AgtCAElctnAdvc.setter
		def AgtCAElctnAdvc(self, value):
			self._AgtCAElctnAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAElctnAdvc")

		@AgtCAElctnAdvc.deleter
		def AgtCAElctnAdvc(self):
			del self._AgtCAElctnAdvc
			self._AgtCAElctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAdvc', type=AgentCAElectionAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))