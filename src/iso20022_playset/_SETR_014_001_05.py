# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SwitchOrderCancellationRequestV05

class SETR_014_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.014.001.05"
		_docname = "setr.014.001.05"

		__slots__ = ["_SwtchOrdrCxlReq"]
		@property
		def SwtchOrdrCxlReq(self):
			return self._SwtchOrdrCxlReq

		@SwtchOrdrCxlReq.setter
		def SwtchOrdrCxlReq(self, value):
			self._SwtchOrdrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'SwtchOrdrCxlReq', SwitchOrderCancellationRequestV05, False)

		@SwtchOrdrCxlReq.deleter
		def SwtchOrdrCxlReq(self):
			del self._SwtchOrdrCxlReq
			self._SwtchOrdrCxlReq = base_types.UninitialisedField(self, 'SwtchOrdrCxlReq', SwitchOrderCancellationRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrCxlReq', type=SwitchOrderCancellationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))