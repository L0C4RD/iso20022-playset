# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExtendOrPayRequestV01 import ExtendOrPayRequestV01

class TSRV_014_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.014.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_XtndOrPayReq"]
		@property
		def XtndOrPayReq(self):
			return self._XtndOrPayReq

		@XtndOrPayReq.setter
		def XtndOrPayReq(self, value):
			self._XtndOrPayReq = value if type(value) != base_types.auto else self.make_default("XtndOrPayReq")

		@XtndOrPayReq.deleter
		def XtndOrPayReq(self):
			del self._XtndOrPayReq
			self._XtndOrPayReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='XtndOrPayReq', type=ExtendOrPayRequestV01, min=1, max=1, mutex_group=None, array=False),
		))