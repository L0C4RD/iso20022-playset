# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionBulkOrderV05 import RedemptionBulkOrderV05

class SETR_001_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.001.001.05"
		_docname = "setr.001.001.05"

		__slots__ = ["_RedBlkOrdr"]
		@property
		def RedBlkOrdr(self):
			return self._RedBlkOrdr

		@RedBlkOrdr.setter
		def RedBlkOrdr(self, value):
			self._RedBlkOrdr = value if type(value) != base_types.auto else self.make_default("RedBlkOrdr")

		@RedBlkOrdr.deleter
		def RedBlkOrdr(self):
			del self._RedBlkOrdr
			self._RedBlkOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdr', type=RedemptionBulkOrderV05, min=1, max=1, mutex_group=None, array=False),
		))