# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMExceptionAdvice2
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header32

class ATMExceptionAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_ATMXcptnAdvc", "_Hdr", "_PrtctdATMXcptnAdvc", "_SctyTrlr"]
	@property
	def ATMXcptnAdvc(self):
		return self._ATMXcptnAdvc

	@ATMXcptnAdvc.setter
	def ATMXcptnAdvc(self, value):
		self._ATMXcptnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMXcptnAdvc', ATMExceptionAdvice2, False)

	@ATMXcptnAdvc.deleter
	def ATMXcptnAdvc(self):
		del self._ATMXcptnAdvc
		self._ATMXcptnAdvc = base_types.UninitialisedField(self, 'ATMXcptnAdvc', ATMExceptionAdvice2, False)

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
	def PrtctdATMXcptnAdvc(self):
		return self._PrtctdATMXcptnAdvc

	@PrtctdATMXcptnAdvc.setter
	def PrtctdATMXcptnAdvc(self, value):
		self._PrtctdATMXcptnAdvc = value if value is not None else base_types.UninitialisedField(self, 'PrtctdATMXcptnAdvc', ContentInformationType10, False)

	@PrtctdATMXcptnAdvc.deleter
	def PrtctdATMXcptnAdvc(self):
		del self._PrtctdATMXcptnAdvc
		self._PrtctdATMXcptnAdvc = base_types.UninitialisedField(self, 'PrtctdATMXcptnAdvc', ContentInformationType10, False)

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
		base_types.FieldEntry(name='ATMXcptnAdvc', type=ATMExceptionAdvice2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdATMXcptnAdvc', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))