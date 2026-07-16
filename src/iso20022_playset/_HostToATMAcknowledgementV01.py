# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType10
from . import ContentInformationType15
from . import Header20
from . import HostToATMAcknowledgement1

class HostToATMAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_HstToATMAck", "_PrtctdHstToATMAck", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header20, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header20, False)

	@property
	def HstToATMAck(self):
		return self._HstToATMAck

	@HstToATMAck.setter
	def HstToATMAck(self, value):
		self._HstToATMAck = value if value is not None else base_types.UninitialisedField(self, 'HstToATMAck', HostToATMAcknowledgement1, False)

	@HstToATMAck.deleter
	def HstToATMAck(self):
		del self._HstToATMAck
		self._HstToATMAck = base_types.UninitialisedField(self, 'HstToATMAck', HostToATMAcknowledgement1, False)

	@property
	def PrtctdHstToATMAck(self):
		return self._PrtctdHstToATMAck

	@PrtctdHstToATMAck.setter
	def PrtctdHstToATMAck(self, value):
		self._PrtctdHstToATMAck = value if value is not None else base_types.UninitialisedField(self, 'PrtctdHstToATMAck', ContentInformationType10, False)

	@PrtctdHstToATMAck.deleter
	def PrtctdHstToATMAck(self):
		del self._PrtctdHstToATMAck
		self._PrtctdHstToATMAck = base_types.UninitialisedField(self, 'PrtctdHstToATMAck', ContentInformationType10, False)

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
		base_types.FieldEntry(name='Hdr', type=Header20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstToATMAck', type=HostToATMAcknowledgement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdHstToATMAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
	))