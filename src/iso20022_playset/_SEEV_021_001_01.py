# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAMovementConfirmationV01 import AgentCAMovementConfirmationV01

class SEEV_021_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAMvmntConf"]
		@property
		def AgtCAMvmntConf(self):
			return self._AgtCAMvmntConf

		@AgtCAMvmntConf.setter
		def AgtCAMvmntConf(self, value):
			self._AgtCAMvmntConf = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntConf")

		@AgtCAMvmntConf.deleter
		def AgtCAMvmntConf(self):
			del self._AgtCAMvmntConf
			self._AgtCAMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntConf', type=AgentCAMovementConfirmationV01, min=1, max=1, mutex_group=None, array=False),
		))