# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcquirerToAcceptorFileBody3
from . import ContentInformationType38
from . import Header56
from . import ResponseType11

class AcquirerToAcceptorBatchFileExchangeV03(base_types._BaseFieldType):

	__slots__ = ["_BodyElmt", "_Hdr", "_Rspn", "_SctyTrlr"]
	@property
	def BodyElmt(self):
		return self._BodyElmt

	@BodyElmt.setter
	def BodyElmt(self, value):
		self._BodyElmt = value if value is not None else base_types.UninitialisedField(self, 'BodyElmt', AcquirerToAcceptorFileBody3, True)

	@BodyElmt.deleter
	def BodyElmt(self):
		del self._BodyElmt
		self._BodyElmt = base_types.UninitialisedField(self, 'BodyElmt', AcquirerToAcceptorFileBody3, True)

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
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType38, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BodyElmt', type=AcquirerToAcceptorFileBody3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))