# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIAbortV08 import SaleToPOIAbortV08

class CASP_011_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:casp.011.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SaleToPOIAbrt"]
		@property
		def SaleToPOIAbrt(self):
			return self._SaleToPOIAbrt

		@SaleToPOIAbrt.setter
		def SaleToPOIAbrt(self, value):
			self._SaleToPOIAbrt = value if type(value) != base_types.auto else self.make_default("SaleToPOIAbrt")

		@SaleToPOIAbrt.deleter
		def SaleToPOIAbrt(self):
			del self._SaleToPOIAbrt
			self._SaleToPOIAbrt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAbrt', type=SaleToPOIAbortV08, min=1, max=1, mutex_group=None, array=False),
		))