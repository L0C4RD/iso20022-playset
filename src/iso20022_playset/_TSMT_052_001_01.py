# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RoleAndBaselineRejectionNotificationV01

class TSMT_052_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.052.001.01"
		_docname = "tsmt.052.001.01"

		__slots__ = ["_RoleAndBaselnRjctnNtfctn"]
		@property
		def RoleAndBaselnRjctnNtfctn(self):
			return self._RoleAndBaselnRjctnNtfctn

		@RoleAndBaselnRjctnNtfctn.setter
		def RoleAndBaselnRjctnNtfctn(self, value):
			self._RoleAndBaselnRjctnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'RoleAndBaselnRjctnNtfctn', RoleAndBaselineRejectionNotificationV01, False)

		@RoleAndBaselnRjctnNtfctn.deleter
		def RoleAndBaselnRjctnNtfctn(self):
			del self._RoleAndBaselnRjctnNtfctn
			self._RoleAndBaselnRjctnNtfctn = base_types.UninitialisedField(self, 'RoleAndBaselnRjctnNtfctn', RoleAndBaselineRejectionNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctnNtfctn', type=RoleAndBaselineRejectionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))