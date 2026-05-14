# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAStandingInstructionStatusAdviceV01 import AgentCAStandingInstructionStatusAdviceV01

class SEEV_027_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAStgInstrStsAdvc"]
		@property
		def AgtCAStgInstrStsAdvc(self):
			return self._AgtCAStgInstrStsAdvc

		@AgtCAStgInstrStsAdvc.setter
		def AgtCAStgInstrStsAdvc(self, value):
			self._AgtCAStgInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAStgInstrStsAdvc")

		@AgtCAStgInstrStsAdvc.deleter
		def AgtCAStgInstrStsAdvc(self):
			del self._AgtCAStgInstrStsAdvc
			self._AgtCAStgInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrStsAdvc', type=AgentCAStandingInstructionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))