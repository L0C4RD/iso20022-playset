# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UnableToApplyV10 import UnableToApplyV10

class CAMT_026_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.026.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_UblToApply"]
		@property
		def UblToApply(self):
			return self._UblToApply

		@UblToApply.setter
		def UblToApply(self, value):
			self._UblToApply = value if type(value) != base_types.auto else self.make_default("UblToApply")

		@UblToApply.deleter
		def UblToApply(self):
			del self._UblToApply
			self._UblToApply = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UblToApply', type=UnableToApplyV10, min=1, max=1, mutex_group=None, array=False),
		))