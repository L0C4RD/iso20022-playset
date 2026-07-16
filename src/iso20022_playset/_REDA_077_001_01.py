# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CloseLinkDeletionRequestV01

class REDA_077_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.077.001.01"
		_docname = "reda.077.001.01"

		__slots__ = ["_ClsLkDeltnReq"]
		@property
		def ClsLkDeltnReq(self):
			return self._ClsLkDeltnReq

		@ClsLkDeltnReq.setter
		def ClsLkDeltnReq(self, value):
			self._ClsLkDeltnReq = value if value is not None else base_types.UninitialisedField(self, 'ClsLkDeltnReq', CloseLinkDeletionRequestV01, False)

		@ClsLkDeltnReq.deleter
		def ClsLkDeltnReq(self):
			del self._ClsLkDeltnReq
			self._ClsLkDeltnReq = base_types.UninitialisedField(self, 'ClsLkDeltnReq', CloseLinkDeletionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClsLkDeltnReq', type=CloseLinkDeletionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))