# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NetPositionV04

class SECL_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.004.001.04"
		_docname = "secl.004.001.04"

		__slots__ = ["_NetPos"]
		@property
		def NetPos(self):
			return self._NetPos

		@NetPos.setter
		def NetPos(self, value):
			self._NetPos = value if value is not None else base_types.UninitialisedField(self, 'NetPos', NetPositionV04, False)

		@NetPos.deleter
		def NetPos(self):
			del self._NetPos
			self._NetPos = base_types.UninitialisedField(self, 'NetPos', NetPositionV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetPos', type=NetPositionV04, min=1, max=1, mutex_group=None, array=False),
		))