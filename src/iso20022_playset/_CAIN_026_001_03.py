# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AddendumResponseV03 import AddendumResponseV03

class CAIN_026_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:cain.026.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AdddmRspn"]
		@property
		def AdddmRspn(self):
			return self._AdddmRspn

		@AdddmRspn.setter
		def AdddmRspn(self, value):
			self._AdddmRspn = value if type(value) != base_types.auto else self.make_default("AdddmRspn")

		@AdddmRspn.deleter
		def AdddmRspn(self):
			del self._AdddmRspn
			self._AdddmRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmRspn', type=AddendumResponseV03, min=1, max=1, mutex_group=None, array=False),
		))