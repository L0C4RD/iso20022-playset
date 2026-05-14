# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentBatchTransfer14 import CardPaymentBatchTransfer14
from ._ContentInformationType37 import ContentInformationType37
from ._Header56 import Header56

class AcceptorBatchTransferV15(base_types._BaseFieldType):

	__slots__ = ["_BtchTrf", "_Hdr", "_SctyTrlr"]
	@property
	def BtchTrf(self):
		return self._BtchTrf

	@BtchTrf.setter
	def BtchTrf(self, value):
		self._BtchTrf = value if type(value) != base_types.auto else self.make_default("BtchTrf")

	@BtchTrf.deleter
	def BtchTrf(self):
		del self._BtchTrf
		self._BtchTrf = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchTrf', type=CardPaymentBatchTransfer14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))