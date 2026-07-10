# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StaticDataRequestV02 import StaticDataRequestV02

class ADMI_009_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.009.001.02"
		_docname = "admi.009.001.02"

		__slots__ = ["_StatcDataReq"]
		@property
		def StatcDataReq(self):
			return self._StatcDataReq

		@StatcDataReq.setter
		def StatcDataReq(self, value):
			self._StatcDataReq = value if type(value) != base_types.auto else self.make_default("StatcDataReq")

		@StatcDataReq.deleter
		def StatcDataReq(self):
			del self._StatcDataReq
			self._StatcDataReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StatcDataReq', type=StaticDataRequestV02, min=1, max=1, mutex_group=None, array=False),
		))