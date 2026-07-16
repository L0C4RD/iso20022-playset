# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RoleAndBaselineRejectionV01

class TSMT_050_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01"
		_docname = "tsmt.050.001.01"

		__slots__ = ["_RoleAndBaselnRjctn"]
		@property
		def RoleAndBaselnRjctn(self):
			return self._RoleAndBaselnRjctn

		@RoleAndBaselnRjctn.setter
		def RoleAndBaselnRjctn(self, value):
			self._RoleAndBaselnRjctn = value if value is not None else base_types.UninitialisedField(self, 'RoleAndBaselnRjctn', RoleAndBaselineRejectionV01, False)

		@RoleAndBaselnRjctn.deleter
		def RoleAndBaselnRjctn(self):
			del self._RoleAndBaselnRjctn
			self._RoleAndBaselnRjctn = base_types.UninitialisedField(self, 'RoleAndBaselnRjctn', RoleAndBaselineRejectionV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctn', type=RoleAndBaselineRejectionV01, min=1, max=1, mutex_group=None, array=False),
		))