# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionOrderConfirmationV06

class SETR_006_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.006.001.06"
		_docname = "setr.006.001.06"

		__slots__ = ["_RedOrdrConf"]
		@property
		def RedOrdrConf(self):
			return self._RedOrdrConf

		@RedOrdrConf.setter
		def RedOrdrConf(self, value):
			self._RedOrdrConf = value if value is not None else base_types.UninitialisedField(self, 'RedOrdrConf', RedemptionOrderConfirmationV06, False)

		@RedOrdrConf.deleter
		def RedOrdrConf(self):
			del self._RedOrdrConf
			self._RedOrdrConf = base_types.UninitialisedField(self, 'RedOrdrConf', RedemptionOrderConfirmationV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConf', type=RedemptionOrderConfirmationV06, min=1, max=1, mutex_group=None, array=False),
		))