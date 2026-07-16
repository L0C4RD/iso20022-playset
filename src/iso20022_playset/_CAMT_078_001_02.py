# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementQueryV02

class CAMT_078_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.078.001.02"
		_docname = "camt.078.001.02"

		__slots__ = ["_IntraBalMvmntQry"]
		@property
		def IntraBalMvmntQry(self):
			return self._IntraBalMvmntQry

		@IntraBalMvmntQry.setter
		def IntraBalMvmntQry(self, value):
			self._IntraBalMvmntQry = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntQry', IntraBalanceMovementQueryV02, False)

		@IntraBalMvmntQry.deleter
		def IntraBalMvmntQry(self):
			del self._IntraBalMvmntQry
			self._IntraBalMvmntQry = base_types.UninitialisedField(self, 'IntraBalMvmntQry', IntraBalanceMovementQueryV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntQry', type=IntraBalanceMovementQueryV02, min=1, max=1, mutex_group=None, array=False),
		))