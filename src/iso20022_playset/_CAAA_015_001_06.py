# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorRejectionV06 import AcceptorRejectionV06

class CAAA_015_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caaa.015.001.06",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AccptrRjctn"]
		@property
		def AccptrRjctn(self):
			return self._AccptrRjctn

		@AccptrRjctn.setter
		def AccptrRjctn(self, value):
			self._AccptrRjctn = value if type(value) != base_types.auto else self.make_default("AccptrRjctn")

		@AccptrRjctn.deleter
		def AccptrRjctn(self):
			del self._AccptrRjctn
			self._AccptrRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRjctn', type=AcceptorRejectionV06, min=1, max=1, mutex_group=None, array=False),
		))