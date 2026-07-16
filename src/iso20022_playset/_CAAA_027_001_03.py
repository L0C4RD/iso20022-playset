# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcquirerToAcceptorBatchFileExchangeV03

class CAAA_027_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.027.001.03"
		_docname = "caaa.027.001.03"

		__slots__ = ["_AcqrrToAccptrBtchFileXchg"]
		@property
		def AcqrrToAccptrBtchFileXchg(self):
			return self._AcqrrToAccptrBtchFileXchg

		@AcqrrToAccptrBtchFileXchg.setter
		def AcqrrToAccptrBtchFileXchg(self, value):
			self._AcqrrToAccptrBtchFileXchg = value if value is not None else base_types.UninitialisedField(self, 'AcqrrToAccptrBtchFileXchg', AcquirerToAcceptorBatchFileExchangeV03, False)

		@AcqrrToAccptrBtchFileXchg.deleter
		def AcqrrToAccptrBtchFileXchg(self):
			del self._AcqrrToAccptrBtchFileXchg
			self._AcqrrToAccptrBtchFileXchg = base_types.UninitialisedField(self, 'AcqrrToAccptrBtchFileXchg', AcquirerToAcceptorBatchFileExchangeV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcqrrToAccptrBtchFileXchg', type=AcquirerToAcceptorBatchFileExchangeV03, min=1, max=1, mutex_group=None, array=False),
		))