# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionBulkOrderConfirmationV04

class SETR_003_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.003.001.04"
		_docname = "setr.003.001.04"

		__slots__ = ["_RedBlkOrdrConf"]
		@property
		def RedBlkOrdrConf(self):
			return self._RedBlkOrdrConf

		@RedBlkOrdrConf.setter
		def RedBlkOrdrConf(self, value):
			self._RedBlkOrdrConf = value if value is not None else base_types.UninitialisedField(self, 'RedBlkOrdrConf', RedemptionBulkOrderConfirmationV04, False)

		@RedBlkOrdrConf.deleter
		def RedBlkOrdrConf(self):
			del self._RedBlkOrdrConf
			self._RedBlkOrdrConf = base_types.UninitialisedField(self, 'RedBlkOrdrConf', RedemptionBulkOrderConfirmationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrConf', type=RedemptionBulkOrderConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))