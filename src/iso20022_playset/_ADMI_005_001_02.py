# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportQueryRequestV02

class ADMI_005_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.005.001.02"
		_docname = "admi.005.001.02"

		__slots__ = ["_RptQryReq"]
		@property
		def RptQryReq(self):
			return self._RptQryReq

		@RptQryReq.setter
		def RptQryReq(self, value):
			self._RptQryReq = value if value is not None else base_types.UninitialisedField(self, 'RptQryReq', ReportQueryRequestV02, False)

		@RptQryReq.deleter
		def RptQryReq(self):
			del self._RptQryReq
			self._RptQryReq = base_types.UninitialisedField(self, 'RptQryReq', ReportQueryRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RptQryReq', type=ReportQueryRequestV02, min=1, max=1, mutex_group=None, array=False),
		))