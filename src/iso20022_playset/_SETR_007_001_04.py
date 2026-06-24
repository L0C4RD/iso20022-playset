# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionBulkOrderV04 import SubscriptionBulkOrderV04

class SETR_007_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.007.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SbcptBlkOrdr"]
		@property
		def SbcptBlkOrdr(self):
			return self._SbcptBlkOrdr

		@SbcptBlkOrdr.setter
		def SbcptBlkOrdr(self, value):
			self._SbcptBlkOrdr = value if type(value) != base_types.auto else self.make_default("SbcptBlkOrdr")

		@SbcptBlkOrdr.deleter
		def SbcptBlkOrdr(self):
			del self._SbcptBlkOrdr
			self._SbcptBlkOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdr', type=SubscriptionBulkOrderV04, min=1, max=1, mutex_group=None, array=False),
		))