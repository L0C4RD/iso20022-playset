# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAElectionStatusAdviceV01 import AgentCAElectionStatusAdviceV01

class SEEV_015_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAElctnStsAdvc"]
		@property
		def AgtCAElctnStsAdvc(self):
			return self._AgtCAElctnStsAdvc

		@AgtCAElctnStsAdvc.setter
		def AgtCAElctnStsAdvc(self, value):
			self._AgtCAElctnStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAElctnStsAdvc")

		@AgtCAElctnStsAdvc.deleter
		def AgtCAElctnStsAdvc(self):
			del self._AgtCAElctnStsAdvc
			self._AgtCAElctnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnStsAdvc', type=AgentCAElectionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))