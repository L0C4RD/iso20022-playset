# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMExceptionAcknowledgement2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMExceptionAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_ATMXcptnAck", "_Hdr", "_PrtctdATMXcptnAck", "_SctyTrlr"]
	@property
	def ATMXcptnAck(self):
		return self._ATMXcptnAck

	@ATMXcptnAck.setter
	def ATMXcptnAck(self, value):
		self._ATMXcptnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMXcptnAck', ATMExceptionAcknowledgement2, False)

	@ATMXcptnAck.deleter
	def ATMXcptnAck(self):
		del self._ATMXcptnAck
		self._ATMXcptnAck = base_types.UninitialisedField(self, 'ATMXcptnAck', ATMExceptionAcknowledgement2, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header32, False)

	@property
	def PrtctdATMXcptnAck(self):
		return self._PrtctdATMXcptnAck

	@PrtctdATMXcptnAck.setter
	def PrtctdATMXcptnAck(self, value):
		self._PrtctdATMXcptnAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMXcptnAck', ContentInformationType10, False)

	@PrtctdATMXcptnAck.deleter
	def PrtctdATMXcptnAck(self):
		del self._PrtctdATMXcptnAck
		self._PrtctdATMXcptnAck = base_types.UninitialisedField(self, 'PrtctdATMXcptnAck', ContentInformationType10, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMXcptnAck', type=ATMExceptionAcknowledgement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMXcptnAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))