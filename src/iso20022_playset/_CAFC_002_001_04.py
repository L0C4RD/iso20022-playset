# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FeeCollectionResponseV04 import FeeCollectionResponseV04

class CAFC_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafc.002.001.04"
		_docname = "cafc.002.001.04"

		__slots__ = ["_FeeColltnRspn"]
		@property
		def FeeColltnRspn(self):
			return self._FeeColltnRspn

		@FeeColltnRspn.setter
		def FeeColltnRspn(self, value):
			self._FeeColltnRspn = value if type(value) != base_types.auto else self.make_default("FeeColltnRspn")

		@FeeColltnRspn.deleter
		def FeeColltnRspn(self):
			del self._FeeColltnRspn
			self._FeeColltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FeeColltnRspn', type=FeeCollectionResponseV04, min=1, max=1, mutex_group=None, array=False),
		))