# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingStatusAdvice002V09 import SecuritiesFinancingStatusAdvice002V09

class SESE_034_002_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:sese.034.002.09",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesFincgStsAdvc"]
		@property
		def SctiesFincgStsAdvc(self):
			return self._SctiesFincgStsAdvc

		@SctiesFincgStsAdvc.setter
		def SctiesFincgStsAdvc(self, value):
			self._SctiesFincgStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesFincgStsAdvc")

		@SctiesFincgStsAdvc.deleter
		def SctiesFincgStsAdvc(self):
			del self._SctiesFincgStsAdvc
			self._SctiesFincgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgStsAdvc', type=SecuritiesFinancingStatusAdvice002V09, min=1, max=1, mutex_group=None, array=False),
		))