# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchManagementInitiationV03

class CAAD_001_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.001.001.03"
		_docname = "caad.001.001.03"

		__slots__ = ["_BtchMgmtInitn"]
		@property
		def BtchMgmtInitn(self):
			return self._BtchMgmtInitn

		@BtchMgmtInitn.setter
		def BtchMgmtInitn(self, value):
			self._BtchMgmtInitn = value if value is not None else base_types.UninitialisedField(self, 'BtchMgmtInitn', BatchManagementInitiationV03, False)

		@BtchMgmtInitn.deleter
		def BtchMgmtInitn(self):
			del self._BtchMgmtInitn
			self._BtchMgmtInitn = base_types.UninitialisedField(self, 'BtchMgmtInitn', BatchManagementInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtInitn', type=BatchManagementInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))