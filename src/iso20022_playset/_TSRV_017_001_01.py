# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DemandWithdrawalNotificationV01 import DemandWithdrawalNotificationV01

class TSRV_017_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsrv.017.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_DmndWdrwlNtfctn"]
		@property
		def DmndWdrwlNtfctn(self):
			return self._DmndWdrwlNtfctn

		@DmndWdrwlNtfctn.setter
		def DmndWdrwlNtfctn(self, value):
			self._DmndWdrwlNtfctn = value if type(value) != base_types.auto else self.make_default("DmndWdrwlNtfctn")

		@DmndWdrwlNtfctn.deleter
		def DmndWdrwlNtfctn(self):
			del self._DmndWdrwlNtfctn
			self._DmndWdrwlNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DmndWdrwlNtfctn', type=DemandWithdrawalNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))