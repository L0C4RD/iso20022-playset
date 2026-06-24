# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionBulkOrderConfirmationV04 import SubscriptionBulkOrderConfirmationV04

class SETR_009_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.009.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SbcptBlkOrdrConf"]
		@property
		def SbcptBlkOrdrConf(self):
			return self._SbcptBlkOrdrConf

		@SbcptBlkOrdrConf.setter
		def SbcptBlkOrdrConf(self, value):
			self._SbcptBlkOrdrConf = value if type(value) != base_types.auto else self.make_default("SbcptBlkOrdrConf")

		@SbcptBlkOrdrConf.deleter
		def SbcptBlkOrdrConf(self):
			del self._SbcptBlkOrdrConf
			self._SbcptBlkOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConf', type=SubscriptionBulkOrderConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))