# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIMessageRejectionV02

class CASP_013_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.013.001.02"
		_docname = "casp.013.001.02"

		__slots__ = ["_SaleToPOIMsgRjctn"]
		@property
		def SaleToPOIMsgRjctn(self):
			return self._SaleToPOIMsgRjctn

		@SaleToPOIMsgRjctn.setter
		def SaleToPOIMsgRjctn(self, value):
			self._SaleToPOIMsgRjctn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIMsgRjctn', SaleToPOIMessageRejectionV02, False)

		@SaleToPOIMsgRjctn.deleter
		def SaleToPOIMsgRjctn(self):
			del self._SaleToPOIMsgRjctn
			self._SaleToPOIMsgRjctn = base_types.UninitialisedField(self, 'SaleToPOIMsgRjctn', SaleToPOIMessageRejectionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgRjctn', type=SaleToPOIMessageRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))