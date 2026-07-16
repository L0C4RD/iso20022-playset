# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SwitchOrderV05

class SETR_013_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.013.001.05"
		_docname = "setr.013.001.05"

		__slots__ = ["_SwtchOrdr"]
		@property
		def SwtchOrdr(self):
			return self._SwtchOrdr

		@SwtchOrdr.setter
		def SwtchOrdr(self, value):
			self._SwtchOrdr = value if value is not None else base_types.UninitialisedField(self, 'SwtchOrdr', SwitchOrderV05, False)

		@SwtchOrdr.deleter
		def SwtchOrdr(self):
			del self._SwtchOrdr
			self._SwtchOrdr = base_types.UninitialisedField(self, 'SwtchOrdr', SwitchOrderV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdr', type=SwitchOrderV05, min=1, max=1, mutex_group=None, array=False),
		))