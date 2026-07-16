# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInConfirmationV03

class SECL_009_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.009.001.03"
		_docname = "secl.009.001.03"

		__slots__ = ["_BuyInConf"]
		@property
		def BuyInConf(self):
			return self._BuyInConf

		@BuyInConf.setter
		def BuyInConf(self, value):
			self._BuyInConf = value if value is not None else base_types.UninitialisedField(self, 'BuyInConf', BuyInConfirmationV03, False)

		@BuyInConf.deleter
		def BuyInConf(self):
			del self._BuyInConf
			self._BuyInConf = base_types.UninitialisedField(self, 'BuyInConf', BuyInConfirmationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInConf', type=BuyInConfirmationV03, min=1, max=1, mutex_group=None, array=False),
		))