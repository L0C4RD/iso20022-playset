# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RedemptionOrderConfirmationV06 import RedemptionOrderConfirmationV06

class SETR_006_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.006.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RedOrdrConf"]
		@property
		def RedOrdrConf(self):
			return self._RedOrdrConf

		@RedOrdrConf.setter
		def RedOrdrConf(self, value):
			self._RedOrdrConf = value if type(value) != base_types.auto else self.make_default("RedOrdrConf")

		@RedOrdrConf.deleter
		def RedOrdrConf(self):
			del self._RedOrdrConf
			self._RedOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConf', type=RedemptionOrderConfirmationV06, min=1, max=1, mutex_group=None, array=False),
		))