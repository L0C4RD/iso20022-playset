# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExtendOrPayResponseV01

class TSRV_015_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.015.001.01"
		_docname = "tsrv.015.001.01"

		__slots__ = ["_XtndOrPayRspn"]
		@property
		def XtndOrPayRspn(self):
			return self._XtndOrPayRspn

		@XtndOrPayRspn.setter
		def XtndOrPayRspn(self, value):
			self._XtndOrPayRspn = value if value is not None else base_types.UninitialisedField(self, 'XtndOrPayRspn', ExtendOrPayResponseV01, False)

		@XtndOrPayRspn.deleter
		def XtndOrPayRspn(self):
			del self._XtndOrPayRspn
			self._XtndOrPayRspn = base_types.UninitialisedField(self, 'XtndOrPayRspn', ExtendOrPayResponseV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='XtndOrPayRspn', type=ExtendOrPayResponseV01, min=1, max=1, mutex_group=None, array=False),
		))