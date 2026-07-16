# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReversalResponseV05

class CAIN_006_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.006.001.05"
		_docname = "cain.006.001.05"

		__slots__ = ["_RvslRspn"]
		@property
		def RvslRspn(self):
			return self._RvslRspn

		@RvslRspn.setter
		def RvslRspn(self, value):
			self._RvslRspn = value if value is not None else base_types.UninitialisedField(self, 'RvslRspn', ReversalResponseV05, False)

		@RvslRspn.deleter
		def RvslRspn(self):
			del self._RvslRspn
			self._RvslRspn = base_types.UninitialisedField(self, 'RvslRspn', ReversalResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslRspn', type=ReversalResponseV05, min=1, max=1, mutex_group=None, array=False),
		))