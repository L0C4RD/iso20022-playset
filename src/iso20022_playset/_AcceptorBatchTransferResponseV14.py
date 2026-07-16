# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentBatchTransferResponse13
from . import ContentInformationType37
from . import Header56

class AcceptorBatchTransferResponseV14(base_types._BaseFieldType):

	__slots__ = ["_BtchTrfRspn", "_Hdr", "_SctyTrlr"]
	@property
	def BtchTrfRspn(self):
		return self._BtchTrfRspn

	@BtchTrfRspn.setter
	def BtchTrfRspn(self, value):
		self._BtchTrfRspn = value if value is not None else base_types.UninitialisedField(self, 'BtchTrfRspn', CardPaymentBatchTransferResponse13, False)

	@BtchTrfRspn.deleter
	def BtchTrfRspn(self):
		del self._BtchTrfRspn
		self._BtchTrfRspn = base_types.UninitialisedField(self, 'BtchTrfRspn', CardPaymentBatchTransferResponse13, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header56, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header56, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrfRspn', type=CardPaymentBatchTransferResponse13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))