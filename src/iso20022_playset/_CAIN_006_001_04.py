# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReversalResponseV04 import ReversalResponseV04

class CAIN_006_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RvslRspn"]
		@property
		def RvslRspn(self):
			return self._RvslRspn

		@RvslRspn.setter
		def RvslRspn(self, value):
			self._RvslRspn = value if type(value) != base_types.auto else self.make_default("RvslRspn")

		@RvslRspn.deleter
		def RvslRspn(self):
			del self._RvslRspn
			self._RvslRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslRspn', type=ReversalResponseV04, min=1, max=1, mutex_group=None, array=False),
		))