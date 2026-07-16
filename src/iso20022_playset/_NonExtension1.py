# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationMethod1Choice
from . import Max140Text
from . import Number
from . import PartyType1Choice
from . import PostalAddress6

class NonExtension1(base_types._BaseFieldType):

	__slots__ = ["_NtfctnMtd", "_NtfctnPrd", "_NtfctnRcptAdr", "_NtfctnRcptNm", "_NtfctnRcptTp"]
	@property
	def NtfctnMtd(self):
		return self._NtfctnMtd

	@NtfctnMtd.setter
	def NtfctnMtd(self, value):
		self._NtfctnMtd = value if value is not None else base_types.UninitialisedField(self, 'NtfctnMtd', CommunicationMethod1Choice, False)

	@NtfctnMtd.deleter
	def NtfctnMtd(self):
		del self._NtfctnMtd
		self._NtfctnMtd = base_types.UninitialisedField(self, 'NtfctnMtd', CommunicationMethod1Choice, False)

	@property
	def NtfctnPrd(self):
		return self._NtfctnPrd

	@NtfctnPrd.setter
	def NtfctnPrd(self, value):
		self._NtfctnPrd = value if value is not None else base_types.UninitialisedField(self, 'NtfctnPrd', Number, False)

	@NtfctnPrd.deleter
	def NtfctnPrd(self):
		del self._NtfctnPrd
		self._NtfctnPrd = base_types.UninitialisedField(self, 'NtfctnPrd', Number, False)

	@property
	def NtfctnRcptAdr(self):
		return self._NtfctnRcptAdr

	@NtfctnRcptAdr.setter
	def NtfctnRcptAdr(self, value):
		self._NtfctnRcptAdr = value if value is not None else base_types.UninitialisedField(self, 'NtfctnRcptAdr', PostalAddress6, False)

	@NtfctnRcptAdr.deleter
	def NtfctnRcptAdr(self):
		del self._NtfctnRcptAdr
		self._NtfctnRcptAdr = base_types.UninitialisedField(self, 'NtfctnRcptAdr', PostalAddress6, False)

	@property
	def NtfctnRcptNm(self):
		return self._NtfctnRcptNm

	@NtfctnRcptNm.setter
	def NtfctnRcptNm(self, value):
		self._NtfctnRcptNm = value if value is not None else base_types.UninitialisedField(self, 'NtfctnRcptNm', Max140Text, False)

	@NtfctnRcptNm.deleter
	def NtfctnRcptNm(self):
		del self._NtfctnRcptNm
		self._NtfctnRcptNm = base_types.UninitialisedField(self, 'NtfctnRcptNm', Max140Text, False)

	@property
	def NtfctnRcptTp(self):
		return self._NtfctnRcptTp

	@NtfctnRcptTp.setter
	def NtfctnRcptTp(self, value):
		self._NtfctnRcptTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnRcptTp', PartyType1Choice, False)

	@NtfctnRcptTp.deleter
	def NtfctnRcptTp(self):
		del self._NtfctnRcptTp
		self._NtfctnRcptTp = base_types.UninitialisedField(self, 'NtfctnRcptTp', PartyType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnMtd', type=CommunicationMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcptTp', type=PartyType1Choice, min=0, max=1, mutex_group=None, array=False),
	))