# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIEventNotificationV08

class CASP_012_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.012.001.08"
		_docname = "casp.012.001.08"

		__slots__ = ["_SaleToPOIEvtNtfctn"]
		@property
		def SaleToPOIEvtNtfctn(self):
			return self._SaleToPOIEvtNtfctn

		@SaleToPOIEvtNtfctn.setter
		def SaleToPOIEvtNtfctn(self, value):
			self._SaleToPOIEvtNtfctn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIEvtNtfctn', SaleToPOIEventNotificationV08, False)

		@SaleToPOIEvtNtfctn.deleter
		def SaleToPOIEvtNtfctn(self):
			del self._SaleToPOIEvtNtfctn
			self._SaleToPOIEvtNtfctn = base_types.UninitialisedField(self, 'SaleToPOIEvtNtfctn', SaleToPOIEventNotificationV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIEvtNtfctn', type=SaleToPOIEventNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))