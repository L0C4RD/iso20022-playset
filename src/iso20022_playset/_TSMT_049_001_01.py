# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RoleAndBaselineAcceptanceV01

class TSMT_049_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.049.001.01"
		_docname = "tsmt.049.001.01"

		__slots__ = ["_RoleAndBaselnAccptnc"]
		@property
		def RoleAndBaselnAccptnc(self):
			return self._RoleAndBaselnAccptnc

		@RoleAndBaselnAccptnc.setter
		def RoleAndBaselnAccptnc(self, value):
			self._RoleAndBaselnAccptnc = value if value is not None else base_types.UninitialisedField(self, 'RoleAndBaselnAccptnc', RoleAndBaselineAcceptanceV01, False)

		@RoleAndBaselnAccptnc.deleter
		def RoleAndBaselnAccptnc(self):
			del self._RoleAndBaselnAccptnc
			self._RoleAndBaselnAccptnc = base_types.UninitialisedField(self, 'RoleAndBaselnAccptnc', RoleAndBaselineAcceptanceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnAccptnc', type=RoleAndBaselineAcceptanceV01, min=1, max=1, mutex_group=None, array=False),
		))