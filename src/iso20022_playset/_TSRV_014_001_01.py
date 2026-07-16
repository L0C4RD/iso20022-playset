# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExtendOrPayRequestV01

class TSRV_014_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.014.001.01"
		_docname = "tsrv.014.001.01"

		__slots__ = ["_XtndOrPayReq"]
		@property
		def XtndOrPayReq(self):
			return self._XtndOrPayReq

		@XtndOrPayReq.setter
		def XtndOrPayReq(self, value):
			self._XtndOrPayReq = value if value is not None else base_types.UninitialisedField(self, 'XtndOrPayReq', ExtendOrPayRequestV01, False)

		@XtndOrPayReq.deleter
		def XtndOrPayReq(self):
			del self._XtndOrPayReq
			self._XtndOrPayReq = base_types.UninitialisedField(self, 'XtndOrPayReq', ExtendOrPayRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='XtndOrPayReq', type=ExtendOrPayRequestV01, min=1, max=1, mutex_group=None, array=False),
		))