# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RedemptionOrderV04

class SETR_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.004.001.04"
		_docname = "setr.004.001.04"

		__slots__ = ["_RedOrdr"]
		@property
		def RedOrdr(self):
			return self._RedOrdr

		@RedOrdr.setter
		def RedOrdr(self, value):
			self._RedOrdr = value if value is not None else base_types.UninitialisedField(self, 'RedOrdr', RedemptionOrderV04, False)

		@RedOrdr.deleter
		def RedOrdr(self):
			del self._RedOrdr
			self._RedOrdr = base_types.UninitialisedField(self, 'RedOrdr', RedemptionOrderV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdr', type=RedemptionOrderV04, min=1, max=1, mutex_group=None, array=False),
		))