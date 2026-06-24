# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionBulkOrderConfirmationV05 import SubscriptionBulkOrderConfirmationV05

class SETR_009_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.009.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
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
			base_types.FieldEntry(name='SbcptBlkOrdrConf', type=SubscriptionBulkOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))