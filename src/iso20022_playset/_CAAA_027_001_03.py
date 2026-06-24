# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcquirerToAcceptorBatchFileExchangeV03 import AcquirerToAcceptorBatchFileExchangeV03

class CAAA_027_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.027.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcqrrToAccptrBtchFileXchg"]
		@property
		def AcqrrToAccptrBtchFileXchg(self):
			return self._AcqrrToAccptrBtchFileXchg

		@AcqrrToAccptrBtchFileXchg.setter
		def AcqrrToAccptrBtchFileXchg(self, value):
			self._AcqrrToAccptrBtchFileXchg = value if type(value) != base_types.auto else self.make_default("AcqrrToAccptrBtchFileXchg")

		@AcqrrToAccptrBtchFileXchg.deleter
		def AcqrrToAccptrBtchFileXchg(self):
			del self._AcqrrToAccptrBtchFileXchg
			self._AcqrrToAccptrBtchFileXchg = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcqrrToAccptrBtchFileXchg', type=AcquirerToAcceptorBatchFileExchangeV03, min=1, max=1, mutex_group=None, array=False),
		))