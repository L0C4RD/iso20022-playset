# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReversalOfTransferOutConfirmationV09

class SESE_004_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.004.001.09"
		_docname = "sese.004.001.09"

		__slots__ = ["_RvslOfTrfOutConf"]
		@property
		def RvslOfTrfOutConf(self):
			return self._RvslOfTrfOutConf

		@RvslOfTrfOutConf.setter
		def RvslOfTrfOutConf(self, value):
			self._RvslOfTrfOutConf = value if value is not None else base_types.UninitialisedField(self, 'RvslOfTrfOutConf', ReversalOfTransferOutConfirmationV09, False)

		@RvslOfTrfOutConf.deleter
		def RvslOfTrfOutConf(self):
			del self._RvslOfTrfOutConf
			self._RvslOfTrfOutConf = base_types.UninitialisedField(self, 'RvslOfTrfOutConf', ReversalOfTransferOutConfirmationV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslOfTrfOutConf', type=ReversalOfTransferOutConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))