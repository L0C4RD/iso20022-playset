# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardManagementInitiationV03

class CAIN_023_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.023.001.03"
		_docname = "cain.023.001.03"

		__slots__ = ["_CardMgmtInitn"]
		@property
		def CardMgmtInitn(self):
			return self._CardMgmtInitn

		@CardMgmtInitn.setter
		def CardMgmtInitn(self, value):
			self._CardMgmtInitn = value if value is not None else base_types.UninitialisedField(self, 'CardMgmtInitn', CardManagementInitiationV03, False)

		@CardMgmtInitn.deleter
		def CardMgmtInitn(self):
			del self._CardMgmtInitn
			self._CardMgmtInitn = base_types.UninitialisedField(self, 'CardMgmtInitn', CardManagementInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CardMgmtInitn', type=CardManagementInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))