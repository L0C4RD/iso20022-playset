# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAInformationStatusAdviceV01 import AgentCAInformationStatusAdviceV01

class SEEV_024_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAInfStsAdvc"]
		@property
		def AgtCAInfStsAdvc(self):
			return self._AgtCAInfStsAdvc

		@AgtCAInfStsAdvc.setter
		def AgtCAInfStsAdvc(self, value):
			self._AgtCAInfStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAInfStsAdvc")

		@AgtCAInfStsAdvc.deleter
		def AgtCAInfStsAdvc(self):
			del self._AgtCAInfStsAdvc
			self._AgtCAInfStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAInfStsAdvc', type=AgentCAInformationStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))