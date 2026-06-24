# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesAccountAuditTrailQueryV01 import SecuritiesAccountAuditTrailQueryV01

class REDA_036_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesAcctAudtTrlQry"]
		@property
		def SctiesAcctAudtTrlQry(self):
			return self._SctiesAcctAudtTrlQry

		@SctiesAcctAudtTrlQry.setter
		def SctiesAcctAudtTrlQry(self, value):
			self._SctiesAcctAudtTrlQry = value if type(value) != base_types.auto else self.make_default("SctiesAcctAudtTrlQry")

		@SctiesAcctAudtTrlQry.deleter
		def SctiesAcctAudtTrlQry(self):
			del self._SctiesAcctAudtTrlQry
			self._SctiesAcctAudtTrlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctAudtTrlQry', type=SecuritiesAccountAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))