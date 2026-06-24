# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountStatusAdviceV01 import SecuritiesAccountStatusAdviceV01

class REDA_020_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.020.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesAcctStsAdvc"]
		@property
		def SctiesAcctStsAdvc(self):
			return self._SctiesAcctStsAdvc

		@SctiesAcctStsAdvc.setter
		def SctiesAcctStsAdvc(self, value):
			self._SctiesAcctStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesAcctStsAdvc")

		@SctiesAcctStsAdvc.deleter
		def SctiesAcctStsAdvc(self):
			del self._SctiesAcctStsAdvc
			self._SctiesAcctStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctStsAdvc', type=SecuritiesAccountStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))