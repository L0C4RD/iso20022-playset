# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyInConfirmationV03 import BuyInConfirmationV03

class SECL_009_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:secl.009.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BuyInConf"]
		@property
		def BuyInConf(self):
			return self._BuyInConf

		@BuyInConf.setter
		def BuyInConf(self, value):
			self._BuyInConf = value if type(value) != base_types.auto else self.make_default("BuyInConf")

		@BuyInConf.deleter
		def BuyInConf(self):
			del self._BuyInConf
			self._BuyInConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInConf', type=BuyInConfirmationV03, min=1, max=1, mutex_group=None, array=False),
		))