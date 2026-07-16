# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RetrievalResponseV03

class CAIN_022_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.022.001.03"
		_docname = "cain.022.001.03"

		__slots__ = ["_RtrvlRspn"]
		@property
		def RtrvlRspn(self):
			return self._RtrvlRspn

		@RtrvlRspn.setter
		def RtrvlRspn(self, value):
			self._RtrvlRspn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlRspn', RetrievalResponseV03, False)

		@RtrvlRspn.deleter
		def RtrvlRspn(self):
			del self._RtrvlRspn
			self._RtrvlRspn = base_types.UninitialisedField(self, 'RtrvlRspn', RetrievalResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlRspn', type=RetrievalResponseV03, min=1, max=1, mutex_group=None, array=False),
		))