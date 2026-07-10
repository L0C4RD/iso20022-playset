# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferInConfirmationV09 import TransferInConfirmationV09

class SESE_007_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.007.001.09"
		_docname = "sese.007.001.09"

		__slots__ = ["_TrfInConf"]
		@property
		def TrfInConf(self):
			return self._TrfInConf

		@TrfInConf.setter
		def TrfInConf(self, value):
			self._TrfInConf = value if type(value) != base_types.auto else self.make_default("TrfInConf")

		@TrfInConf.deleter
		def TrfInConf(self):
			del self._TrfInConf
			self._TrfInConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInConf', type=TransferInConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))