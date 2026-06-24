# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CloseLinkCreationRequestV01 import CloseLinkCreationRequestV01

class REDA_027_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.027.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ClsLkCreReq"]
		@property
		def ClsLkCreReq(self):
			return self._ClsLkCreReq

		@ClsLkCreReq.setter
		def ClsLkCreReq(self, value):
			self._ClsLkCreReq = value if type(value) != base_types.auto else self.make_default("ClsLkCreReq")

		@ClsLkCreReq.deleter
		def ClsLkCreReq(self):
			del self._ClsLkCreReq
			self._ClsLkCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClsLkCreReq', type=CloseLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))