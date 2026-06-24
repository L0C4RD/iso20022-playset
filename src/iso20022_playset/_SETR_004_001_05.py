# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionOrderV05 import RedemptionOrderV05

class SETR_004_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.004.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RedOrdr"]
		@property
		def RedOrdr(self):
			return self._RedOrdr

		@RedOrdr.setter
		def RedOrdr(self, value):
			self._RedOrdr = value if type(value) != base_types.auto else self.make_default("RedOrdr")

		@RedOrdr.deleter
		def RedOrdr(self):
			del self._RedOrdr
			self._RedOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdr', type=RedemptionOrderV05, min=1, max=1, mutex_group=None, array=False),
		))