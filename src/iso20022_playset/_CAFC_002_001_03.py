# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FeeCollectionResponseV03 import FeeCollectionResponseV03

class CAFC_002_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:cafc.002.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

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
			base_types.FieldEntry(name='FeeColltnRspn', type=FeeCollectionResponseV03, min=1, max=1, mutex_group=None, array=False),
		))