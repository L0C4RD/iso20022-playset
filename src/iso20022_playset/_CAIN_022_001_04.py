# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RetrievalResponseV04 import RetrievalResponseV04

class CAIN_022_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrvlRspn"]
		@property
		def RtrvlRspn(self):
			return self._RtrvlRspn

		@RtrvlRspn.setter
		def RtrvlRspn(self, value):
			self._RtrvlRspn = value if type(value) != base_types.auto else self.make_default("RtrvlRspn")

		@RtrvlRspn.deleter
		def RtrvlRspn(self):
			del self._RtrvlRspn
			self._RtrvlRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlRspn', type=RetrievalResponseV04, min=1, max=1, mutex_group=None, array=False),
		))