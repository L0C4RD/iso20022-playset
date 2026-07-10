# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingConfirmation002V11 import SecuritiesFinancingConfirmation002V11

class SESE_035_002_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.035.002.11"
		_docname = "sese.035.002.11"

		__slots__ = ["_SctiesFincgConf"]
		@property
		def SctiesFincgConf(self):
			return self._SctiesFincgConf

		@SctiesFincgConf.setter
		def SctiesFincgConf(self, value):
			self._SctiesFincgConf = value if type(value) != base_types.auto else self.make_default("SctiesFincgConf")

		@SctiesFincgConf.deleter
		def SctiesFincgConf(self):
			del self._SctiesFincgConf
			self._SctiesFincgConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgConf', type=SecuritiesFinancingConfirmation002V11, min=1, max=1, mutex_group=None, array=False),
		))