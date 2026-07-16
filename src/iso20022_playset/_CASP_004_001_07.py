# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIReconciliationResponseV07

class CASP_004_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.004.001.07"
		_docname = "casp.004.001.07"

		__slots__ = ["_SaleToPOIRcncltnRspn"]
		@property
		def SaleToPOIRcncltnRspn(self):
			return self._SaleToPOIRcncltnRspn

		@SaleToPOIRcncltnRspn.setter
		def SaleToPOIRcncltnRspn(self, value):
			self._SaleToPOIRcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIRcncltnRspn', SaleToPOIReconciliationResponseV07, False)

		@SaleToPOIRcncltnRspn.deleter
		def SaleToPOIRcncltnRspn(self):
			del self._SaleToPOIRcncltnRspn
			self._SaleToPOIRcncltnRspn = base_types.UninitialisedField(self, 'SaleToPOIRcncltnRspn', SaleToPOIReconciliationResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRcncltnRspn', type=SaleToPOIReconciliationResponseV07, min=1, max=1, mutex_group=None, array=False),
		))