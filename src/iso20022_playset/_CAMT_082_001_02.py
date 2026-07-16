# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementCancellationQueryV02

class CAMT_082_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.082.001.02"
		_docname = "camt.082.001.02"

		__slots__ = ["_IntraBalMvmntCxlQry"]
		@property
		def IntraBalMvmntCxlQry(self):
			return self._IntraBalMvmntCxlQry

		@IntraBalMvmntCxlQry.setter
		def IntraBalMvmntCxlQry(self, value):
			self._IntraBalMvmntCxlQry = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntCxlQry', IntraBalanceMovementCancellationQueryV02, False)

		@IntraBalMvmntCxlQry.deleter
		def IntraBalMvmntCxlQry(self):
			del self._IntraBalMvmntCxlQry
			self._IntraBalMvmntCxlQry = base_types.UninitialisedField(self, 'IntraBalMvmntCxlQry', IntraBalanceMovementCancellationQueryV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlQry', type=IntraBalanceMovementCancellationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))