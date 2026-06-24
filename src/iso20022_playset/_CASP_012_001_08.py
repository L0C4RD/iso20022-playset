# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIEventNotificationV08 import SaleToPOIEventNotificationV08

class CASP_012_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:casp.012.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SaleToPOIEvtNtfctn"]
		@property
		def SaleToPOIEvtNtfctn(self):
			return self._SaleToPOIEvtNtfctn

		@SaleToPOIEvtNtfctn.setter
		def SaleToPOIEvtNtfctn(self, value):
			self._SaleToPOIEvtNtfctn = value if type(value) != base_types.auto else self.make_default("SaleToPOIEvtNtfctn")

		@SaleToPOIEvtNtfctn.deleter
		def SaleToPOIEvtNtfctn(self):
			del self._SaleToPOIEvtNtfctn
			self._SaleToPOIEvtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIEvtNtfctn', type=SaleToPOIEventNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))