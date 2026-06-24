# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FIToFIPaymentReversalV13 import FIToFIPaymentReversalV13

class PACS_007_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:pacs.007.001.13",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FIToFIPmtRvsl"]
		@property
		def FIToFIPmtRvsl(self):
			return self._FIToFIPmtRvsl

		@FIToFIPmtRvsl.setter
		def FIToFIPmtRvsl(self, value):
			self._FIToFIPmtRvsl = value if type(value) != base_types.auto else self.make_default("FIToFIPmtRvsl")

		@FIToFIPmtRvsl.deleter
		def FIToFIPmtRvsl(self):
			del self._FIToFIPmtRvsl
			self._FIToFIPmtRvsl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtRvsl', type=FIToFIPaymentReversalV13, min=1, max=1, mutex_group=None, array=False),
		))