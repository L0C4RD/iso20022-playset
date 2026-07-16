# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionBulkOrderV05

class SETR_007_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.007.001.05"
		_docname = "setr.007.001.05"

		__slots__ = ["_SbcptBlkOrdr"]
		@property
		def SbcptBlkOrdr(self):
			return self._SbcptBlkOrdr

		@SbcptBlkOrdr.setter
		def SbcptBlkOrdr(self, value):
			self._SbcptBlkOrdr = value if value is not None else base_types.UninitialisedField(self, 'SbcptBlkOrdr', SubscriptionBulkOrderV05, False)

		@SbcptBlkOrdr.deleter
		def SbcptBlkOrdr(self):
			del self._SbcptBlkOrdr
			self._SbcptBlkOrdr = base_types.UninitialisedField(self, 'SbcptBlkOrdr', SubscriptionBulkOrderV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdr', type=SubscriptionBulkOrderV05, min=1, max=1, mutex_group=None, array=False),
		))