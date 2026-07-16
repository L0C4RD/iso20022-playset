# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIAbortV07

class CASP_011_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.011.001.07"
		_docname = "casp.011.001.07"

		__slots__ = ["_SaleToPOIAbrt"]
		@property
		def SaleToPOIAbrt(self):
			return self._SaleToPOIAbrt

		@SaleToPOIAbrt.setter
		def SaleToPOIAbrt(self, value):
			self._SaleToPOIAbrt = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIAbrt', SaleToPOIAbortV07, False)

		@SaleToPOIAbrt.deleter
		def SaleToPOIAbrt(self):
			del self._SaleToPOIAbrt
			self._SaleToPOIAbrt = base_types.UninitialisedField(self, 'SaleToPOIAbrt', SaleToPOIAbortV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAbrt', type=SaleToPOIAbortV07, min=1, max=1, mutex_group=None, array=False),
		))