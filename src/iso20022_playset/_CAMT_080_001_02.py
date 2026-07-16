# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementModificationQueryV02

class CAMT_080_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.080.001.02"
		_docname = "camt.080.001.02"

		__slots__ = ["_IntraBalMvmntModQry"]
		@property
		def IntraBalMvmntModQry(self):
			return self._IntraBalMvmntModQry

		@IntraBalMvmntModQry.setter
		def IntraBalMvmntModQry(self, value):
			self._IntraBalMvmntModQry = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntModQry', IntraBalanceMovementModificationQueryV02, False)

		@IntraBalMvmntModQry.deleter
		def IntraBalMvmntModQry(self):
			del self._IntraBalMvmntModQry
			self._IntraBalMvmntModQry = base_types.UninitialisedField(self, 'IntraBalMvmntModQry', IntraBalanceMovementModificationQueryV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModQry', type=IntraBalanceMovementModificationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))