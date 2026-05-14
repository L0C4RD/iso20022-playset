# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RetrievalFulfilmentResponseV04 import RetrievalFulfilmentResponseV04

class CAIN_015_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrvlFlfmtRspn"]
		@property
		def RtrvlFlfmtRspn(self):
			return self._RtrvlFlfmtRspn

		@RtrvlFlfmtRspn.setter
		def RtrvlFlfmtRspn(self, value):
			self._RtrvlFlfmtRspn = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtRspn")

		@RtrvlFlfmtRspn.deleter
		def RtrvlFlfmtRspn(self):
			del self._RtrvlFlfmtRspn
			self._RtrvlFlfmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlFlfmtRspn', type=RetrievalFulfilmentResponseV04, min=1, max=1, mutex_group=None, array=False),
		))