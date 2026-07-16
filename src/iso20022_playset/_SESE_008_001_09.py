# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReversalOfTransferInConfirmationV09

class SESE_008_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.008.001.09"
		_docname = "sese.008.001.09"

		__slots__ = ["_RvslOfTrfInConf"]
		@property
		def RvslOfTrfInConf(self):
			return self._RvslOfTrfInConf

		@RvslOfTrfInConf.setter
		def RvslOfTrfInConf(self, value):
			self._RvslOfTrfInConf = value if value is not None else base_types.UninitialisedField(self, 'RvslOfTrfInConf', ReversalOfTransferInConfirmationV09, False)

		@RvslOfTrfInConf.deleter
		def RvslOfTrfInConf(self):
			del self._RvslOfTrfInConf
			self._RvslOfTrfInConf = base_types.UninitialisedField(self, 'RvslOfTrfInConf', ReversalOfTransferInConfirmationV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslOfTrfInConf', type=ReversalOfTransferInConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))