# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementQueryResponseV02

class CAMT_079_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.079.001.02"
		_docname = "camt.079.001.02"

		__slots__ = ["_IntraBalMvmntQryRspn"]
		@property
		def IntraBalMvmntQryRspn(self):
			return self._IntraBalMvmntQryRspn

		@IntraBalMvmntQryRspn.setter
		def IntraBalMvmntQryRspn(self, value):
			self._IntraBalMvmntQryRspn = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntQryRspn', IntraBalanceMovementQueryResponseV02, False)

		@IntraBalMvmntQryRspn.deleter
		def IntraBalMvmntQryRspn(self):
			del self._IntraBalMvmntQryRspn
			self._IntraBalMvmntQryRspn = base_types.UninitialisedField(self, 'IntraBalMvmntQryRspn', IntraBalanceMovementQueryResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntQryRspn', type=IntraBalanceMovementQueryResponseV02, min=1, max=1, mutex_group=None, array=False),
		))