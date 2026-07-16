# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDeviceReportV04

class CAAM_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.001.001.04"
		_docname = "caam.001.001.04"

		__slots__ = ["_ATMDvcRpt"]
		@property
		def ATMDvcRpt(self):
			return self._ATMDvcRpt

		@ATMDvcRpt.setter
		def ATMDvcRpt(self, value):
			self._ATMDvcRpt = value if value is not None else base_types.UninitialisedField(self, 'ATMDvcRpt', ATMDeviceReportV04, False)

		@ATMDvcRpt.deleter
		def ATMDvcRpt(self):
			del self._ATMDvcRpt
			self._ATMDvcRpt = base_types.UninitialisedField(self, 'ATMDvcRpt', ATMDeviceReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDvcRpt', type=ATMDeviceReportV04, min=1, max=1, mutex_group=None, array=False),
		))