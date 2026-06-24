# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RoleAndBaselineRejectionNotificationV01 import RoleAndBaselineRejectionNotificationV01

class TSMT_052_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.052.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RoleAndBaselnRjctnNtfctn"]
		@property
		def RoleAndBaselnRjctnNtfctn(self):
			return self._RoleAndBaselnRjctnNtfctn

		@RoleAndBaselnRjctnNtfctn.setter
		def RoleAndBaselnRjctnNtfctn(self, value):
			self._RoleAndBaselnRjctnNtfctn = value if type(value) != base_types.auto else self.make_default("RoleAndBaselnRjctnNtfctn")

		@RoleAndBaselnRjctnNtfctn.deleter
		def RoleAndBaselnRjctnNtfctn(self):
			del self._RoleAndBaselnRjctnNtfctn
			self._RoleAndBaselnRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctnNtfctn', type=RoleAndBaselineRejectionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))