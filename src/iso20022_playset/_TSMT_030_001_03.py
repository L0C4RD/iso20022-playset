# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusChangeRequestRejectionNotificationV03

class TSMT_030_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.030.001.03"
		_docname = "tsmt.030.001.03"

		__slots__ = ["_StsChngReqRjctnNtfctn"]
		@property
		def StsChngReqRjctnNtfctn(self):
			return self._StsChngReqRjctnNtfctn

		@StsChngReqRjctnNtfctn.setter
		def StsChngReqRjctnNtfctn(self, value):
			self._StsChngReqRjctnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'StsChngReqRjctnNtfctn', StatusChangeRequestRejectionNotificationV03, False)

		@StsChngReqRjctnNtfctn.deleter
		def StsChngReqRjctnNtfctn(self):
			del self._StsChngReqRjctnNtfctn
			self._StsChngReqRjctnNtfctn = base_types.UninitialisedField(self, 'StsChngReqRjctnNtfctn', StatusChangeRequestRejectionNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqRjctnNtfctn', type=StatusChangeRequestRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))