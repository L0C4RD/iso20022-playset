# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DeleteStandingOrderV05 import DeleteStandingOrderV05

class CAMT_071_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.071.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_DelStgOrdr"]
		@property
		def DelStgOrdr(self):
			return self._DelStgOrdr

		@DelStgOrdr.setter
		def DelStgOrdr(self, value):
			self._DelStgOrdr = value if type(value) != base_types.auto else self.make_default("DelStgOrdr")

		@DelStgOrdr.deleter
		def DelStgOrdr(self):
			del self._DelStgOrdr
			self._DelStgOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DelStgOrdr', type=DeleteStandingOrderV05, min=1, max=1, mutex_group=None, array=False),
		))