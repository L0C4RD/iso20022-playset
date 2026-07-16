# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubscriptionBulkOrderConfirmationV05

class SETR_009_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.009.001.05"
		_docname = "setr.009.001.05"

		__slots__ = ["_SbcptBlkOrdrConf"]
		@property
		def SbcptBlkOrdrConf(self):
			return self._SbcptBlkOrdrConf

		@SbcptBlkOrdrConf.setter
		def SbcptBlkOrdrConf(self, value):
			self._SbcptBlkOrdrConf = value if value is not None else base_types.UninitialisedField(self, 'SbcptBlkOrdrConf', SubscriptionBulkOrderConfirmationV05, False)

		@SbcptBlkOrdrConf.deleter
		def SbcptBlkOrdrConf(self):
			del self._SbcptBlkOrdrConf
			self._SbcptBlkOrdrConf = base_types.UninitialisedField(self, 'SbcptBlkOrdrConf', SubscriptionBulkOrderConfirmationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConf', type=SubscriptionBulkOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))