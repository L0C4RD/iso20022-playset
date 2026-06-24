# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionBulkOrderConfirmationV05 import RedemptionBulkOrderConfirmationV05

class SETR_003_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.003.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RedBlkOrdrConf"]
		@property
		def RedBlkOrdrConf(self):
			return self._RedBlkOrdrConf

		@RedBlkOrdrConf.setter
		def RedBlkOrdrConf(self, value):
			self._RedBlkOrdrConf = value if type(value) != base_types.auto else self.make_default("RedBlkOrdrConf")

		@RedBlkOrdrConf.deleter
		def RedBlkOrdrConf(self):
			del self._RedBlkOrdrConf
			self._RedBlkOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdrConf', type=RedemptionBulkOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))