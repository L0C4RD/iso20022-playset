# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMReconciliationAdviceV03 import ATMReconciliationAdviceV03

class CAAM_009_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caam.009.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ATMRcncltnAdvc"]
		@property
		def ATMRcncltnAdvc(self):
			return self._ATMRcncltnAdvc

		@ATMRcncltnAdvc.setter
		def ATMRcncltnAdvc(self, value):
			self._ATMRcncltnAdvc = value if type(value) != base_types.auto else self.make_default("ATMRcncltnAdvc")

		@ATMRcncltnAdvc.deleter
		def ATMRcncltnAdvc(self):
			del self._ATMRcncltnAdvc
			self._ATMRcncltnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnAdvc', type=ATMReconciliationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))